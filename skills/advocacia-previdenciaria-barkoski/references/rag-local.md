# Documento digitalizado, OCR e RAG local

Processo administrativo e judicial previdenciario quase sempre mistura pagina nato-digital com pagina escaneada. Ler as duas como se fossem a mesma coisa e a principal fonte de erro. Este modulo define como separar uma da outra e o que pode ser afirmado a partir de cada uma.

## 1. Conferir a paginacao antes de citar

Nunca confiar na contagem de paginas anunciada pelo ambiente, pelo nome do arquivo ou pelo indice. Ler os metadados do proprio PDF e usar esse numero.

Divergencia entre a contagem anunciada e a real e comum e ja foi observada em processos reais. Se houver divergencia, registrar as duas e trabalhar com a do arquivo. Citar pagina com base em contagem errada invalida toda a rastreabilidade.

Quando o rodape do documento trouxer a propria numeracao (`Pagina X de Y`), conferir se bate com a posicao no PDF e informar as duas quando divergirem.

## 2. Diagnosticar a camada de texto antes de concluir que "nao ha nada"

Extrair texto de uma amostra de paginas e medir o volume por pagina:

- **Pagina com poucas dezenas de caracteres, repetindo carimbo, ID de anexo, numeracao ou data de emissao**: e pagina de IMAGEM. O conteudo existe e nao foi lido.
- **Pagina com centenas ou milhares de caracteres**: e nato-digital. O conteudo foi lido.

Registrar essa separacao explicitamente. `AUSENCIA DE TEXTO EXTRAIDO NAO E AUSENCIA DE CONTEUDO` — jamais tratar pagina de imagem como pagina vazia, como documento inexistente ou como prova ausente.

Um mesmo PDF costuma ter os dois tipos: peticoes, despachos, telas de sistema e extratos de CNIS costumam ter texto; documentos do segurado (CTPS, notas fiscais, certidoes, laudos, fotos) costumam ser imagem.

## 3. Mapear o documento antes de ler em profundidade

Em processo extenso, localizar antes de ler:

- Buscar pelo identificador de anexo no rodape para descobrir onde comeca e termina cada documento juntado. Isso funciona mesmo quando o corpo da pagina e imagem, porque o carimbo costuma ser texto.
- Buscar termos decisivos: `INDEFER`, `EXIGENCIA`, `DESPACHO`, `ANALISE`, `CNIS`, `DER`, `AUTODECLARACAO`, `COMUNICACAO DE DECISAO`, `RESUMO DE BENEFICIO`, `DESCRITIVO`.
- So depois abrir as faixas relevantes e o entorno.

Declarar quais faixas foram lidas e marcar `LEITURA PARCIAL` para o restante. Nunca deixar implicito que o documento inteiro foi lido.

## 4. Ler a pagina de imagem quando ela for decisiva

Pagina de imagem que sustenta requisito, prova ou prazo nao pode ficar sem leitura. Rotas, em ordem de preferencia:

1. **Renderizar a pagina e ler visualmente.** Melhor fidelidade para manuscrito, carimbo, assinatura, tabela e documento torto ou degradado.
2. **OCR local do escritorio**, quando existir, para volume grande. Adequado para triagem; conferir visualmente o que for decisivo.
3. **Se nenhuma rota estiver disponivel**, dizer isso com todas as letras e listar exatamente quais paginas ficaram sem leitura e o que dependeria delas.

Nunca deduzir o conteudo de uma pagina de imagem a partir do nome do arquivo, da descricao no indice de anexos ou do que seria "esperado" naquele tipo de documento. Nome de arquivo e alegacao da parte que juntou, nao prova do conteudo.

## 5. Qualidade da leitura e o que ela permite afirmar

Para todo trecho aproveitado de pagina digitalizada, registrar a qualidade: `TEXTO NITIDO`, `OCR DUVIDOSO`, `LEITURA PARCIAL` ou `ILEGIVEL`.

Exigem conferencia humana antes de ir para peca, sem excecao: nome proprio, CPF, NB, numero de processo, data, valor, periodo, numero de matricula ou de CCIR, e qualquer numero que sustente calculo. Manuscrito e carimbo desbotado sao os pontos de erro mais frequentes.

Nao reconstruir, completar nem "corrigir" texto incerto. Trecho duvidoso vai entre colchetes com o rotulo de qualidade, ou nao vai.

## 6. RAG e busca semantica

Resultado de busca semantica e candidato de leitura, nunca fonte. Antes de citar, abrir a pagina indicada e conferir.

Registrar arquivo de origem, pagina, trecho, data de extracao e qualidade. Isolar casos e clientes por pasta e permissao; nao misturar bases sem autorizacao.

Transcricao gerada por assistente local e leitura de apoio: a fonte citada continua sendo o documento original, pagina X.

Em jurisprudencia recuperada de acervo, aplicar [jurisprudencia.md](jurisprudencia.md) antes de cita-la como atual ou oficial. Em calculo, extrair premissas e usar ferramenta deterministica para o resultado final.

## 7. Saida obrigatoria

Toda analise que envolva documento digitalizado declara, antes das conclusoes:

- Total real de paginas, e a divergencia se houver.
- Quais faixas foram lidas e por qual meio.
- Quais faixas sao imagem e ficaram sem leitura.
- O que especificamente depende dessas paginas nao lidas.

E monta a tabela de provas do modulo [tabela-de-provas.md](tabela-de-provas.md).
