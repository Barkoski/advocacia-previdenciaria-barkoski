# Exemplos e regressao do validador

Dois casos ficticios. Nenhum dado real, nenhum cliente.

| Arquivo | Serve para | Resultado esperado |
|---|---|---|
| `caso-ficticio.json` | referencia de formato de [saida-json.md](../skills/advocacia-previdenciaria-barkoski/references/saida-json.md) e fixture de regressao | passa: `sem erros`, com 1 aviso deliberado (`D5: titular desconhecido`) |
| `caso-invalido.json` | fixture negativo: guarda as travas do validador | falha com codigo 1; quantidade de achados pode aumentar com novas verificacoes |

## Rodar a regressao

```bash
python skills/advocacia-previdenciaria-barkoski/scripts/previdenciario_tool.py validate examples/caso-ficticio.json && python skills/advocacia-previdenciaria-barkoski/scripts/previdenciario_tool.py validate examples/caso-invalido.json; echo "o segundo comando DEVE falhar"
```

O primeiro tem de sair com codigo 0; o segundo, com codigo 1. Se o `caso-invalido.json` passar, o validador perdeu uma trava — corrigir o validador, nao o exemplo.

## O que o caso ficticio exercita

Ele foi montado para cobrir as situacoes que o validador precisa reconhecer, e nao para ser um caso bonito:

- documento nao lido (`D5`) que fica fora da tabela de provas e aparece nos blocos de pendencia;
- documento de terceiro (`D3`, em nome do conjuge), com `conferir: SIM`;
- documento com `OCR DUVIDOSO` (`D4`);
- fato `INFERENCIA` com `base_inferencia` declarada (`F4`);
- fato `ALEGACAO` sem documento (`F5`);
- prova contraria a propria tese (`D2`, vinculo urbano dentro do periodo rural alegado);
- requisito nao analisado, com situacao `?` (`R2`);
- marco com data aproximada e fonte de natureza alegada; aproximacao isolada nao define o grau;
- prazo incompleto, obrigatoriamente `PRAZO PENDENTE DE CONFERENCIA HUMANA`;
- norma citada de memoria e norma vinda do acervo, cada uma com seu estado;
- decisao operacional com decisao paralela distinta.

## Violacoes plantadas no caso invalido

Estao listadas dentro do proprio arquivo, em `_violacoes_esperadas`. Ao acrescentar uma trava nova ao validador, plantar aqui a violacao correspondente e registrar na lista.
