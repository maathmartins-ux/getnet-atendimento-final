# Modos de falha (eval ao vivo)

Gerado por `python -m evals.failure_modes` a partir de `evals/results/live_*.json`. Cada falha conta uma vez, pela primeira checagem que falhou. Para cada modo: o que fazer é decisão humana; o que foi feito fica no commit que cita o modo.

Fora da conta: `heldout` (111 execuções), o conjunto cego: ler as falhas dele para corrigir o motor o contamina. A medida dele fica nos blocos ao vivo, do juiz e humano de `docs/RESULTS.md`.

6 falhas em 229 execuções (2.6%).

| modo | falhas | casos distintos | splits |
|---|---:|---:|---|
| `handoff` | 3 | 3 | replan (3) |
| `intent` | 2 | 2 | partial (1), replan (1) |
| `claims` | 1 | 1 | official-var (1) |

## `handoff`

Casos que mais falham: `replan-02` (1x), `replan-04` (1x), `replan-07` (1x)

- exemplo `replan-02`: “Does Getnet offer a card machine that accepts bitcoin payments?”
- esperado: intent `knowledge`; obtido: `knowledge`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: No, I found no Getnet card machine that is listed as accepting bitcoin or other cryptocurrency. The sources only list these accepted payments: - **Card brands:** MasterCard, Visa, Elo, Amex and Hipercard for individuals. Businesses also get Alelo, Pluxee, Tic…

## `intent`

Casos que mais falham: `q-partial-02` (1x), `replan-08` (1x)

- exemplo `q-partial-02`: “What is the exact monthly fee of the Get Smart and its battery life in hours?”
- esperado: intent `knowledge`; obtido: `multi`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: There is no single exact monthly fee for the Get Smart. The rental depends on your sales volume, and the sources don't give battery life in hours. **Monthly fee** - The rental is R$50,00 for sales from R$10 mil/month and R$10,00 for sales from R$30 mil/month.…

## `claims`

Casos que mais falham: `q-offvar-01-en` (1x)

- exemplo `q-offvar-01-en`: “Compare the two terminals for me: Get Smart versus Get Clássica, what sets them apart?”
- esperado: intent `knowledge`; obtido: `knowledge`; rota ['router', 'faq']; ferramentas []
- números sem base: nenhum
- resposta: The Get Smart is a smart terminal with built-in management features, and the Get Clássica is a simpler option for both CPF and CNPJ. **Get Smart** - You can control stock, take orders, close tabs, load a menu and issue invoices on the terminal [1]. - It can r…
