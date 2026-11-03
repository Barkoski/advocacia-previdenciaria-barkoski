# Calculos previdenciarios

Finalidade: impedir que indice, taxa, termo inicial ou periodo sejam aplicados por habito. Todo parametro tem de ter fonte juridica identificada e vigencia conferida para o periodo em que incide. Este modulo cuida do valor; o prazo esta em [prazos-e-calculos.md](prazos-e-calculos.md) e [motor-de-prazo.md](motor-de-prazo.md).

Regra que vale acima de tudo o que segue: sem parametro completo e conferido, nao existe valor final. Existe roteiro, premissa e cenario, identificados como `ESTIMATIVA`.

## 1. Dados minimos antes de calcular

- objeto do calculo: RMI, RMA, atrasados, valor da causa, tempo de contribuicao, carencia, contribuicao em atraso ou honorarios;
- especie e enquadramento do beneficio;
- DER, DIB, DIP, DCB e data da citacao;
- periodo de apuracao, com inicio e fim explicitos;
- salarios de contribuicao ou salarios de beneficio disponiveis, com a fonte de cada competencia;
- lacunas do CNIS e competencias sem recolhimento;
- regra de calculo aplicavel a data do fato: redacao vigente da Lei 8.213/1991, EC 103/2019 e regra de transicao pertinente, todas conferidas em fonte oficial;
- titulo judicial, quando houver, com o comando literal sobre correcao, juros e termo inicial;
- valores ja pagos administrativamente;
- beneficio inacumulavel recebido no periodo;
- descontos, IR e contribuicoes incidentes conforme o caso;
- honorarios contratuais e de sucumbencia.

Exigir apenas parametros que alterem o calculo pedido. Lacuna impede valor definitivo, mas permite cenarios condicionais identificados; com dados suficientes, executar a conta deterministica.

## 2. Parametros que nao podem ser afirmados de memoria

Cada linha abaixo e ponto de conferencia obrigatorio em fonte oficial. Sem consulta, rotular `DE MEMORIA — CONFIRMAR EM FONTE OFICIAL` e entregar o roteiro no lugar do valor.

| Parametro | O que conferir |
|---|---|
| Regra de calculo da RMI | redacao vigente na data do fato ou da DER, e regra de transicao aplicavel |
| Correcao monetaria das parcelas vencidas | indice e periodo determinados pelo titulo judicial ou pelo entendimento vinculante vigente |
| Juros de mora | taxa, termo inicial e alteracao legislativa no meio do periodo, inclusive o regime unificado por Selic e sua data de inicio |
| Termo inicial dos atrasados | DER, data da citacao, DII fixada em laudo ou outro marco definido no titulo |
| Prescricao quinquenal | termo inicial e marco interruptivo no caso concreto |
| Honorarios de sucumbencia | base de calculo e alcance das parcelas vencidas, conforme sumula e jurisprudencia vigentes |
| Teto e piso do beneficio | valor vigente em cada competencia do periodo |
| Reajustes anuais | indice e data de cada reajuste do periodo |
| Fator previdenciario e divisor minimo | aplicabilidade a regra invocada |
| Conversao de tempo especial | fator aplicavel a atividade, ao periodo e a norma vigente a epoca |

## 3. Memoria de calculo

Todo calculo relevante expoe, nesta ordem:

1. objeto e periodo;
2. valor ou tempo inicial;
3. cada parametro com sua fonte juridica e a vigencia conferida;
4. indice de atualizacao e fonte da serie, com data da consulta;
5. taxa de juros e termo inicial;
6. formula ou metodologia;
7. valores ja pagos e demais abatimentos, na data efetiva;
8. honorarios, quando aplicaveis;
9. resultado;
10. o que muda o resultado se um parametro em aberto for confirmado de outro modo.

Encerrar com:

**[CONFERIR CALCULO]**

O resultado produzido aqui e rascunho de trabalho. Valor que vai para peca, acordo ou impugnacao passa por planilha, calculadora deterministica ou sistema especializado do escritorio.

## 4. Atrasados

Calcular competencia a competencia, nunca por multiplicacao de um valor medio pelo numero de meses, salvo se a estimativa estiver declarada como tal.

Tabela util:

| Competencia | Valor devido | Correcao ate a data-base | Juros | Ja pago | Beneficio inacumulavel | Saldo |
|---|---:|---:|---:|---:|---:|---:|

Conferir sempre: cabimento e valor do decimo terceiro para a especie e periodo; parcelas atingidas pela prescricao; periodo em que a parte recebeu outro beneficio; e periodo ja pago por tutela antecipada.

## 5. Tempo de contribuicao e carencia

- somar periodos com inicio e fim exatos, sem arredondar mes;
- identificar e nao contar em dobro periodos concomitantes;
- separar tempo comum, tempo especial e tempo rural, com o fundamento de cada um;
- registrar competencias sem recolhimento e o efeito de cada uma sobre carencia e qualidade de segurado;
- indicar a fonte de cada periodo: CNIS por pagina, CTPS por folha, PPP, certidao ou sentenca;
- apresentar o total em anos, meses e dias, com a data-limite da contagem explicita;
- quando houver conversao de tempo especial, mostrar o periodo antes e depois da conversao e o fator usado, com a norma que o autoriza.

## 6. Valor da causa

Distinguir o que compoe: parcelas vencidas ate a data do ajuizamento mais o numero de prestacoes vincendas admitido pelo criterio aplicavel. Quando a RMI nao for apuravel, apresentar estimativa somente com premissas expressas e justificadas; sem base numerica, manter campo pendente, nunca atribuir valor arbitrario. Nao escolher valor para caber no limite do JEF sem registrar a renuncia, quando ela for a opcao deliberada do advogado.

## 7. Conferencia da implantacao

Depois da concessao, comparar o que o INSS implantou com o que o titulo determinou: especie, DIB, DIP, RMI, periodos averbados e composicao da renda. Divergencia vira peticao com o confronto item a item, e nao pedido generico de cumprimento.

## 8. Erros a evitar

- aplicar indice ou taxa por costume, sem verificar o periodo de vigencia;
- ignorar alteracao legislativa no meio do periodo de calculo;
- misturar correcao e juros sem base;
- esquecer valores ja pagos administrativamente ou por tutela;
- desprezar beneficio inacumulavel recebido no periodo;
- somar periodos concomitantes;
- usar teto ou salario minimo de um ano em competencia de outro;
- tratar estimativa como valor liquido;
- apresentar valor final quando um parametro segue pendente de conferencia.
