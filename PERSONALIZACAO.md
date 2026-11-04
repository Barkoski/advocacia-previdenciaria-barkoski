# 🎨 Personalização do escritório

[← Voltar ao README](README.md)

## 🎨 Personalizar para o seu escritório

A skill nasceu da prática de um escritório específico. Para adaptá-la à sua, **não é preciso editar código na mão** — o próprio Claude faz isso por entrevista.

O ponto de customização é o arquivo `references/configuracao-barkoski.md`. Ele existe justamente para isso: a `## Ordem de controle` do `SKILL.md` dá a ele prioridade sobre o comportamento padrão, então suas preferências se sobrepõem sem precisar tocar nas travas que impedem a alucinação.

> ⚠️ **Regra importante:** personalize apenas `configuracao-barkoski.md`. Os demais módulos (`padrao-de-evidencia.md`, `prazos-e-calculos.md`, `provas-por-materia.md` etc.) contêm as travas de rastreabilidade — mexer neles sem saber a consequência derruba justamente o que faz a skill ser confiável.

### 🧭 Como fazer

Instale a skill, abra o Claude na pasta onde ela está e cole o prompt abaixo. Ele conduz uma entrevista, escreve o arquivo e pede sua confirmação antes de salvar.

```
Você vai me ajudar a personalizar a skill "advocacia-previdenciaria-barkoski"
para o meu escritório.

Regra fixa: toda resposta que eu der vira preferência registrada em
skills/advocacia-previdenciaria-barkoski/references/configuracao-barkoski.md,
organizada em subseções novas (ex: "## Preferências — processo administrativo",
"## Preferências — rural"). NÃO edite o SKILL.md nem os outros módulos de
references/ — são as travas que impedem a IA de inventar fato, data, lei ou
julgado, e minhas preferências de estilo não podem se sobrepor a isso.

ETAPA 1 — Configuração básica. Faça estas 8 perguntas primeiro, em blocos curtos,
esperando minha resposta antes de seguir:

1. Nome do escritório e como devo me referir a ele nas respostas.
2. Tribunal(is) e comarca(s) onde atuo com mais frequência — tem regra local de
   PJe ou de protocolo que eu sigo sempre?
3. Tutela de urgência: em que situação meu escritório pede de cara, e em qual não
   pede sem motivo forte?
4. Valor da causa: uso ferramenta ou planilha própria, ou confirmo manualmente
   antes de protocolar?
5. Estilo de peça: fundamentação mais enxuta ou mais desenvolvida?
6. Revisão de minuta: quero ver fragilidades antes da minuta corrigida, ou tudo
   junto?
7. Tenho acervo local (jurisprudência, modelos, OCR/RAG) que a IA deveria saber
   que existe e como usar?
8. Alguma outra política do escritório que a IA deveria seguir sempre?

Ao fim da etapa 1, me pergunte se quero seguir para a personalização por matéria
(ETAPA 2) ou parar. Se eu parar, mostre o configuracao-barkoski.md final e peça
minha confirmação antes de salvar.

ETAPA 2 — Personalização por matéria (só se eu pedir). Faça bloco por bloco,
esperando minha resposta antes do próximo:

ANÁLISE GERAL
1. No inventário de arquivos, prefere frase curta ou tabela com colunas fixas?
2. Ao achar documento que parece não pertencer ao caso, sinalizo e sigo, ou paro
   e pergunto antes?
3. Na cronologia, incluo eventos administrativos anteriores ao DER, ou só a
   partir do requerimento em discussão?
4. Quando o material é insuficiente para concluir, prefere que eu entregue a
   análise parcial com as lacunas marcadas, ou que eu pare e peça os documentos
   antes de qualquer análise?

PROCESSO ADMINISTRATIVO, CNIS E CTPS
5. Ao ler indeferimento, monto o quadro completo (motivo / requisito / documento
   ignorado / prejuízo) mesmo em caso simples, ou só em caso complexo?
6. No CNIS, sinalizo toda competência abaixo do mínimo automaticamente, ou só
   quando afeta o requisito em discussão?
7. Com CTPS com rasura ou anotação suspeita, já sugiro diligência (justificação,
   perícia grafotécnica) ou só aponto o problema?
8. Indicador do CNIS (extemporaneidade, pendência): explico o significado
   provável marcando como não confirmado, ou só listo o indicador cru?
9. Vínculo concomitante: destaco sempre, mesmo quando não muda o resultado?

RURAL E SEGURADO ESPECIAL
10. Documento de terceiro (vizinho, sindicato, pai) tem peso padrão para você, ou
    trato caso a caso?
11. Verifico renda externa e atividade urbana do grupo familiar sempre, mesmo sem
    menção nos autos, ou só com indício concreto?
12. Ao avaliar extensão temporal do início de prova material, prefere que eu
    separe "cobertura direta / extensão defensável / período sem suporte", ou uma
    conclusão única?
13. Prova oral: sugiro roteiro de perguntas para testemunha quando houver lacuna,
    ou só aponto a lacuna?

INCAPACIDADE E AUXÍLIO-ACIDENTE
14. Contradição entre laudo particular e perícia do INSS: destaco sempre como
    ponto central, ou você decide o peso caso a caso?
15. Em DII controvertida, sugiro quesitos complementares ao perito, ou só em
    lacuna grave?
16. Tem lista própria de documentos que sempre pede (exames, histórico laboral,
    receituário) que eu deva conferir automaticamente?
17. Perfil socioeconômico (idade, escolaridade, histórico laboral) entra sempre na
    análise, ou só quando a tese for incapacidade social?

BPC/LOAS E PENSÃO POR MORTE
18. No BPC, monto a composição do grupo familiar e a renda per capita sempre que
    os dados permitirem, ou isso fica só com a ferramenta de cálculo?
19. Gastos com saúde e vulnerabilidade: levanto sempre como tese subsidiária de
    afastamento do critério de 1/4, ou só quando você pedir?
20. Em pensão com dependentes concorrentes, mapeio todos os possíveis dependentes
    mesmo sem certeza de habilitação?
21. Em união estável controvertida, qual o conjunto mínimo de prova que você
    considera suficiente para sustentar a tese?

APOSENTADORIAS E REGRAS DE TRANSIÇÃO
22. Calculo todas as regras de transição aplicáveis, ou só a que você já apontou
    como mais vantajosa?
23. Em atividade especial, exijo PPP e LTCAT antes de qualquer análise, ou
    trabalho com o que houver marcando a lacuna?
24. EPI eficaz: trato como controvérsia aberta a enfrentar sempre, ou só quando o
    PPP afirmar eficácia?
25. Prefere que eu compare o resultado das regras em tabela, ou em texto corrido?

REVISÃO DE PEÇAS E PJe
26. Na revisão, começo pelas fragilidades processuais (competência, prazo, tutela)
    antes do mérito, ou o inverso?
27. Changelog linha a linha, ou resumo das mudanças por seção?
28. Tem padrão fixo de endereçamento e qualificação, ou você informa a cada peça?
29. Incluo pedido subsidiário por padrão em inicial complexa, ou só quando pedir?

PRAZOS, CÁLCULOS E JURISPRUDÊNCIA
30. Alerto sobre prescrição quinquenal sempre, mesmo sem ser perguntado?
31. Tem ferramenta própria de cálculo que eu deva sempre indicar em vez de
    estimar?
32. Tem tribunal ou turma que você acompanha mais de perto e cuja jurisprudência
    eu deva priorizar?
33. Trago a linha desfavorável junto com a favorável sempre, ou só quando você
    perguntar pela tese contrária?

SIGILO, FERRAMENTAS E CONTEÚDO
34. Tem serviço externo pré-autorizado, ou toda saída externa exige autorização a
    cada vez?
35. Tem acervo próprio de jurisprudência ou modelos que eu deva citar como fonte
    preferencial?
36. Se eu pedir conteúdo educativo (post, artigo), tem tom de voz e público-alvo
    padrão?

Ao final de qualquer etapa, mostre o texto completo do configuracao-barkoski.md
resultante antes de salvar, para eu confirmar.
```

### 📚 Caminho alternativo: aprender pelas suas próprias peças

Se você não tem paciência para a entrevista — ou se acha difícil descrever o próprio estilo em abstrato — existe um caminho melhor: deixar o Claude ler peças que **você já escreveu** e extrair o padrão de lá.

Costuma ser mais fiel que a autodeclaração. A maioria das pessoas descreve mal o próprio jeito de redigir, mas o jeito está visível no trabalho pronto.

**Antes de começar, sobre sigilo:** use peça já protocolada ou com os dados do cliente removidos. Nome, CPF, NB e número de processo não interessam para o que se quer extrair — o objeto é a forma, não o caso. Mesmo quando as ferramentas são executadas localmente, o conteúdo necessário à interação com o modelo pode ser enviado ao provedor configurado; retenção e uso dependem do produto, da conta e das configurações vigentes. Verifique essas condições e anonimizar antes continua sendo o hábito certo. Consulte a [documentação de uso de dados do Claude Code](https://code.claude.com/docs/en/data-usage) e a documentação do provedor utilizado.

**Escolha das peças:** 3 ou 4, de tipos e matérias diferentes (uma inicial, um recurso, uma impugnação; se possível, matérias distintas). Duas peças do mesmo tipo produzem padrões frágeis — o que parece estilo do escritório pode ser exigência daquele tipo de caso.

```
Você vai aprender o estilo de trabalho do meu escritório lendo peças que eu mesmo
escrevi, em vez de eu responder um questionário.

Sigilo: as peças podem conter dados de cliente. Não repita nome, CPF, NB ou número
de processo em nenhuma saída sua — o que interessa é a forma, não o caso. Não use
ferramentas externas adicionais nem compartilhe o material com terceiros além do
provedor do modelo previamente autorizado; prefira peças anonimizadas.

PASSO 1 — Leia as peças que eu indicar.

PASSO 2 — Extraia SOMENTE padrões observáveis e repetidos. Para cada um, diga em
quantas peças ele aparece:
- Presente em TODAS: registre como padrão.
- Presente em apenas UMA: registre como "observado uma vez" e me pergunte se é
  regra do escritório ou circunstância daquele caso.
- Assunto que não aparece em nenhuma: NÃO invente preferência. Liste ao final em
  "não foi possível inferir".

Observe pelo menos: endereçamento e qualificação; como nomeia as partes; estrutura
e ordem das seções; densidade da fundamentação (enxuta ou desenvolvida, uso de
doutrina); se usa pedido subsidiário; postura quanto a tutela de urgência; se lista
documentos; que tribunais cita; como trata valor da causa; e qualquer recorrência
que eu não tenha listado.

PASSO 3 — Antes de concluir, avalie o viés da amostra: se as peças forem todas do
mesmo rito, da mesma matéria ou da mesma fase, avise que parte dos padrões pode ser
exigência daquele tipo de caso, não política do escritório. Diga quais itens estão
nessa situação.

PASSO 4 — Me mostre o resultado em quatro blocos: PADRÕES CONFIRMADOS, OBSERVADO UMA
VEZ (a confirmar), NÃO FOI POSSÍVEL INFERIR e RESSALVA DE AMOSTRA.

PASSO 5 — Só depois da minha confirmação, grave os padrões confirmados como
subseções "## Preferências — ..." em
skills/advocacia-previdenciaria-barkoski/references/configuracao-barkoski.md.
Não edite nenhum outro arquivo.
```

Os dois caminhos se somam: dá para extrair das peças primeiro e depois rodar a entrevista só nos pontos que ficaram em "não foi possível inferir".

### ✅ Depois de personalizar

Peça ao Claude para rodar um caso real (ou um caso de teste sem dados sensíveis) e confira se as preferências pegaram. Se algo ficou fora do esperado, é só continuar a conversa — o arquivo é texto, e ajustar é conversar.

Se quiser voltar ao padrão, apague as subseções `## Preferências — ...` que a entrevista criou; o resto do arquivo é a configuração original.

