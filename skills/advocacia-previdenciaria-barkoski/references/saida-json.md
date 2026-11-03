# Saida em JSON e conjuntos fechados

Usar **somente quando o advogado pedir saida estruturada** para planilha, base, validador ou automacao. Sem pedido expresso, a entrega e em texto e tabela, conforme [identificacao-documental.md](identificacao-documental.md) e [tabela-de-provas.md](tabela-de-provas.md).

Este e o formato que o validador de [validacao.md](validacao.md) verifica. Exemplos prontos: `examples/caso-ficticio.json` (valido) e `examples/caso-invalido.json` (recusado de proposito, para conferir se o validador ainda acusa).

```json
{
  "schema_version": "1.0",
  "caso": {
    "parte": "", "cpf": "?", "especie": "", "nb": "?", "der": "?",
    "processo_ou_protocolo": "?", "fase": "", "data_referencia": ""
  },
  "triagem": {
    "tipo_procedimento": "", "assunto_principal": "", "questao_central": "",
    "pontos_controvertidos": [], "fundamento_do_indeferimento": "?",
    "palavras_chave": [], "normas_invocadas": [], "origem": ""
  },
  "documentos": [
    {
      "id": "D1", "familia": "", "tipo": "", "titular": "?",
      "evento_inicio": "?", "pagina_inicio": "?",
      "evento_fim": "?", "pagina_fim": "?", "data": "?",
      "localizacao": "", "resumo": "", "criterio_delimitacao": "",
      "confianca_identificacao": "", "qualidade_da_leitura": "", "lido": true,
      "documento_estranho": false, "motivo_divergencia": ""
    }
  ],
  "fatos": [
    {
      "id": "F1", "enunciado": "", "data": "?", "grau": "",
      "documentos": ["D1"], "base_inferencia": "", "origem": ""
    }
  ],
  "provas": [
    { "id": "P1", "documento": "D1", "o_que_prova": "", "requisito": "R1", "conferir": "SIM" }
  ],
  "requisitos": [
    {
      "id": "R1", "enunciado": "", "situacao": "", "fatos": ["F1"],
      "prova_necessaria": "", "favoravel": "", "contraria": "",
      "lacuna": "", "risco": "", "providencia": ""
    }
  ],
  "marcos": [{ "marco": "", "data": "?", "fonte": "D1", "localizacao": "?", "grau": "" }],
  "normas": [{ "referencia": "", "estado": "", "origem": "" }],
  "prazos": [
    {
      "ato": "", "termo_inicial": "?", "forma_ciencia": "?", "regra_contagem": "?",
      "termo_final": "?", "fonte": "D1", "situacao": "PRAZO PENDENTE DE CONFERENCIA HUMANA"
    }
  ],
  "conclusao": "", "decisao_operacional": "", "decisao_paralela": "",
  "motivo_decisao": "", "proxima_acao": "", "confianca": "",
  "pendencias": { "nao_lidos": [], "sem_localizacao": [], "confirmar": [], "estranhos_ao_caso": [] }
}
```

Conjuntos fechados, verificados pelo validador:

- `grau` do fato e do marco: `FATO COMPROVADO`, `ALEGACAO`, `INFERENCIA`, `CONCLUSAO JURIDICA`.
- `situacao` do requisito: `COMPROVADO`, `PARCIALMENTE COMPROVADO`, `CONTROVERTIDO`, `NAO COMPROVADO`, `NAO APLICAVEL`, `?`.
- `qualidade_da_leitura`: `TEXTO NITIDO`, `OCR DUVIDOSO`, `LEITURA PARCIAL`, `ILEGIVEL`, `NAO LIDO`.
- `estado` da norma: `FONTE OFICIAL CONSULTADA AGORA`, `ARQUIVO OFICIAL CAPTURADO`, `ACERVO LOCALIZADOR`, `PESQUISA OFICIAL PENDENTE`, `DE MEMORIA - CONFIRMAR EM FONTE OFICIAL`.
- `decisao_operacional`: uma das dez da entrega padrao do SKILL.md. `decisao_paralela` e opcional, usa o mesmo conjunto e nao pode repetir a principal. `NAO RECORRER` exige `motivo_decisao` preenchido.
- `conferir`: `SIM` ou `NAO`, e obrigatoriamente `SIM` quando a qualidade nao for `TEXTO NITIDO`, quando faltar localizacao, ou quando o titular nao for a parte.

Regras de coerencia que o validador recusa violar: `FATO COMPROVADO` exige documento lido e com localizacao; documento `NAO LIDO` nao entra em `provas`; `INFERENCIA` exige `base_inferencia`; prazo com elemento ausente exige `situacao` pendente e nao pode afirmar `termo_final`; documento nao lido, sem localizacao, de confianca `BAIXA` ou estranho ao caso precisa constar do bloco de pendencia correspondente.

Campo sem base no material fica `?`; nunca preencher por plausibilidade.

Campos opcionais de documento: `estado_conferencia` (ORIGINAL CONFERIDO, SOMENTE TRANSCRICAO, RELATADO NA CONVERSA, NAO LIDO), `registro_conferencia` e registro de revisao humana separado. O primeiro estado exige leitura, localizacao e registro concreto. Campos extras sao preservados; o validador nao verifica a veracidade do registro. Data parcial nao e automaticamente alegacao.
