# O que muda

<!-- Uma frase. O que a skill passa a fazer, ou deixa de fazer. -->

# Por quê

<!-- O motivo concreto. Se veio de um caso real, descreva sem identificar ninguém: benefício, fase e o que a skill errou ou deixou passar. -->

# Como testei

<!-- O que você rodou e o que verificou à mão. Diga também o que NÃO testou. -->

---

## Antes de pedir revisão

- [ ] **Nenhum dado de caso real** neste PR: código, exemplos, testes, capturas ou mensagens de commit. Sem nome, CPF, NB, número de processo, endereço, dado clínico ou trecho de autos.
- [ ] Uma mudança por PR — correção de texto e mudança de comportamento não vão juntas.
- [ ] Rótulo técnico em caixa alta e sem acento; o resto em português com acentuação.
- [ ] Não afrouxei trava existente. Se afrouxei, há issue discutindo antes.
- [ ] Nada aqui promete resultado, êxito ou probabilidade de ganho.

## Se mexi em conjunto fechado

Famílias documentais, graus de comprovação, situação de requisito, qualidade de leitura, estado de norma ou decisões operacionais. Marque tudo que atualizou:

- [ ] `SKILL.md`
- [ ] `scripts/previdenciario_tool.py` — constantes `VALID_*`
- [ ] `references/identificacao-documental.md` — schema e conjuntos
- [ ] `references/validacao.md`
- [ ] `README.md` — contagens e descrições
- [ ] Não se aplica

> Mudar um sem os outros faz o validador recusar entrada válida.

## Testes

- [ ] `python -m unittest discover -s tests -v` passa
- [ ] `python scripts/previdenciario_tool.py validate examples/caso-ficticio.json` passa
- [ ] Trava nova tem teste que a protege — quebra a regra de propósito e exige recusa
- [ ] Não se aplica: mudança só de texto, sem efeito no validador
