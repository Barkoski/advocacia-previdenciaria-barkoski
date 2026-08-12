# Validacao da entrega

Aplicar antes de apresentar analise de autos, indice documental, tabela de provas ou minuta como concluida.

A validacao tem duas camadas. A primeira e humana e vale sempre. A segunda e mecanica, opcional, e so alcanca o que estiver estruturado em JSON.

## Camada 1 — conferencia humana

1. Toda afirmacao factual tem arquivo e pagina, ou rotulo de `ALEGACAO`, `INFERENCIA` ou `CONCLUSAO JURIDICA`.
2. Nenhum `FATO COMPROVADO` se apoia em documento nao lido ou sem localizacao confirmada.
3. Documento `NAO LIDO` nao sustenta fato, requisito ou linha da tabela de provas.
4. Inferencia declara de que fatos foi deduzida e nao foi promovida a fato.
5. Toda lei, sumula, tema ou julgado foi conferido em fonte, ou esta marcado `DE MEMORIA - CONFIRMAR EM FONTE OFICIAL`.
6. Todo prazo mostra ato, termo inicial, forma de ciencia, regra de contagem e fonte; faltando qualquer elemento, sai `PRAZO PENDENTE DE CONFERENCIA HUMANA`.
7. Nenhum numero que va para peca ou calculo foi produzido de cabeca.
8. A prova contraria e a melhor tese do INSS foram enfrentadas.
9. Os documentos internos do INSS foram confrontados entre si.
10. Ha decisao operacional entre as oito, proxima acao e limite de confianca.
11. Nenhum dado de cliente saiu para servico externo sem autorizacao expressa nesta conversa.
12. Os blocos de pendencia existem, inclusive quando vazios.

Falhou algum item: corrigir e repetir a lista. Nao chamar a entrega de completa enquanto houver falha.

## Camada 2 — validador

Quando o caso estiver estruturado conforme o JSON de [identificacao-documental.md](identificacao-documental.md) e houver Python disponivel:

```text
python scripts/previdenciario_tool.py validate caso.json
```

Tambem oferece `pendencias` e `provas`. Usa somente a biblioteca padrao.

O validador recusa a entrega quando encontra, entre outros: fato comprovado sem documento lido e localizado; documento nao lido dentro da tabela de provas; coluna de conferencia vazia ou `NAO` onde a regra exige `SIM`; inferencia sem base declarada; familia documental ou grau fora do conjunto previsto; norma sem estado de conferencia; prazo incompleto que afirma termo final; marco com data aproximada classificado como comprovado; documento nao lido ausente do bloco de pendencias; decisao operacional fora das dez; decisao paralela que repete a principal; e `NAO RECORRER` sem motivo registrado.

## O que o validador nao faz

Ele nao abre pagina, nao confere documento, nao checa vigencia de norma e nao avalia se a delimitacao entre pecas foi bem traçada. Verifica **estrutura, referencias e coerencia interna**, nunca a veracidade do caso.

Resultado sem erro significa que a entrega esta internamente coerente e que as travas mecanizaveis foram respeitadas. Nao significa que os fatos sao verdadeiros, que as paginas citadas contem o que se afirma, nem que a tese procede. A tabela de provas continua sendo roteiro de conferencia, e nenhuma linha dela foi conferida na fonte.

Nao apresentar o resultado do validador ao advogado como se fosse conferencia do caso.
