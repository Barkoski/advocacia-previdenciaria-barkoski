#!/usr/bin/env python3
"""Valida casos previdenciarios em JSON sem dependencias externas.

Verifica estrutura, referencias e as travas da skill que sao decidiveis por
maquina. NAO verifica a veracidade do caso: nenhuma pagina e aberta, nenhum
documento e conferido, nenhuma norma e checada em fonte oficial.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCHEMA_VERSION = "1.0"

UNKNOWN = "?"
NO_LOCATION = "PAGINA NAO IDENTIFICADA"

COLLECTIONS = ("documentos", "fatos", "requisitos", "provas")

VALID_FACT_GRADES = {
    "FATO COMPROVADO", "ALEGACAO", "INFERENCIA", "CONCLUSAO JURIDICA",
}
VALID_REQUIREMENT_STATES = {
    "COMPROVADO", "PARCIALMENTE COMPROVADO", "CONTROVERTIDO",
    "NAO COMPROVADO", "NAO APLICAVEL", UNKNOWN,
}
VALID_DOCUMENT_FAMILIES = {
    "PECA_PROCESSUAL", "DECISAO_JUDICIAL", "ATO_PROCESSUAL",
    "REQUERIMENTO_ADMINISTRATIVO", "DECISAO_ADMINISTRATIVA",
    "VINCULO_E_CONTRIBUICAO", "ATIVIDADE_ESPECIAL", "PROVA_RURAL",
    "PROVA_MEDICA", "PROVA_SOCIOECONOMICA", "PROVA_PESSOAL",
    "PARECER_OU_LAUDO_TECNICO", "PROVA_CIVIL", "PROVA_ECONOMICA",
    "MIDIA", "OUTRO",
}
VALID_IDENTIFICATION_CONFIDENCE = {"ALTA", "MEDIA", "BAIXA"}
VALID_READING_QUALITY = {
    "TEXTO NITIDO", "OCR DUVIDOSO", "LEITURA PARCIAL", "ILEGIVEL", "NAO LIDO",
}
VALID_NORM_STATES = {
    "FONTE OFICIAL CONSULTADA AGORA",
    "ARQUIVO OFICIAL CAPTURADO",
    "ACERVO LOCALIZADOR",
    "PESQUISA OFICIAL PENDENTE",
    "DE MEMORIA - CONFIRMAR EM FONTE OFICIAL",
}
VALID_OPERATIONAL_DECISIONS = {
    "AJUIZAR AGORA", "AJUIZAR COM RESSALVA", "RECORRER ADMINISTRATIVAMENTE",
    "FAZER NOVO REQUERIMENTO", "DILIGENCIAR ANTES", "REFORMULAR TESE",
    "NAO AJUIZAR NO ESTADO ATUAL", "ORIENTAR/NEGOCIAR",
}
PENDING_DEADLINE = "PRAZO PENDENTE DE CONFERENCIA HUMANA"
PENDENCY_BLOCKS = ("nao_lidos", "sem_localizacao", "confirmar", "estranhos_ao_caso")


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("a raiz do JSON deve ser um objeto")
    return value


def _is_blank(value) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def _has_location(document: dict) -> bool:
    location = document.get("localizacao")
    if _is_blank(location):
        return False
    return str(location).strip() not in (UNKNOWN, NO_LOCATION)


def index_entities(data: dict) -> "tuple[dict, list]":
    index: dict = {}
    errors: list = []
    for collection in COLLECTIONS:
        items = data.get(collection, [])
        if not isinstance(items, list):
            errors.append(collection + ": deve ser uma lista")
            continue
        for item in items:
            if not isinstance(item, dict) or _is_blank(item.get("id")):
                errors.append(collection + ": entidade sem id")
                continue
            entity_id = str(item["id"])
            if entity_id in index:
                errors.append("id duplicado: " + entity_id)
            merged = dict(item)
            merged["_colecao"] = collection
            index[entity_id] = merged
    return index, errors


def _validate_documents(index: dict, errors: list, warnings: list) -> None:
    for entity_id, item in index.items():
        if item.get("_colecao") != "documentos":
            continue
        if item.get("familia") not in VALID_DOCUMENT_FAMILIES:
            errors.append(entity_id + ": familia documental invalida")
        if item.get("confianca_identificacao") not in VALID_IDENTIFICATION_CONFIDENCE:
            errors.append(entity_id + ": confianca_identificacao invalida")
        if item.get("qualidade_da_leitura") not in VALID_READING_QUALITY:
            errors.append(entity_id + ": qualidade_da_leitura invalida")
        for field in ("tipo", "resumo", "criterio_delimitacao", "titular"):
            if _is_blank(item.get(field)):
                errors.append(entity_id + ": campo obrigatorio vazio: " + field)
        for field in ("evento_inicio", "pagina_inicio", "evento_fim", "pagina_fim"):
            if _is_blank(item.get(field)):
                errors.append(entity_id + ": campo de delimitacao ausente: " + field)
        read = item.get("lido")
        if not isinstance(read, bool):
            errors.append(entity_id + ": campo lido deve ser booleano")
        elif read == (item.get("qualidade_da_leitura") == "NAO LIDO"):
            errors.append(entity_id + ": lido e qualidade_da_leitura se contradizem")
        if item.get("documento_estranho") and _is_blank(item.get("motivo_divergencia")):
            errors.append(entity_id + ": documento estranho sem motivo_divergencia")
        if item.get("titular") == UNKNOWN:
            warnings.append(entity_id + ": titular desconhecido")


def _validate_facts(index: dict, errors: list) -> None:
    documents = {k: v for k, v in index.items() if v.get("_colecao") == "documentos"}
    for entity_id, item in index.items():
        if item.get("_colecao") != "fatos":
            continue
        grade = item.get("grau")
        if grade not in VALID_FACT_GRADES:
            errors.append(entity_id + ": grau invalido: " + str(grade))
        if _is_blank(item.get("enunciado")):
            errors.append(entity_id + ": enunciado vazio")
        doc_ids = item.get("documentos", [])
        if not isinstance(doc_ids, list):
            errors.append(entity_id + ": documentos deve ser uma lista")
            doc_ids = []
        for doc_id in doc_ids:
            if doc_id not in documents:
                errors.append(entity_id + ": documento inexistente: " + str(doc_id))
        if grade == "FATO COMPROVADO":
            if not doc_ids:
                errors.append(entity_id + ": fato comprovado sem documento")
            for doc_id in doc_ids:
                document = documents.get(doc_id)
                if document is None:
                    continue
                if not document.get("lido"):
                    errors.append(
                        entity_id + ": fato comprovado apoiado em documento nao lido: " + str(doc_id)
                    )
                elif not _has_location(document):
                    errors.append(
                        entity_id + ": fato comprovado apoiado em documento sem localizacao: " + str(doc_id)
                    )
        if grade == "INFERENCIA" and _is_blank(item.get("base_inferencia")):
            errors.append(entity_id + ": inferencia sem base_inferencia")


def _validate_evidence_table(data: dict, index: dict, errors: list) -> None:
    documents = {k: v for k, v in index.items() if v.get("_colecao") == "documentos"}
    requirements = {k for k, v in index.items() if v.get("_colecao") == "requisitos"}
    holder = str(data.get("caso", {}).get("parte", "")).strip()
    for entity_id, item in index.items():
        if item.get("_colecao") != "provas":
            continue
        doc_id = item.get("documento")
        document = documents.get(doc_id)
        if document is None:
            errors.append(entity_id + ": documento inexistente: " + str(doc_id))
            continue
        if not document.get("lido"):
            errors.append(entity_id + ": documento nao lido nao entra na tabela de provas")
        if _is_blank(item.get("o_que_prova")):
            errors.append(entity_id + ": o_que_prova vazio")
        requirement_id = item.get("requisito")
        if not _is_blank(requirement_id) and requirement_id not in requirements:
            errors.append(entity_id + ": requisito inexistente: " + str(requirement_id))
        confirm = item.get("conferir")
        if confirm not in ("SIM", "NAO"):
            errors.append(entity_id + ": conferir deve ser SIM ou NAO")
            continue
        must_confirm = (
            document.get("qualidade_da_leitura") != "TEXTO NITIDO"
            or not _has_location(document)
            or (holder != "" and str(document.get("titular", "")).strip() != holder)
        )
        if must_confirm and confirm != "SIM":
            errors.append(entity_id + ": conferir deve ser SIM para esta prova")


def _validate_requirements(index: dict, errors: list) -> None:
    facts = {k for k, v in index.items() if v.get("_colecao") == "fatos"}
    for entity_id, item in index.items():
        if item.get("_colecao") != "requisitos":
            continue
        if item.get("situacao") not in VALID_REQUIREMENT_STATES:
            errors.append(entity_id + ": situacao invalida")
        fact_ids = item.get("fatos", [])
        if not isinstance(fact_ids, list):
            errors.append(entity_id + ": fatos deve ser uma lista")
            continue
        for fact_id in fact_ids:
            if fact_id not in facts:
                errors.append(entity_id + ": fato inexistente: " + str(fact_id))


def _validate_norms(data: dict, errors: list) -> None:
    norms = data.get("normas", [])
    if not isinstance(norms, list):
        errors.append("normas: deve ser uma lista")
        return
    for position, norm in enumerate(norms, 1):
        label = "norma " + str(position)
        if not isinstance(norm, dict):
            errors.append(label + ": formato invalido")
            continue
        if _is_blank(norm.get("referencia")):
            errors.append(label + ": referencia vazia")
        if norm.get("estado") not in VALID_NORM_STATES:
            errors.append(label + ": estado de conferencia invalido")


def _validate_deadlines(data: dict, errors: list) -> None:
    deadlines = data.get("prazos", [])
    if not isinstance(deadlines, list):
        errors.append("prazos: deve ser uma lista")
        return
    for position, deadline in enumerate(deadlines, 1):
        label = "prazo " + str(position)
        if not isinstance(deadline, dict):
            errors.append(label + ": formato invalido")
            continue
        incomplete = any(
            _is_blank(deadline.get(field)) or deadline.get(field) == UNKNOWN
            for field in ("termo_inicial", "forma_ciencia", "regra_contagem")
        )
        if incomplete:
            if deadline.get("situacao") != PENDING_DEADLINE:
                errors.append(label + ": elemento ausente exige situacao " + PENDING_DEADLINE)
            if not _is_blank(deadline.get("termo_final")) and deadline.get("termo_final") != UNKNOWN:
                errors.append(label + ": termo_final afirmado sem elementos confirmados")


def _validate_marks(data: dict, errors: list) -> None:
    marks = data.get("marcos", [])
    if not isinstance(marks, list):
        errors.append("marcos: deve ser uma lista")
        return
    for position, mark in enumerate(marks, 1):
        label = "marco " + str(position)
        if not isinstance(mark, dict):
            errors.append(label + ": formato invalido")
            continue
        if _is_blank(mark.get("marco")):
            errors.append(label + ": nome do marco vazio")
        if mark.get("grau") not in VALID_FACT_GRADES:
            errors.append(label + ": grau invalido")
        date = str(mark.get("data", ""))
        if date.startswith("~") and mark.get("grau") != "ALEGACAO":
            errors.append(label + ": data aproximada exige grau ALEGACAO")


def _validate_pendencies(data: dict, index: dict, errors: list) -> None:
    pendencies = data.get("pendencias")
    if not isinstance(pendencies, dict):
        errors.append("pendencias: deve ser um objeto")
        return
    for block in PENDENCY_BLOCKS:
        if not isinstance(pendencies.get(block), list):
            errors.append("pendencias: bloco ausente ou invalido: " + block)
    if any(not isinstance(pendencies.get(block), list) for block in PENDENCY_BLOCKS):
        return
    unread = set(pendencies["nao_lidos"])
    without_location = set(pendencies["sem_localizacao"])
    to_confirm = set(pendencies["confirmar"])
    strange = set(pendencies["estranhos_ao_caso"])
    for entity_id, item in index.items():
        if item.get("_colecao") != "documentos":
            continue
        if item.get("lido") is False and entity_id not in unread:
            errors.append(entity_id + ": documento nao lido ausente de pendencias.nao_lidos")
        if item.get("lido") and not _has_location(item) and entity_id not in without_location:
            errors.append(entity_id + ": documento sem localizacao ausente de pendencias.sem_localizacao")
        if item.get("confianca_identificacao") == "BAIXA" and entity_id not in to_confirm:
            errors.append(entity_id + ": confianca BAIXA ausente de pendencias.confirmar")
        if item.get("documento_estranho") and entity_id not in strange:
            errors.append(entity_id + ": documento estranho ausente de pendencias.estranhos_ao_caso")


def validate(data: dict) -> "tuple[list, list]":
    errors: list = []
    warnings: list = []

    if str(data.get("schema_version")) != SCHEMA_VERSION:
        errors.append("schema_version deve ser " + SCHEMA_VERSION)
    for key in ("caso", "triagem", "normas", "marcos", "prazos", "pendencias", *COLLECTIONS):
        if key not in data:
            errors.append("campo obrigatorio ausente: " + key)

    case = data.get("caso", {})
    if not isinstance(case, dict):
        errors.append("caso: deve ser um objeto")
    else:
        for key in ("parte", "especie", "fase", "data_referencia"):
            if _is_blank(case.get(key)):
                errors.append("caso: campo ausente: " + key)

    triage = data.get("triagem", {})
    if not isinstance(triage, dict):
        errors.append("triagem: deve ser um objeto")
    else:
        for key in ("tipo_procedimento", "assunto_principal", "questao_central", "origem"):
            if _is_blank(triage.get(key)):
                errors.append("triagem: campo ausente: " + key)
        for key in ("pontos_controvertidos", "palavras_chave"):
            if not isinstance(triage.get(key), list):
                errors.append("triagem: " + key + " deve ser uma lista")

    index, index_errors = index_entities(data)
    errors.extend(index_errors)

    _validate_documents(index, errors, warnings)
    _validate_facts(index, errors)
    _validate_evidence_table(data, index, errors)
    _validate_requirements(index, errors)
    _validate_norms(data, errors)
    _validate_deadlines(data, errors)
    _validate_marks(data, errors)
    _validate_pendencies(data, index, errors)

    decision = data.get("decisao_operacional")
    if decision not in VALID_OPERATIONAL_DECISIONS:
        errors.append("decisao_operacional invalida: " + str(decision))
    if _is_blank(data.get("proxima_acao")):
        errors.append("proxima_acao vazia")

    return errors, warnings


DISCLAIMER = (
    "Verificado: estrutura, referencias e travas decidiveis por maquina. "
    "NAO verificado: veracidade do caso, conteudo de pagina, vigencia de norma "
    "e acerto da delimitacao. Nenhuma linha foi conferida na fonte."
)


def command_validate(args: argparse.Namespace) -> int:
    data = load_json(args.json)
    errors, warnings = validate(data)
    for warning in warnings:
        print("AVISO: " + warning)
    for error in errors:
        print("ERRO: " + error)
    print(DISCLAIMER)
    if errors:
        print("Resultado: " + str(len(errors)) + " erro(s), " + str(len(warnings)) + " aviso(s).")
        return 1
    print("Resultado: sem erros, " + str(len(warnings)) + " aviso(s).")
    return 0


def command_pendencias(args: argparse.Namespace) -> int:
    data = load_json(args.json)
    pendencies = data.get("pendencias", {})
    if not isinstance(pendencies, dict):
        print("pendencias ausente ou invalida")
        return 1
    for block in PENDENCY_BLOCKS:
        items = pendencies.get(block, [])
        if not isinstance(items, list):
            items = []
        print(block + ": " + (", ".join(str(i) for i in items) if items else "bloco vazio"))
    return 0


def command_provas(args: argparse.Namespace) -> int:
    data = load_json(args.json)
    index, _ = index_entities(data)
    documents = {k: v for k, v in index.items() if v.get("_colecao") == "documentos"}
    rows = [v for v in index.values() if v.get("_colecao") == "provas"]
    if not rows:
        print("nenhuma prova registrada")
        return 0
    for row in rows:
        document = documents.get(row.get("documento"), {})
        print(
            " | ".join([
                str(row.get("id")),
                str(document.get("tipo", UNKNOWN)),
                str(document.get("localizacao", NO_LOCATION)),
                str(document.get("titular", UNKNOWN)),
                str(document.get("qualidade_da_leitura", UNKNOWN)),
                str(row.get("o_que_prova", "")),
                "CONFERIR=" + str(row.get("conferir", UNKNOWN)),
            ])
        )
    print("Nenhuma linha foi conferida na fonte. A tabela e roteiro de conferencia.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Valida e consulta casos previdenciarios em JSON.")
    sub = parser.add_subparsers(dest="comando", required=True)

    check = sub.add_parser("validate", help="valida o caso")
    check.add_argument("json", type=Path)
    check.set_defaults(func=command_validate)

    pending = sub.add_parser("pendencias", help="lista os blocos de pendencia")
    pending.add_argument("json", type=Path)
    pending.set_defaults(func=command_pendencias)

    evidence = sub.add_parser("provas", help="imprime a tabela de provas")
    evidence.add_argument("json", type=Path)
    evidence.set_defaults(func=command_provas)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print("Falha ao ler o arquivo: " + str(error))
        return 2


if __name__ == "__main__":
    sys.exit(main())
