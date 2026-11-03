# Motor de prazo: metodo e limites

Este modulo descreve o metodo de contagem de prazo em dias. O pacote nao traz calculadora: a conta e feita seguindo o metodo abaixo, com conferencia manual da contagem, do calendario do orgao e do primeiro dia contado. Uma calculadora local pode existir no ambiente do advogado, mas nao faz parte deste pacote e, se usada, sua saida e rascunho de conferencia, nunca prazo oficial.

O metodo vale para aritmetica em dias. Nao use para calcular automaticamente prescricao/decadencia em meses ou anos, prazo material ou regras administrativas: esses objetos exigem metodo proprio e marco confirmado.

## Preparar a conta

1. Identifique ato, meio de ciencia, termo inicial e regra aplicavel com fonte. A data atual e referencia para avaliar a situacao do prazo, nao substitui o marco.
2. Fixe o primeiro dia contado ja confirmado e o calendario do orgao. Nessa forma a data informada e o dia 1, nao o dia do ato a excluir. Data sem expediente ou suspensa nao e deslocada em silencio: registre e confirme.
3. Registre quantidade de dias, regime (uteis ou corridos), localidade, fonte/calendario e se ha suspensao de 20/12 a 20/01 aplicavel. Nao presuma recesso para toda especie de prazo.
4. Entregue a memoria da conta (cada dia contado, dias excluidos e motivo), as premissas e os pontos pendentes. Se o ato indicar prazo aparentemente incompativel com a norma, confronte ambos; nao afirme prevalencia automatica do ato.
5. Refaca a contagem manualmente uma segunda vez, de forma independente, e compare o termo final.

## Calendario

Informe todos os dias sem expediente pertinentes ao orgao e ao periodo, incluindo feriados forenses, com a fonte e a data da consulta. A fonte deve identificar o calendario e a norma ou ato consultado, com URL oficial ou arquivo/pagina, e nao somente "tribunal".

Carnaval, Corpus Christi, aniversario municipal e ponto facultativo nao devem ser presumidos como suspensao automatica. Feriado municipal da comarca, portaria de suspensao e indisponibilidade de sistema exigem fonte propria. Suspensao que nao corresponda a feriado ou expediente exige avaliar a regra antes de representa-la na conta.

Sem calendario conferido, a conta e apenas simulacao e deve vir identificada como tal. Nao recomendar lancamento definitivo de prazo a partir de simulacao.

## Modos de ciencia

Data da publicacao e data da disponibilizacao nao se deduzem uma da outra sem fonte. Ciencia por portal e ciencia presumida dependem de regra atual e de logs do sistema: prefira confirmar o primeiro dia contado no proprio sistema do orgao. Este modulo nao certifica regras de ciencia nem de leitura no Domicilio Judicial Eletronico.

Recurso inominado e embargos do JEC contam-se em dias uteis conforme art. 12-A da Lei 9.099/1995, introduzido pela Lei 13.728/2018. Para JEF, confira a aplicacao subsidiaria e particularidades da Lei 10.259/2001; nao aplique dobro ao INSS pelo simples fato de ser autarquia (art. 9o). Para periodo historico, confira a redacao entao vigente. Fontes consultadas em 04/09/2026: [Lei 13.728/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13728.htm), [Lei 10.259/2001](https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10259.htm). Reconfira quando aplicar a caso real.

Prazo em dobro exige motivo normativo identificado; justificativa generica nao prova cabimento. Quantidade de dias, localidade e meio de ciencia invalidos ou inconsistentes devem ser corrigidos antes de contar.

## Saida

Entregar: ato, termo inicial, primeiro dia contado, regime, calendario e fonte, memoria da conta, termo final, alertas sugeridos (datas, nao lembretes agendados) e a lista do que depende de conferencia humana. Sem os elementos acima, sair com `PRAZO PENDENTE DE CONFERENCIA HUMANA`.
