# Modos de falha (eval ao vivo)

Gerado por `python -m evals.failure_modes` a partir de `evals/results/live_*.json`. Cada falha conta uma vez, pela primeira checagem que falhou. Para cada modo: o que fazer é decisão humana; o que foi feito fica no commit que cita o modo.

Fora da conta: `heldout` (111 execuções), o conjunto cego: ler as falhas dele para corrigir o motor o contamina. A medida dele fica nos blocos ao vivo, do juiz e humano de `docs/RESULTS.md`.

8 falhas em 229 execuções (3.5%).

| modo | falhas | casos distintos | splits |
|---|---:|---:|---|
| `handoff` | 3 | 3 | replan (3) |
| `claims` | 2 | 2 | memory (1), official-var (1) |
| `intent` | 2 | 2 | partial (1), replan (1) |
| `memory` | 1 | 1 | memory (1) |

## `handoff`

Casos que mais falham: `replan-02` (1x), `replan-04` (1x), `replan-07` (1x)

- exemplo `replan-02`: “Does Getnet offer a card machine that accepts bitcoin payments?”
- esperado: intent `knowledge`; obtido: `knowledge`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: No, I found no Getnet card machine that is listed as accepting bitcoin or other cryptocurrency. The sources only list these accepted payments: - **Card brands:** MasterCard, Visa, Elo, Amex and Hipercard for individuals. Businesses also get Alelo, Pluxee, Tic…

## `claims`

Casos que mais falham: `memory-03` (1x), `q-offvar-01-en` (1x)

- exemplo `memory-03`: “E a outra maquininha, a Get Clássica, como é?”
- esperado: intent `knowledge`; obtido: `knowledge`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: A Get Clássica é uma maquininha de cartão (POS 3G + Wi-Fi) para CPF ou CNPJ, com conta e cartão grátis, recebimento em 2 dias e taxa única nas principais bandeiras. Ela é recomendada para quem quer vender mais sem pagar aluguel [1]. - **Máquina grátis:** a pá…

## `intent`

Casos que mais falham: `q-partial-02` (1x), `replan-08` (1x)

- exemplo `q-partial-02`: “What is the exact monthly fee of the Get Smart and its battery life in hours?”
- esperado: intent `knowledge`; obtido: `multi`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: There is no single exact monthly fee for the Get Smart. The rental depends on your sales volume, and the sources don't give battery life in hours. **Monthly fee** - The rental is R$50,00 for sales from R$10 mil/month and R$10,00 for sales from R$30 mil/month.…

## `memory`

Casos que mais falham: `memory-02` (1x)

- exemplo `memory-02`: “And the other one, the Get Clássica?”
- esperado: intent `knowledge`; obtido: `knowledge`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: It depends on your sales. No fixed monthly fee is stated for the Get Clássica, and it can be free. - The 2026 page says the Get Clássica is free ("máquina grátis") with sales above R$20 mil per month [1]. - Voucher (VA/VR) and Crediário sales don't count towa…
