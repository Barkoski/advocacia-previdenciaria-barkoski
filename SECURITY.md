# Política de segurança

## O que conta como vulnerabilidade aqui

Este projeto é uma skill jurídica com um validador. Não há servidor, autenticação nem armazenamento de dados. O risco não está em execução remota — está em **fazer um advogado confiar em algo que não se sustenta** ou em **vazar dado de cliente**.

Trate como vulnerabilidade e reporte em privado:

- **Vazamento de sigilo.** Qualquer instrução, exemplo ou caminho do código que leve a enviar dado de caso para fora sem autorização expressa: busca web com identificador, conector, serviço de terceiro, telemetria, nome de arquivo com dado pessoal.
- **Falso verde do validador.** Caso que viola uma trava e mesmo assim passa em `validate`. É o pior defeito possível aqui: o validador existe para recusar, e um falso verde induz confiança em conteúdo não conferido.
- **Trava contornável por conteúdo dos autos.** Texto embutido em PDF, petição ou e-mail que faça a skill obedecer a instrução em vez de tratá-lo como prova. A trava 10 do `SKILL.md` existe para isso; furo nela é vulnerabilidade.
- **Indução a afirmação sem lastro.** Redação de módulo que faça a skill afirmar fato, página, norma ou prazo sem fonte, ou promover grau de comprovação silenciosamente.
- **Dado real no repositório.** Se encontrar dado de caso real em qualquer arquivo ou no histórico, reporte em privado, não abra issue pública.

Bug comum de código — mensagem de erro confusa, caso não coberto, incompatibilidade de versão — é issue normal, não precisa de canal privado.

## Como reportar

Use o **relato privado de vulnerabilidade do GitHub**, na aba *Security* deste repositório, em *Report a vulnerability*. Fica visível apenas para o mantenedor.

Não abra issue pública para os itens da lista acima.

**Não inclua dados de caso real no relato.** Se precisar demonstrar o problema, descreva o padrão ou monte um exemplo fictício. Um relato de vazamento de sigilo que traga dado de cliente reproduz o próprio problema que denuncia.

## O que esperar

Este é um projeto mantido por uma pessoa, ao lado da advocacia. Não há acordo de nível de serviço. O compromisso realista:

- Confirmação de recebimento assim que possível.
- Resposta dizendo se foi reproduzido e o que será feito.
- Crédito no commit da correção, se você quiser.

## Versões

Correções entram na versão corrente publicada no catálogo `barkoski-skills`. Não há manutenção de versões anteriores. Para atualizar:

```bash
/plugin marketplace update barkoski-skills
```

## O que o validador não protege

Vale repetir, porque é limite de projeto e não defeito a corrigir: o validador verifica estrutura, referências e coerência interna. Ele **não** abre página, não confere documento, não checa vigência de norma e não avalia se a tese procede. Resultado sem erro não significa que os fatos são verdadeiros. A conferência na fonte continua sendo humana.
