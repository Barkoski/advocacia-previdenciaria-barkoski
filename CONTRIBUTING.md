# Como contribuir

Obrigado pelo interesse. Este repositório é uma skill: texto e instruções, mais um validador em Python. Não é aplicação, não tem servidor e não guarda dados.

## Regra nº 1 — nunca dados reais

**Não inclua dados de caso real em lugar nenhum: issue, pull request, exemplo, teste, captura de tela ou mensagem de commit.**

Isso vale para nome de parte, CPF, NB, número de processo, endereço, data de nascimento, dado clínico, laudo, CNIS, CTPS e trecho de autos. Vale também para número de processo que corre em segredo de justiça e para o que parece inofensivo isolado mas identifica alguém em conjunto.

Se precisar demonstrar um comportamento, use dados inventados. O arquivo [`examples/caso-ficticio.json`](examples/caso-ficticio.json) existe para isso e é inteiramente fictício.

Contribuição que traga dado real será fechada sem merge, e o histórico terá de ser reescrito. É mais fácil não enviar.

## O que é uma boa contribuição

A skill é usada para trabalhar com processo de gente real. Mudança aqui muda o que um advogado entrega. Por isso:

- **Regra nova precisa de motivo concreto.** De preferência um caso real que a expôs, descrito sem identificar ninguém. "Achei que ficaria melhor" não sustenta uma trava.
- **Módulo é carregado sob demanda.** Texto acrescentado custa contexto em toda análise que carregar aquele módulo. Prefira precisão a volume.
- **Não afrouxe trava sem discussão.** As travas existem para impedir invenção de fato, página, norma e prazo. Se uma atrapalha, abra issue antes do PR.
- **Nada que prometa resultado.** A skill não afirma êxito, não estima probabilidade de ganho e não substitui o advogado.

## Convenções de escrita

- Rótulo técnico em caixa alta e sem acento: `FATO COMPROVADO`, `DILIGENCIAR ANTES`, `PRAZO PENDENTE DE CONFERENCIA HUMANA`.
- Todo o restante em português correto, com acentuação.
- Célula de tabela vazia é erro: `—` para não aplicável, `?` para desconhecido.
- Módulos em `references/` são curtos e específicos. Se um assunto novo não couber nos existentes, proponha módulo próprio em vez de inflar outro.

## Conjuntos fechados: mude em todos os lugares

Alguns valores são verificados por código. Se você alterar um conjunto, atualize **todos** estes pontos, ou o validador passará a recusar entrada válida:

| Onde | O quê |
|---|---|
| `skills/advocacia-previdenciaria-barkoski/SKILL.md` | decisões operacionais, entrega padrão |
| `skills/advocacia-previdenciaria-barkoski/scripts/previdenciario_tool.py` | as constantes `VALID_*` |
| `skills/advocacia-previdenciaria-barkoski/references/identificacao-documental.md` | schema JSON e conjuntos fechados |
| `skills/advocacia-previdenciaria-barkoski/references/validacao.md` | o que o validador recusa |
| `README.md` | contagens e descrições |

Vale para famílias documentais, graus de comprovação, situação de requisito, qualidade de leitura, estado de norma e decisões operacionais.

## Testes

O validador só depende da biblioteca padrão. Antes de abrir o PR:

```bash
python -m unittest discover -s tests -v
```

```bash
python skills/advocacia-previdenciaria-barkoski/scripts/previdenciario_tool.py validate examples/caso-ficticio.json
```

O CI roda os dois em Python 3.9 e 3.13. **Trava nova precisa de teste que a proteja** — um teste que quebre a regra deliberadamente e exija recusa. É o teste que define a trava, não a frase em prosa.

## Commits e PRs

- Uma mudança por PR. Correção de texto e mudança de comportamento não vão juntas.
- Mensagem de commit explica **por que**, não só o quê.
- Se a mudança veio de um caso real, diga isso sem identificar o caso.
- Descreva no PR o que você testou e o que não testou.

## Licença

Ao contribuir, você concorda em licenciar sua contribuição sob a [licença MIT](LICENSE) do projeto.
