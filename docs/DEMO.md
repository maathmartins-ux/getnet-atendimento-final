# Respostas reais — split `official`

Geradas de `evals/results/live_official.json` (provedor `anthropic`, status `complete`, gasto US$ 0.66); respostas medidas no commit `1a38cbd` (2026-11-05T23:05:21Z), página gerada no commit `2244707` em 05/11/2026 23:19 UTC. Nada aqui foi escrito à mão: é a saída do `POST /chat` com o LLM ligado, 1ª rodada de cada caso.

Estabilidade em 3 rodadas: pass@1 1.0, pass^3 1.0; instáveis: nenhum.

Em cada passo, **decidido por** diz quem pôs o agente no turno: o supervisor LLM (tool call); o plano do router (o router LLM, ou a regra que o substitui: seguimento herdado, guarda da própria empresa, queda do LLM), quando o supervisor LLM não foi consultado (rodado pelo atalho de 1 passo ou pelo motor de tabela); o código, com a regra entre parênteses (`supervisor.CODE_WHY`); ou a operadora que respondeu o caso. "não registrado" = passo gravado sem o campo `decided_by`.

| caso | intenção | rota | ferramentas | handoff | veredito automático |
|---|---|---|---|---|---|
| `official-01` | knowledge | router → faq | — | não | OK |
| `official-02` | general | router → general | weather_forecast | não | OK |
| `official-03` | support | router → records | get_settlements | não | OK |
| `official-04` | knowledge | router → faq | — | não | OK |
| `official-05` | troubleshoot | router → records → faq | get_terminals | não | OK |
| `official-06` | knowledge | router → faq | — | não | OK |
| `official-07` | general | router → general | currency_rate | não | OK |
| `official-08` | troubleshoot | router → records → faq | get_transactions, get_terminals | não | OK |
| `official-09` | knowledge | router → faq | — | não | OK |
| `official-10` | knowledge | router → faq | — | não | OK |

## official-01

**Pergunta:** What's the difference between the Get Clássica and the Get Smart?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0399 · **latência:** 23.7 s

**Resposta:**

> The Get Smart is an Android smart machine that does more on the device, and it needs higher sales to be free: R$60,000 per month, against R$10,000 for the Get Clássica [1].
>
> **Get Clássica**
> - The page says it comes with a free machine*, a free account and card, and receipt in 2 days. It is valid for CPF and CNPJ. The page is from 2025, so it may be outdated [1].
> - Rates: debit 1.69%, credit 1x 3.79%, 2x 7.98%, 3x 8.47%, 4x 8.96%, 5x 9.45% [1].
>
> **Get Smart**
> - On the device you can control stock, place orders, close the bill, load the menu and issue invoices. It can be integrated with your business system [2].
> - It replaces the computer and fiscal printer [2].
> - Because it runs Android, it can do things like exchange messages between kitchen and floor. Whether it prints the NF-e depends on the app you choose, and most apps issue it [2].
> - It can be used as a TEF solution [3] and supports payment split for commission or tips [3].
> - App subscriptions are charged by the app developers. Getnet charges rent and administrative fees [4].
>
> Both are covered by the rent discount offer [5].
>
> I didn't find the Get Smart's own rates or rent. A human agent can give you those if you'd like.

**Passos:**

1. **faq** · ok · 13792 ms · decidido por: supervisor LLM (tool call)

**Fontes citadas:** [1] <https://site.getnet.com.br/maquininha/get-classica/>; [2] <https://site.getnet.com.br/duvidas/get-smart/>; [3] <https://site.getnet.com.br/maquininha/get-smart/>; [4] <https://site.getnet.com.br/duvidas/taxas/>; [5] <https://site.getnet.com.br/get-tap/>
**Checagens:** 9/9 passam · **juiz:** fundamentada · **desfecho:** completa

## official-02

**Pergunta:** What's the weather forecast in Porto Alegre tomorrow?

**Intenção:** general (esperada general) · **rota:** router → general · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0132 · **latência:** 9.2 s

**Resposta:**

> Tomorrow (2026-11-06) in Porto Alegre, the forecast is a low of 16 °C, a high of 28 °C and up to a 10% chance of rain. Source: wttr.in.

**Passos:**

1. **general** · ok · 5256 ms · decidido por: supervisor LLM (tool call)
   - `weather_forecast` {"city": "Porto Alegre", "day": "amanhã"} → ok

**Dados ao vivo de:** <https://wttr.in/>
**Checagens:** 10/10 passam · **juiz:** fundamentada · **desfecho:** completa

## official-03

**Pergunta:** When will the money from yesterday's sales be deposited?

**Intenção:** support (esperada support) · **rota:** router → records · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0224 · **latência:** 7.9 s

**Resposta:**

> Yesterday's sales (04/11/2026) totaled R$ 695,50 across 3 sales. R$ 215,50 has been deposited and R$ 480,00 is still to be deposited.
>
> - **Pix:** R$ 120,00, deposited on 04/11/2026.
> - **Debit:** R$ 95,50, deposited on 05/11/2026.
> - **Credit (30-day plan):** R$ 480,00, scheduled for 04/12/2026.

**Passos:**

1. **records** · ok · 3034 ms · decidido por: supervisor LLM (tool call)
   - `get_settlements` {"period": "yesterday"} → ok · `{"ok": true, "data": {"period": "yesterday", "from": "2026-11-04", "to": "2026-11-04", "today": "2026-11-05", "schedule": [{"method": "pix"…`

**Checagens:** 10/10 passam · **juiz:** fundamentada · **desfecho:** completa

## official-04

**Pergunta:** Do I need a bank account to receive my sales via Pix?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0396 · **latência:** 18.2 s

**Resposta:**

> Yes. To receive Pix sales you need a bank domicile and an active Pix key [1]. When you sign up for Pix in the Getnet Minha Conta portal or the Getnet app, you enter the same key you registered at your bank domicile, and that is where the Pix arrives [2].
>
> The eligibility criteria are:
> - a compatible capture method (terminal, TEF or e-commerce);
> - a Santander bank domicile with an active Pix key;
> - registration with an individual (PF) legal representative [1].
>
> **If you don't have an account:** Get Conta is Getnet's free digital account. It gives you a bank number, branch and account number, and you can receive your sales settlements and sell via Pix with it [3].
>
> **If your Pix key is at another institution:**
> - You can delete it there and register it at Get Conta.
> - Or you can request portability in the Getnet Brasil app. You must confirm it within 7 days at the other institution, or the request is cancelled.
> - Only CPF/CNPJ, e-mail and mobile phone keys can be ported [4].
>
> I couldn't find whether a Get Conta counts as the Santander bank domicile required for Pix enablement. A human agent can confirm that if you'd like.

**Passos:**

1. **faq** · ok · 10148 ms · decidido por: supervisor LLM (tool call)

**Fontes citadas:** [1] <https://site.getnet.com.br/duvidas/pix/>; [2] <https://site.getnet.com.br/duvidas/>; [3] <https://site.getnet.com.br/duvidas/get-conta/>; [4] <https://site.getnet.com.br/duvidas/pix-mais-respostas/>
**Checagens:** 9/9 passam · **juiz:** fundamentada · **desfecho:** completa

## official-05

**Pergunta:** My card machine won't connect to the internet, what should I do?

**Intenção:** troubleshoot (esperada troubleshoot) · **rota:** router → records → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0465 · **latência:** 22.3 s

**Resposta:**

> Your machine T1988B (Get Clássica) is the one that's offline. It connects by chip, has no signal, and has been offline for 5 hours. Its last contact was 05/11/2026 at 15:03. Your other machine, T1988A (Get Smart), is online on Wi-Fi with a good signal.
>
> Because T1988B uses a chip, these are the chip steps from the manual:
> - With the machine off, open the back cover. Insert the chip in the slot marked SIM1 or SIM2, metal side down. Close the cover, turn the machine on and wait for the data network connection [1].
> - When it shows a connected network (2G or 3G), it is ready to use [1].
> - Run a communication test. Press the function button (F, # or your machine's own), choose option 2 (maintenance), then option 1 (communication test) [1].
>
> If you see error ADQ 1-87 during a sale, follow these steps [2]:
> 1. Confirm the chip is properly inserted.
> 2. Press the Function key, enter 25 and wait for the green screen.
> 3. Enter the merchant password, select Function 46 and wait for the green screen.
> 4. Select Function 90 and wait for the green screen again.
> 5. Make a test sale.
>
> I can also propose a support ticket for T1988B with the reason "no signal". Nothing is opened until you confirm, and an unconfirmed proposal expires after 15 minutes. Do you want me to propose it?

**Passos:**

1. **records** · ok · 3316 ms · decidido por: supervisor LLM (tool call)
   - `get_terminals` {} → ok · `{"ok": true, "data": {"terminals": [{"terminal_id": "T1988A", "model": "Get Smart", "status": "online", "connection": "wi-fi", "signal": "b…`
2. **faq** · ok · 11074 ms · decidido por: supervisor LLM (tool call)

**Fontes citadas:** [1] <https://site.getnet.com.br/duvidas/>; [2] <https://site.getnet.com.br/get-ajuda-erros-maquininha/erro-adq-1-87/>
**Checagens:** 10/10 passam · **juiz:** fundamentada · **desfecho:** completa

## official-06

**Pergunta:** How does receivables advance (antecipação) work with Getnet?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0404 · **latência:** 25.9 s

**Resposta:**

> Receivables advance lets you receive your card sales earlier than the normal schedule. Debit sales are available the next day. For credit, you can receive everything in 2 days, in 30 days, or month by month by installment [1].
>
> - **Advance window:** you can advance a sale from D+1 (one business day after the sale) up to D-3 (three business days before the schedule settles into your account) [1].
> - **Rules:** since June 7, 2021, Central Bank Resolution 4.734 and Circular 3.952 let merchants use card receivables in credit operations with authorized institutions. The acquirer registers the receivables with a registry so they become a negotiable financial title [1].
> - **Loan collateral (gravame):** if you take a loan, the gravame is your guarantee to Getnet. Sales made at Getnet and at other acquirers are then received in your Get Conta, up to the loan's outstanding balance [1].
> - **Automatic Advance:** this is a condition for the exemption on the "Receba Conforme suas Vendas" plan. It involves credit approval, and Getnet evaluates each contract individually [2].
> - **Limits:** sales from card brands you enabled with their own operator can't be advanced through Getnet. Advance of e-commerce sales is blocked for 6 months, while physical sales can be advanced normally [1][3].
> - **Fees:** the sources show no advance rate. They say you pay the plan fee plus a card fee that depends on the number of installments and on how many days earlier you want the money [3].
>
> I can propose an advance of credit receivables for an amount in reais. It only runs after you confirm and a human agent approves it. For the exact rates or a step-by-step process, I can also pass you to a human agent.

**Passos:**

1. **faq** · ok · 14260 ms · decidido por: supervisor LLM (tool call)

**Fontes citadas:** [1] <https://site.getnet.com.br/duvidas/antecipacao-de-vendas/>; [2] <https://site.getnet.com.br/duvidas/>; [3] <https://site.getnet.com.br/duvidas/link-de-pagamento/>
**Checagens:** 9/9 passam · **juiz:** fundamentada · **desfecho:** completa

## official-07

**Pergunta:** What's the euro exchange rate today?

**Intenção:** general (esperada general) · **rota:** router → general · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0144 · **latência:** 10.3 s

**Resposta:**

> The euro is R$ 6.1311 at buy and R$ 6.1323 at sell. That's from the Banco Central do Brasil (PTAX) closing bulletin for 05/11/2026. Rounded, both are R$ 6.13.
>
> Source: https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes

**Passos:**

1. **general** · ok · 3716 ms · decidido por: supervisor LLM (tool call)
   - `currency_rate` {"currency": "EUR", "date": "2026-11-05"} → ok

**Dados ao vivo de:** <https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes>
**Checagens:** 10/10 passam · **juiz:** fundamentada · **desfecho:** completa

## official-08

**Pergunta:** My card machine is showing a transaction decline error.

**Intenção:** troubleshoot (esperada troubleshoot) · **rota:** router → records → faq · **replanos:** ['records:need->faq (venda recusada: o que fazer vem do manual de recusas; maquininha offline: se a p)'] · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0267 · **latência:** 16.4 s

**Resposta:**

> The declines come from the card issuer, not from your machine. Your terminal T1988A is online on Wi-Fi with good signal.
>
> In the last 7 days there were 2 declines today (11/05/2026) on T1988A, totaling R$ 285,00:
> - **TX1007**, 10:05, credit, R$ 210,00. Code 51 means insufficient balance or credit limit. The buyer should contact the card issuer or pay with another card or Pix.
> - **TX1008**, 10:40, debit, R$ 75,00. Code 05 means not authorized by the issuer. The buyer should contact the issuing bank. Retrying will not help.
>
> Your other terminal, T1988B, is offline with no signal. It has been offline for 5 hours, since its last contact at 15:03. It has no declines.
>
> I can propose a support ticket for T1988B for "no signal". Nothing happens until you confirm the proposal. Do you want me to do that?

**Passos:**

1. **records** · ok · 4466 ms · decidido por: supervisor LLM (tool call)
   - `get_transactions` {"period": "last_7_days"} → ok · `{"ok": true, "data": {"period": "last_7_days", "from": "2026-10-30", "to": "2026-11-05", "today": "2026-11-05", "sales": [{"transaction_id"…`
   - `get_terminals` {} → ok · `{"ok": true, "data": {"terminals": [{"terminal_id": "T1988A", "model": "Get Smart", "status": "online", "connection": "wi-fi", "signal": "b…`
2. **faq** · insufficient · motivo `no_source` · 3040 ms · decidido por: supervisor LLM (tool call)

**Checagens:** 10/10 passam · **juiz:** fundamentada · **desfecho:** completa

## official-09

**Pergunta:** How many installments can I split a sale into with the crediário?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0158 · **latência:** 10.1 s

**Resposta:**

> You can split a sale into up to 48 installments with the Crediário, on a credit card [1]. The maximum number and the interest rate depend on the card issuer, because each issuer sets its own installment limit [1][2].
>
> To see the interest for your customer, run a simulation on the card machine. Insert the card, enter the amount, then choose credit > crediário. You can print the receipt if the machine has paper. The simulation is for reference only, and the issuer approves the transaction [2].

**Passos:**

1. **faq** · ok · 3001 ms · decidido por: supervisor LLM (tool call)

**Fontes citadas:** [1] <https://site.getnet.com.br/crediario/>; [2] <https://site.getnet.com.br/duvidas/crediario/>
**Checagens:** 9/9 passam · **juiz:** fundamentada · **desfecho:** completa

## official-10

**Pergunta:** Can I sell through WhatsApp using the Payment Link?

**Intenção:** knowledge (esperada knowledge) · **rota:** router → faq · **replanos:** nenhum · **caminho:** supervisor LLM (laço de tool use) · **custo:** US$ 0.0145 · **latência:** 7.8 s

**Resposta:**

> Yes, you can sell through WhatsApp with the Payment Link. You send the link to your customer by WhatsApp, social media, email or SMS. The customer clicks the link, chooses a payment method and completes the purchase [1]. Getnet's Payment Link page also says you can sell from wherever you are through WhatsApp or your social network [2].

**Passos:**

1. **faq** · ok · 2698 ms · decidido por: supervisor LLM (tool call)

**Fontes citadas:** [1] <https://site.getnet.com.br/duvidas/link-de-pagamento/>; [2] <https://site.getnet.com.br/link-de-pagamento/>
**Checagens:** 9/9 passam · **juiz:** fundamentada · **desfecho:** completa
