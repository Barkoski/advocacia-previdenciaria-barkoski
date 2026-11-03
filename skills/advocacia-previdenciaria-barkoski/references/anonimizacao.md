# Anonimizacao

Procedimento para transformar documento ou trecho em versao segura antes de uso
externo autorizado, de publicacao didatica ou de emprego como modelo. Executa o que
[privacidade-e-sigilo.md](privacidade-e-sigilo.md) determina na etapa de minimizacao.

Anonimizar nao dispensa autorizacao: se o destino for externo e envolver dados do
caso, a autorizacao expressa do advogado deve existir antes do envio; a copia anonimizada pode ser preparada localmente para revisao antes dessa decisao.
A skill prepara o material; a decisao de enviar ou publicar e do advogado.

## Principios

1. Anonimizar e sobre o conjunto, nao sobre o nome. Trocar o nome e deixar NB, CPF
   ou numero de processo nao anonimiza nada. O identificador mais forte que restar
   define a protecao real.
2. Contexto reidentifica. Caso raro identifica a pessoa mesmo sem nome. Quando o
   conjunto de atributos e unico, generalizar nao basta: e preciso alterar a
   granularidade ou nao usar o documento.
3. Placeholder neutro e nao sequencial por pessoa real: `[PARTE AUTORA]`,
   `[TESTEMUNHA 1]`, `[PERITO]`, `[EMPREGADOR 1]`. Apelido, primeiro nome e "Cliente
   A" fingem anonimizacao e ainda permitem cruzamento entre documentos.
4. Preservar o merito. Tese, cronologia relativa, natureza do vinculo, agente nocivo
   e valores relevantes precisam sobreviver, senao o documento vira inutil e o
   original acaba sendo enviado.
5. Nunca inventar fato para preencher lacuna. Trecho removido fica marcado como
   removido, nunca completado por suposicao.
6. Pseudonimizacao continua sendo dado pessoal. Usar so quando pedido, e o mapa que
   liga codigo a pessoa nunca vai no mesmo arquivo nem na conversa com a IA.
7. Duas passadas, sempre. A primeira remove o declarado; a segunda procura o que
   reidentifica por combinacao. A maioria dos vazamentos sobrevive a primeira.
8. Terceiro importa tanto quanto o cliente: testemunha, perito, servidor, empregador,
   menor e adverso nao consentiram. Menor de idade e dado de saude de terceiro
   recebem o tratamento mais rigido.
9. Publicar exige leitura humana da versao final. Uso interno tolera risco residual
   baixo; publicacao e irreversivel.

## Primeira passada: identificadores diretos

| Categoria | Exemplos previdenciarios | Tratamento |
|---|---|---|
| Nome | parte, conjuge, dependente, testemunha, perito, procurador, servidor | placeholder por papel |
| Documento | CPF, RG, NIT/PIS/PASEP, CNS, titulo, CNH, certidoes | remover |
| Beneficio e protocolo | NB, DER com data exata, numero de requerimento, protocolo do Meu INSS, senha, comunicado de decisao | remover ou generalizar a data |
| Processo | numero CNJ, vara, comarca, gabinete, numero de recurso, chave do PJe | remover |
| Contato e localizacao | endereco, CEP, telefone, e-mail, coordenadas, nome da propriedade rural, matricula de imovel | generalizar por regiao |
| Vinculo | CNPJ e razao social do empregador, matricula funcional | placeholder por setor |
| Financeiro | conta, agencia, chave PIX, valor de RMI exato quando desnecessario | remover |
| Saude | nome de medico, CRM, numero de prontuario, unidade de saude, laudos com cabecalho | remover cabecalho, manter diagnostico se necessario |
| Arquivo | nome do arquivo, cabecalho, rodape, marca do sistema, QR code, carimbo de assinatura | limpar |

## Segunda passada: reidentificacao por contexto

Perguntar, sobre o texto ja limpo, se o conjunto restante aponta para uma pessoa:

- Combinacao de data de nascimento, cidade pequena e profissao rara.
- Empregador unico na regiao, mesmo sem nome.
- Doenca rara somada a periodo e local.
- Data exata de acidente somada a noticia publica.
- Sequencia de periodos de CNIS suficientemente unica.
- Detalhe processual singular (decisao noticiada, valor atipico, litisconsorcio raro).

Havendo risco, agir por granularidade: ano em vez de data, faixa etaria em vez de
idade, regiao em vez de municipio, setor em vez de empresa, "doenca degenerativa de
coluna" em vez do CID especifico quando o CID nao for o ponto. Se ainda assim o
conjunto for unico, declarar `RISCO DE REIDENTIFICACAO ALTO` e recomendar nao usar o
documento nesse destino.

## Relatorio obrigatorio

Toda anonimizacao entrega, junto com o texto tratado:

`ITEM REMOVIDO OU GENERALIZADO | CATEGORIA | COMO FICOU | ONDE APARECIA`

Mais: risco residual declarado (`BAIXO`, `MEDIO`, `ALTO`) com o motivo; o que foi
preservado de proposito e por que; e trechos que precisam de conferencia humana antes
do envio ou da publicacao.

## Limites

Nao decide segredo de justica, nao redige pedido de sigilo, nao criptografa arquivo e
para remocao de metadados e camadas de PDF, exige ferramenta de arquivo apropriada e conferencia, alem da revisao textual. Documento destinado
a protocolo nos autos nao se anonimiza: ali a qualificacao e obrigatoria.

## Preparacao de arquivo

Pedido de anonimizar autoriza preparar copia local; nao e preciso aprovar o envio antes de existir a versao revisavel. Autorizacao especifica e exigida para o envio externo efetivo. Se o pedido for anonimizar PDF/DOCX, examinar tambem metadados, comentarios, camadas de texto/OCR e imagens com a ferramenta correspondente. Tarja visual sobre texto recuperavel nao e remocao segura. Se a ferramenta nao conseguir remover, declarar a limitacao e nao chamar o arquivo de anonimizado.
