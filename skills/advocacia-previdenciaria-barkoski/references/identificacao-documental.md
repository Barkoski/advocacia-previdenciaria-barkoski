# Identificacao documental e indice de pecas

Aplicar quando o material contiver texto de autos, eventos, anexos ou paginas: PDF integral de processo, copia do PJe, processo administrativo do INSS, dossie do Meu INSS ou lote de documentos do cliente.

Objetivo: montar um mapa verificavel do material **antes** da analise probatoria. Identificar nao e avaliar. Primeiro delimitar e classificar; so depois ligar documento a fato, requisito ou tese.

Indice, sumario do sistema, extracao automatica e OCR sao ponto de partida, nunca prova.

## Sequencia

1. Percorrer o material na ordem em que aparece.
2. Detectar fronteiras por cabecalho, evento, titulo, assinatura, carimbo, mudanca de emissor ou mudanca de numeracao. Nao separar apenas por mudanca de assunto.
3. Criar um documento por unidade autonoma. Evento com varias pecas se segmenta; paginas que formam a mesma peca ficam juntas.
4. Registrar inicio e fim exatamente como expostos. Usar `?` quando ausentes e marcar a delimitacao `INCERTA` quando a fronteira nao estiver demonstrada.
5. Resumir em uma ou duas frases concretas, sem conclusao juridica nova.
6. So depois relacionar o documento ao requisito, ao fato e a tese.

Fronteiras tipicas no material previdenciario:

- Processo administrativo vem como PDF unico com dezenas de pecas coladas: separar por cabecalho do INSS, numero de protocolo, data de juntada e mudanca de servidor ou setor.
- CNIS e um documento so, ainda que ocupe muitas paginas; nao fragmentar por vinculo.
- CTPS digitalizada: separar por pagina de contrato, mantendo juntas as paginas do mesmo vinculo.
- PPP e LTCAT sao documentos distintos mesmo quando juntados no mesmo anexo.
- Laudo pericial e os quesitos que o acompanham sao pecas separadas.

## Familias e tipo normalizado

Usar uma **familia estavel** da lista abaixo e um **tipo normalizado descritivo** em texto livre. A familia padroniza; o tipo descreve. Nao forcar documento em familia que nao serve.

- `PECA_PROCESSUAL`: inicial, emenda, contestacao, replica, impugnacao, recurso inominado, contrarrazoes, apelacao, memoriais, peticao.
- `DECISAO_JUDICIAL`: despacho, decisao interlocutoria, tutela, sentenca, acordao, voto.
- `ATO_PROCESSUAL`: citacao, intimacao, certidao, ata e termo de audiencia, mandado, oficio, transito em julgado.
- `REQUERIMENTO_ADMINISTRATIVO`: requerimento, agendamento, protocolo, carta de exigencia, cumprimento de exigencia, recurso a Junta, recurso especial ao Conselho.
- `DECISAO_ADMINISTRATIVA`: carta de indeferimento, comunicacao de decisao, carta de concessao, dados basicos da concessao, memoria de calculo da RMI, acordao de Junta ou de Camara, cessacao de beneficio, cobranca de valor recebido indevidamente.
- `VINCULO_E_CONTRIBUICAO`: CNIS, CTPS, contrato e rescisao, ficha de registro, CTC, contagem de tempo, relacao de salarios de contribuicao, GPS, carne, recolhimento complementar, HISCRE.
- `ATIVIDADE_ESPECIAL`: PPP, LTCAT, laudo de condicoes ambientais, PPRA/PGR, formulario DSS-8030/SB-40, CAT, ficha de EPI, descricao de funcao.
- `PROVA_RURAL`: autodeclaracao rural, declaracao sindical, bloco de notas de produtor, nota fiscal de produtor, INCRA/CCIR, ITR, DAP/CAF, CAR, contrato de arrendamento, parceria ou comodato, matricula de imovel rural.
- `PROVA_MEDICA`: atestado, relatorio medico, exame, prontuario, receituario, alta hospitalar, ASO, comunicacao de afastamento.
- `PROVA_SOCIOECONOMICA`: estudo social, avaliacao social do INSS, CadUnico, declaracao de composicao familiar, comprovante de renda do grupo familiar, despesa medica continuada, comprovante de residencia.
- `PROVA_PESSOAL`: depoimento, declaracao de terceiro, entrevista rural, pesquisa externa do INSS, justificacao administrativa e seu resultado.
- `PARECER_OU_LAUDO_TECNICO`: laudo pericial judicial, conclusao da pericia medica do INSS, comunicado de resultado de pericia, quesitos, impugnacao ao laudo, parecer de assistente tecnico, parecer da contadoria.
- `PROVA_CIVIL`: identidade, CPF, CNH, certidao de nascimento, casamento ou obito, declaracao de uniao estavel, curatela, procuracao, substabelecimento, declaracao de hipossuficiencia.
- `PROVA_ECONOMICA`: contracheque, ficha financeira, extrato de pagamento de beneficio, calculo, planilha, RPV, precatorio, alvara.
- `MIDIA`: fotografia, audio, video ou outro arquivo multimidia.
- `OUTRO`: somente quando nenhuma familia couber; explicar o tipo no resumo.

Nao copiar cegamente o rotulo cadastrado no sistema ou o nome do arquivo. Classificar pelo que o documento efetivamente e; havendo divergencia, preservar o rotulo original em observacao e rebaixar a confianca.

## Campos e confianca

Cada documento carrega: `id`, `familia`, `tipo`, `titular`, `evento_inicio`, `pagina_inicio`, `evento_fim`, `pagina_fim`, `data`, `resumo`, `criterio_delimitacao`, `confianca_identificacao`, `qualidade_da_leitura` e `lido`.

`confianca_identificacao`:

- `ALTA`: titulo, cabecalho ou metadado confirma tipo e limites.
- `MEDIA`: o conteudo confirma o tipo, mas um limite depende da sequencia.
- `BAIXA`: fragmento, OCR ruim ou ausencia de marcadores impede identificacao segura.

Confianca baixa nao impede o registro; gera item em `confirmar antes de usar`.

`qualidade_da_leitura`: `TEXTO NITIDO`, `OCR DUVIDOSO`, `LEITURA PARCIAL`, `ILEGIVEL` ou `NAO LIDO`.

`titular` e campo obrigatorio: em nome de quem o documento foi emitido, com CPF ou NB quando visivel. Documento em nome de terceiro sustenta prova por extensao, nunca prova direta — e e onde o INSS ataca primeiro. Desconhecido e `?`; nunca presumir que seja do requerente.

Divergencia de pessoa, CPF, NB, especie ou periodo: registrar `POSSIVEL DOCUMENTO ESTRANHO AO CASO` com o motivo objetivo.

## Regras de preenchimento

- Celula vazia e erro. Usar `?` para desconhecido e `—` para nao aplicavel.
- Localizacao exatamente na forma em que aparece: `p. 47`, `pp. 63-65`, `evento 12`, `fl. 117`, `ID 916401037`. Havendo duas numeracoes, PDF e autos, registrar as duas.
- Sem localizacao: `PAGINA NAO IDENTIFICADA`. Nunca estimar, arredondar ou deduzir por proximidade. Limite estimado vai rotulado `INCERTO`, jamais como pagina confirmada.
- Resumo traz o dado que individualiza: `nota fiscal de leite, 320 litros, 03/2015` serve; `documento comprobatorio` nao.
- Documento `NAO LIDO` **nao entra** na tabela de provas nem sustenta fato algum, por mais sugestivo que seja o nome do arquivo. Vai para pendencias.
- Nao promover grau: documento mencionado sem localizacao nao vira `FATO COMPROVADO`.
- Nao transformar quantidade de documentos em forca juridica ou probabilidade de exito.

## Indice documental

| ID | Familia | Tipo normalizado | Titular | Inicio | Fim | Data | Resumo | Delimitacao | Confianca | Qualidade |
|---|---|---|---|---|---|---|---|---|---|---|

Ordenar pela posicao no processo, nao por relevancia. A ordenacao por relevancia e da tabela de provas.

## Triagem previdenciaria

Preencher apenas com o material do caso:

- `especie_e_beneficio`: especie, NB e DER identificados; `?` se ausentes.
- `tipo_procedimento`: via administrativa ou judicial, classe ou recurso, fase.
- `assunto_principal`: rotulo curto, sem antecipar a conclusao. Preferir um destes: `Aposentadoria por idade urbana`; `Aposentadoria por idade rural`; `Aposentadoria por tempo de contribuicao`; `Aposentadoria da pessoa com deficiencia`; `Tempo especial`; `Aposentadoria especial`; `Beneficio por incapacidade`; `Auxilio-acidente`; `Beneficio de prestacao continuada - LOAS`; `Pensao por morte`; `Auxilio-reclusao`; `Salario-maternidade`; `Salario-maternidade rural`; `Averbacao de tempo`; `Revisao da RMI`; `Revisao da vida toda`; `Revisao do teto EC 20/98 e EC 41/03`; `Restabelecimento de beneficio`; `Cobranca de valores por suposto recebimento indevido`; `Reafirmacao da DER`. Se nenhum servir, criar rotulo compacto e dizer que e novo.
- `questao_central`: pergunta juridica unica e decidivel, enfrentada nos documentos.
- `pontos_controvertidos`: divergencias efetivamente presentes no material.
- `fundamento_do_indeferimento`: motivo real dado pelo INSS, transcrito na forma em que aparece; `?` se a decisao nao foi lida.
- `palavras_chave`: termos que descrevem fatos, beneficio e entidades. Nao inserir nome de pessoa. Nao usar nome de peca nem referencia a norma.
- `normas_invocadas`: somente normas e precedentes citados no material, em forma compacta, com o artigo apos virgula: `L 8.213/1991, Art. 42`; `EC 103/2019, Art. 19`; `Sumula 77 TNU`; `Tema 1.007 STJ`. Norma trazida de memoria vai com `DE MEMORIA — CONFIRMAR EM FONTE OFICIAL`.
- `origem`: arquivo, evento ou intervalo de paginas que sustenta a triagem.

Nao declarar conhecimento juridico atualizado, nao completar norma de memoria e nao converter classificacao documental em conclusao sobre o merito.

## Marcos temporais

Antes da cronologia, isolar os marcos que decidem o caso, cada um com fonte e pagina. Nao fundir marcos distintos: DER, DIB, DID, DII, DCB, DIP, data do requerimento, ciencia, exigencia, cumprimento, indeferimento, recurso e obito.

| Marco | Data | Fonte | Localizacao | Grau |
|---|---|---|---|---|

Data aproximada vem com `~` e grau rebaixado para `ALEGACAO`, salvo documento que a confirme. Periodo em aberto se escreve `desde 03/2019` ou `ate 12/2020`; nao fechar intervalo por conta propria.

## Analise apos o indice

Com o indice fechado, seguir para [analise-de-caso.md](analise-de-caso.md) e [padrao-de-evidencia.md](padrao-de-evidencia.md). Quando o advogado pedir a analise estruturada junto do indice, entregar nesta ordem:

1. `FATOS`, com marcos temporais separados e cada fato com fonte e pagina.
2. `PROBLEMA JURIDICO` e `QUESTAO CENTRAL`.
3. `PONTOS CONTROVERTIDOS`.
4. `DIREITO APLICAVEL`: normas e precedentes referenciados no material, com a regra de tempo aplicavel e as transicoes que incidem.
5. `ARGUMENTOS E PROVAS DA PARTE AUTORA`, cada um com prova de apoio e inferencia explicita.
6. `ARGUMENTOS E PROVAS DO INSS`, incluindo o fundamento real do indeferimento e a conclusao da pericia ou da avaliacao social.
7. `APLICACAO DA NORMA`: requisito a requisito, confrontando elemento normativo, prova e contraprova, na matriz de [padrao-de-evidencia.md](padrao-de-evidencia.md).
8. `CONCLUSAO`: havendo decisao, sintetizar o que foi decidido e por que. Nao havendo, nao julgar: indicar encaminhamento e escolher a decisao operacional da skill.

## Saida em JSON

Somente quando o advogado pedir saida estruturada para planilha, base ou automacao. Sem pedido expresso, entregar em texto e tabela.

Este e o formato que o validador de [validacao.md](validacao.md) verifica. Exemplo completo e valido em `examples/caso-ficticio.json`.

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

Regras de coerencia que o validador recusa violar: `FATO COMPROVADO` exige documento lido e com localizacao; documento `NAO LIDO` nao entra em `provas`; `INFERENCIA` exige `base_inferencia`; prazo com elemento ausente exige `situacao` pendente e nao pode afirmar `termo_final`; marco com data em `~` sai como `ALEGACAO`; documento nao lido, sem localizacao, de confianca `BAIXA` ou estranho ao caso precisa constar do bloco de pendencia correspondente.

Campo sem base no material fica `?`; nunca preencher por plausibilidade.

## Fechamento

Toda entrega termina com quatro blocos curtos, e bloco vazio se declara vazio:

- **Nao lidos**: documento citado ou juntado que nao chegou a ser aberto, com o que dependeria dele.
- **Sem localizacao**: item cuja pagina ou evento nao foi identificado.
- **Confirmar antes de usar**: confianca `BAIXA`, delimitacao `INCERTA`, OCR duvidoso, titular diverso do requerente, e todo numero, data ou valor que va para peca ou calculo.
- **Estranhos ao caso**: documentos segregados, com o motivo da divergencia.

Fechar o indice com a frase: **nenhuma linha foi conferida na fonte; o indice e roteiro de conferencia.** Declarar tambem o que nao foi coberto: paginas nao lidas, trechos ilegiveis, anexos nao abertos e volumes ausentes. Sem essa declaracao, o indice nao esta entregue.
