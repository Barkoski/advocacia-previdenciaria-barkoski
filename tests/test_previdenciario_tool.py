"""Testes do validador previdenciario.

Cada teste quebra deliberadamente uma trava da skill e exige que o validador
recuse. O caso de exemplo deve passar sem erro.
"""

import copy
import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "advocacia-previdenciaria-barkoski" / "scripts"))

import previdenciario_tool as tool  # noqa: E402

EXAMPLE = ROOT / "examples" / "caso-ficticio.json"


def load_example():
    return copy.deepcopy(tool.load_json(EXAMPLE))


def find(data, collection, entity_id):
    for item in data[collection]:
        if item["id"] == entity_id:
            return item
    raise AssertionError("entidade nao encontrada: " + entity_id)


class ValidateExampleTest(unittest.TestCase):
    def test_example_is_valid(self):
        errors, _ = tool.validate(load_example())
        self.assertEqual(errors, [])


class FactGradeTest(unittest.TestCase):
    def test_proven_fact_requires_document(self):
        data = load_example()
        find(data, "fatos", "F1")["documentos"] = []
        errors, _ = tool.validate(data)
        self.assertTrue(any("fato comprovado sem documento" in e for e in errors))

    def test_proven_fact_rejects_unread_document(self):
        data = load_example()
        find(data, "fatos", "F1")["documentos"] = ["D4"]
        errors, _ = tool.validate(data)
        self.assertTrue(any("documento nao lido" in e for e in errors))

    def test_proven_fact_rejects_document_without_location(self):
        data = load_example()
        find(data, "documentos", "D1")["localizacao"] = tool.NO_LOCATION
        errors, _ = tool.validate(data)
        self.assertTrue(any("sem localizacao" in e for e in errors))

    def test_invalid_grade_is_rejected(self):
        data = load_example()
        find(data, "fatos", "F4")["grau"] = "PROVAVEL"
        errors, _ = tool.validate(data)
        self.assertTrue(any("grau invalido" in e for e in errors))

    def test_inference_requires_basis(self):
        data = load_example()
        find(data, "fatos", "F3")["base_inferencia"] = ""
        errors, _ = tool.validate(data)
        self.assertTrue(any("inferencia sem base_inferencia" in e for e in errors))

    def test_fact_cannot_point_to_missing_document(self):
        data = load_example()
        find(data, "fatos", "F1")["documentos"] = ["D99"]
        errors, _ = tool.validate(data)
        self.assertTrue(any("documento inexistente" in e for e in errors))


class EvidenceTableTest(unittest.TestCase):
    def test_unread_document_cannot_enter_table(self):
        data = load_example()
        find(data, "provas", "P1")["documento"] = "D4"
        errors, _ = tool.validate(data)
        self.assertTrue(any("nao entra na tabela de provas" in e for e in errors))

    def test_confirm_is_mandatory_for_doubtful_ocr(self):
        data = load_example()
        find(data, "provas", "P1")["conferir"] = "NAO"
        errors, _ = tool.validate(data)
        self.assertTrue(any("conferir deve ser SIM" in e for e in errors))

    def test_confirm_is_mandatory_for_third_party_holder(self):
        data = load_example()
        find(data, "provas", "P2")["conferir"] = "NAO"
        errors, _ = tool.validate(data)
        self.assertTrue(any("conferir deve ser SIM" in e for e in errors))

    def test_confirm_column_cannot_be_empty(self):
        data = load_example()
        find(data, "provas", "P1")["conferir"] = ""
        errors, _ = tool.validate(data)
        self.assertTrue(any("conferir deve ser SIM ou NAO" in e for e in errors))


class DocumentTest(unittest.TestCase):
    def test_invalid_family_is_rejected(self):
        data = load_example()
        find(data, "documentos", "D2")["familia"] = "PROVA_AGRICOLA"
        errors, _ = tool.validate(data)
        self.assertTrue(any("familia documental invalida" in e for e in errors))

    def test_delimitation_criterion_is_required(self):
        data = load_example()
        find(data, "documentos", "D2")["criterio_delimitacao"] = ""
        errors, _ = tool.validate(data)
        self.assertTrue(any("criterio_delimitacao" in e for e in errors))

    def test_read_flag_must_match_quality(self):
        data = load_example()
        find(data, "documentos", "D4")["lido"] = True
        errors, _ = tool.validate(data)
        self.assertTrue(any("se contradizem" in e for e in errors))

    def test_duplicate_id_is_rejected(self):
        data = load_example()
        duplicate = copy.deepcopy(find(data, "documentos", "D1"))
        data["documentos"].append(duplicate)
        errors, _ = tool.validate(data)
        self.assertTrue(any("id duplicado" in e for e in errors))


class NormAndDeadlineTest(unittest.TestCase):
    def test_norm_requires_confirmation_state(self):
        data = load_example()
        data["normas"][0]["estado"] = "conferida"
        errors, _ = tool.validate(data)
        self.assertTrue(any("estado de conferencia invalido" in e for e in errors))

    def test_incomplete_deadline_must_be_flagged(self):
        data = load_example()
        data["prazos"][0]["situacao"] = "30 dias"
        errors, _ = tool.validate(data)
        self.assertTrue(any(tool.PENDING_DEADLINE in e for e in errors))

    def test_incomplete_deadline_cannot_assert_final_date(self):
        data = load_example()
        data["prazos"][0]["termo_final"] = "19/06/2024"
        errors, _ = tool.validate(data)
        self.assertTrue(any("termo_final afirmado" in e for e in errors))

    def test_approximate_mark_must_be_allegation(self):
        data = load_example()
        data["marcos"][1]["grau"] = "FATO COMPROVADO"
        errors, _ = tool.validate(data)
        self.assertTrue(any("data aproximada" in e for e in errors))


class PendencyTest(unittest.TestCase):
    def test_unread_document_must_appear_in_pendencies(self):
        data = load_example()
        data["pendencias"]["nao_lidos"] = []
        errors, _ = tool.validate(data)
        self.assertTrue(any("ausente de pendencias.nao_lidos" in e for e in errors))

    def test_low_confidence_must_appear_in_confirm_block(self):
        data = load_example()
        data["pendencias"]["confirmar"] = []
        errors, _ = tool.validate(data)
        self.assertTrue(any("ausente de pendencias.confirmar" in e for e in errors))

    def test_empty_blocks_must_exist(self):
        data = load_example()
        del data["pendencias"]["estranhos_ao_caso"]
        errors, _ = tool.validate(data)
        self.assertTrue(any("bloco ausente" in e for e in errors))


class DecisionTest(unittest.TestCase):
    def test_operational_decision_must_be_in_the_closed_set(self):
        data = load_example()
        data["decisao_operacional"] = "Recomendo ajuizar"
        errors, _ = tool.validate(data)
        self.assertTrue(any("decisao_operacional invalida" in e for e in errors))

    def test_judicial_appeal_is_accepted(self):
        data = load_example()
        data["decisao_operacional"] = "RECORRER JUDICIALMENTE"
        errors, _ = tool.validate(data)
        self.assertEqual(errors, [])

    def test_parallel_route_is_optional(self):
        data = load_example()
        self.assertNotIn("decisao_paralela", data)
        errors, _ = tool.validate(data)
        self.assertEqual(errors, [])

    def test_parallel_route_is_accepted_when_valid(self):
        data = load_example()
        data["decisao_operacional"] = "RECORRER JUDICIALMENTE"
        data["decisao_paralela"] = "FAZER NOVO REQUERIMENTO"
        errors, _ = tool.validate(data)
        self.assertEqual(errors, [])

    def test_parallel_route_must_be_in_the_closed_set(self):
        data = load_example()
        data["decisao_paralela"] = "tentar de novo"
        errors, _ = tool.validate(data)
        self.assertTrue(any("decisao_paralela invalida" in e for e in errors))

    def test_parallel_route_cannot_repeat_the_main_decision(self):
        data = load_example()
        data["decisao_paralela"] = data["decisao_operacional"]
        errors, _ = tool.validate(data)
        self.assertTrue(any("repete a decisao_operacional" in e for e in errors))

    def test_not_appealing_requires_a_registered_reason(self):
        data = load_example()
        data["decisao_operacional"] = "NAO RECORRER"
        errors, _ = tool.validate(data)
        self.assertTrue(any("exige motivo_decisao" in e for e in errors))

    def test_not_appealing_is_accepted_with_reason(self):
        data = load_example()
        data["decisao_operacional"] = "NAO RECORRER"
        data["motivo_decisao"] = "Sentenca favoravel integralmente; nada a reformar."
        errors, _ = tool.validate(data)
        self.assertEqual(errors, [])

    def test_requirement_state_must_be_valid(self):
        data = load_example()
        find(data, "requisitos", "R1")["situacao"] = "quase comprovado"
        errors, _ = tool.validate(data)
        self.assertTrue(any("situacao invalida" in e for e in errors))


class CommandTest(unittest.TestCase):
    def test_validate_command_succeeds_on_example(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = tool.main(["validate", str(EXAMPLE)])
        self.assertEqual(code, 0)
        self.assertIn("NAO verificado", buffer.getvalue())

    def test_validate_command_fails_on_broken_case(self, ):
        broken = ROOT / "tests" / "_caso-quebrado.json"
        data = load_example()
        data["decisao_operacional"] = "vamos ver"
        broken.write_text(json.dumps(data), encoding="utf-8")
        try:
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                code = tool.main(["validate", str(broken)])
            self.assertEqual(code, 1)
            self.assertIn("ERRO:", buffer.getvalue())
        finally:
            broken.unlink()

    def test_provas_command_prints_confirmation_notice(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = tool.main(["provas", str(EXAMPLE)])
        self.assertEqual(code, 0)
        self.assertIn("roteiro de conferencia", buffer.getvalue())

    def test_pendencias_command_declares_empty_blocks(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = tool.main(["pendencias", str(EXAMPLE)])
        self.assertEqual(code, 0)
        self.assertIn("bloco vazio", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
