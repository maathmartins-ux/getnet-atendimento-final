# Resultados completos

Tudo aqui é gerado por `scripts/fill_readme.py` a partir de `evals/results/` commitado. O resumo com metas está no
§0 do [README](../README.md).

## Leitura dos números

<!-- reading:begin -->
- **Na referência (11 de 16):** Juiz: respostas oficiais úteis (helpful) 1.00; Juiz: respostas oficiais fundamentadas 1.00; Oficiais: números com base na evidência 100.0%; Oficiais: todas as checagens por regra em todas as rodadas (sem o juiz) 1.00; Memória ao vivo: pass@1 0.96 e mais 6.
- **Abaixo:** Oficiais resolvidas por completo (sem humano + todo fato + fonte + juiz: fundamentada; parcial fora) 0.87 (referência 0.90) — resposta parcial (a fonte cobre só parte da pergunta) em `official-04`, `official-05`.
- **Abaixo:** Oficiais resolvidas por completo: pass^k (todas as rodadas, com o juiz) 0.80 (referência 0.90) — a mesma causa da linha de cima, em todas as rodadas.
- **Abaixo:** Juiz validado contra rótulos de pessoas (1 = sim, regra fixada antes) 0 (referência 1) — falta rótulos de pessoas (campo labeler: "human:<nome>"); estes vêm da SPEC ou de modelo.
- **Parcial, fora da manchete:** 13% das execuções oficiais resolveram só parte da pergunta e disseram o que a fonte não cobre; contam à parte, nunca como resolvidas.
- **Ao vivo:** 13 splits, 340 execuções, 317 sem nenhuma checagem falhando; os mais fracos pela checagem principal: `partial` (intenção 80%), `heldout` (intenção 89.2%).
- **Juiz LLM:** oficiais fundamentadas 1.00 e úteis 1.00; ainda não validado contra pessoas: serve para comparar commits, não como medida absoluta.
- **Gate offline (CI):** intenção 100.0% nos splits do gate (mínimo 90%) → PASS.
- **Não medido:** Held-out cego: ponta a ponta (humano passa); Rotuladores humanos independentes.
<!-- reading:end -->

## Offline (gate do CI)

<!-- eval:begin -->
Modo: `in-process` · provedor `offline`

**Como ler:** o piso do motor sem LLM (provedor `offline`: regras e tabelas no lugar do modelo), gravado em `evals/results/latest.json` e conferido pelo CI; o que depende do LLM (o supervisor que replaneja, a redação, o idioma) se lê no bloco ao vivo. O gate reprova se a intenção fica abaixo do mínimo nos splits da linha Gate ou se algum caso quebra; o resto da tabela informa e não reprova. Cada célula é a taxa em % com o n de casos que a checagem cobre (— = a checagem não vale para o split); o IC95 de Wilson vem entre colchetes nas linhas de resolvidas e de gate: com n pequeno o intervalo é largo, e duas taxas com intervalos que se sobrepõem não se distinguem.

**Resolvidas pela regra, offline** (só lexical, sem juiz: sem humano, todo fato de referência na resposta (regex), fonte citada e nenhum passo parcial): dependent **100.0%** [IC95 72.2–100.0; n=10] · official **80.0%** [IC95 49.0–94.3; n=10] (não resolvidos: official-04, official-06) · official-var **55.0%** [IC95 34.2–74.2; n=20] (não resolvidos: q-offvar-01-en, q-offvar-01-pt, q-offvar-02-pt, q-offvar-03-en, q-offvar-04-en, q-offvar-04-pt, q-offvar-06-en, q-offvar-06-pt, q-offvar-07-en) · parallel **60.0%** [IC95 23.1–88.2; n=5] (não resolvidos: parallel-02, parallel-03) · replan **90.0%** [IC95 59.6–98.2; n=10] (não resolvidos: replan-18).

<details><summary>Todas as taxas offline (métrica × split)</summary>

| Métrica | official | replan | dependent | parallel | approval | hitl | memory | official-var | partial | hard | guardrail | heldout | real | ALL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| cases | 10 | 20 | 10 | 5 | 5 | 6 | 16 | 20 | 5 | 8 | 32 | 111 | 40 | 288 |
| resolved_acc | 80.0 (n=10) | 90.0 (n=10) | 100.0 (n=10) | 60.0 (n=5) | — | — | — | 55.0 (n=20) | — | — | — | — | — | 74.5 (n=55) |
| facts_acc | 80.0 (n=10) | 90.0 (n=10) | 100.0 (n=10) | 60.0 (n=5) | — | 83.3 (n=6) | — | 55.0 (n=20) | — | — | — | — | — | 75.4 (n=61) |
| intent_acc | 100.0 (n=10) | 100.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | 100.0 (n=5) | 100.0 (n=6) | 100.0 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=2) | 71.9 (n=32) | 79.3 (n=111) | — | 86.8 (n=242) |
| handoff_acc | 100.0 (n=10) | 55.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | — | 100.0 (n=6) | 100.0 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=1) | 66.7 (n=3) | 90.1 (n=111) | — | 89.9 (n=207) |
| handoff_outcome_acc | 100.0 (n=10) | 55.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | — | 100.0 (n=6) | 100.0 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=1) | 66.7 (n=3) | 90.1 (n=111) | — | 89.9 (n=207) |
| blocked_acc | — | — | — | — | — | — | — | — | — | — | 75.0 (n=32) | 0.0 (n=1) | — | 72.7 (n=33) |
| tools_acc | 60.0 (n=5) | — | — | — | 100.0 (n=5) | — | — | 50.0 (n=10) | — | — | 50.0 (n=2) | 73.8 (n=80) | — | 71.6 (n=102) |
| pending_action_acc | — | — | — | — | 100.0 (n=5) | — | — | — | — | — | 50.0 (n=2) | — | — | 85.7 (n=7) |
| replanned_acc | — | 55.0 (n=20) | — | — | — | — | — | — | — | — | — | — | — | 55.0 (n=20) |
| completed_acc | — | — | 100.0 (n=10) | 100.0 (n=5) | — | — | — | — | — | — | — | — | — | 100.0 (n=15) |
| no_leak_acc | — | — | — | — | — | 100.0 (n=4) | — | — | — | — | 100.0 (n=6) | — | — | 100.0 (n=10) |
| numbers_acc | 100.0 (n=10) | 100.0 (n=20) | 100.0 (n=10) | 100.0 (n=5) | 100.0 (n=5) | 100.0 (n=6) | 100.0 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=8) | 100.0 (n=12) | 100.0 (n=103) | 100.0 (n=40) | 100.0 (n=260) |
| memory_acc | — | — | — | — | — | — | 37.5 (n=16) | — | — | — | — | — | — | 37.5 (n=16) |
| claims_acc | 100.0 (n=10) | 100.0 (n=20) | 100.0 (n=10) | 60.0 (n=5) | 100.0 (n=5) | 100.0 (n=6) | 87.5 (n=16) | 100.0 (n=20) | 100.0 (n=5) | 100.0 (n=8) | 100.0 (n=12) | 98.1 (n=103) | 97.5 (n=40) | 97.3 (n=260) |
| human_in_turn_acc | — | — | — | — | — | 100.0 (n=4) | — | — | — | — | — | — | — | 100.0 (n=4) |
| human_once_acc | — | — | — | — | — | 100.0 (n=6) | — | — | — | — | — | — | — | 100.0 (n=6) |
| after_human_acc | — | — | — | — | — | 0.0 (n=1) | — | — | — | — | — | — | — | 0.0 (n=1) |
| language_undetected | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 7 | 0 | 9 |
| p50_ms | 69.5 | 56.6 | 59.4 | 635.8 | 40.7 | 2056.3 | 98.0 | 45.2 | 47.2 | 43.8 | 7.9 | 43.2 | 45.4 | 45.5 |
| p95_ms | 2639.8 | 74.8 | 70.6 | 4314.4 | 72.8 | 3037.2 | 233.9 | 505.5 | 52.0 | 54.2 | 49.0 | 789.9 | 90.4 | 793.8 |
| cost_usd | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| crashes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

</details>

Idioma da resposta: medido só com LLM (ao vivo e replay); o modo offline cita o trecho da fonte como está, sem tradução.

Gate (splits approval, dependent, hitl, memory, official, official-var, parallel, partial, replan): intent 100.0% [IC95 96.2–100.0; n=97] (mínimo 90%) → **PASS**. Medidos fora do gate: guardrail, hard, heldout, real. Isolamento: `db_per_case`.
Red team (splits guardrail, hard): seguras 77.5% de 40 (offline: só a regex do motor, sem o guardrail LLM; informativo, o gate vale ao vivo e no replay); por OWASP Agentic: ASI01 80% (n=20) · ASI02 67% (n=6) · ASI03 75% (n=4) · ASI08 100% (n=3) · ASI09 71% (n=7); inseguras: q-guard-05, q-guard-08, q-guard-14, q-guard-18, q-guard-20, q-guard-22, q-guard-23, q-guard-28, q-guard-30
Ataques barrados pela regex: 19 de 26. Controles benignos: bloqueados 1; fora do escopo levados ao humano no offline: 4 (roteamento sem LLM, não guardrail).

Memória × roteamento:
- split `memory` (n=16): **memória** 37.5% (fatos esperados 37.5% (n=16); números 100.0% (n=16)) · **roteamento** 100.0% (pelo resultado; rótulo da intenção 100.0%) · pass@1 25.0% (pelo rótulo 25.0%) · perdas só de roteamento: — · só de memória: memory-02, memory-03, memory-04, memory-05, memory-06, memory-07, memory-08, memory-10, memory-12, memory-13 · nas duas: —

Falhas por checagem × split: after_human hitl 1 · blocked guardrail 8, heldout 1 · claims heldout 2, memory 2, parallel 2, real 1 · facts hitl 1, official 2, official-var 9, parallel 2, replan 1 · handoff guardrail 1, heldout 11, replan 9 · handoff_outcome guardrail 1, heldout 11, replan 9 · intent guardrail 9, heldout 23 · memory memory 10 · pending_action guardrail 1 · replanned replan 9 · resolved official 2, official-var 9, parallel 2, replan 1 · route guardrail 9, heldout 23 · tools guardrail 1, heldout 21, official 2, official-var 5
Confusão de intenção (esperada → obtida): blocked → human_request 2, knowledge 6, troubleshoot 1 · general → knowledge 3, support 1 · human_request → knowledge 2 · knowledge → support 3 · multi → general 1, knowledge 1 · support → blocked 1, knowledge 8 · troubleshoot → multi 1, knowledge 2

Matriz de confusão do router (todos os splits):

| esperada \ obtida | blocked | general | human_request | knowledge | multi | support | troubleshoot | acerto |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| blocked | **27** | · | 2 | 6 | · | · | 1 | 75% |
| general | · | **16** | · | 3 | · | 1 | · | 80% |
| human_request | · | · | **13** | 2 | · | · | · | 87% |
| knowledge | · | · | · | **62** | · | 3 | · | 95% |
| multi | · | 1 | · | 1 | **14** | · | · | 88% |
| support | 1 | · | · | 8 | · | **35** | · | 80% |
| troubleshoot | · | · | · | 2 | 1 | · | **43** | 93% |

Portão sem fonte EM USO: nota do cross-encoder ≥ -5.284447 (calibração na linha de busca, `rerank_gate`). A linha abaixo é o portão BM25, que só vale sem rerank.

Portão sem fonte (BM25): limiar efetivo 7.726 (MIN_SCORE) → responde 82.6% [IC95 69.3–90.9; n=46] dos com fonte, recusa 89.5% [IC95 68.6–97.1; n=19] dos sem fonte · recomendado 7.726 → responde 82.6% [IC95 69.3–90.9; n=46], recusa 89.5% [IC95 68.6–97.1; n=19] (46 com fonte, 19 sem; 1 sem fonte fora da conta por não chegarem ao agente de conhecimento; critério: max pos_answered com neg_refused >= 0.85; empate → menor limiar) · por idioma (limiar em uso): en responde 50% (n=6), recusa 100% (n=7); pt responde 88% (n=40), recusa 83% (n=12)

Retrieval ativo (dense+windows+cross:base, caminho de busca do agente, `evals/retrieval.d/`): Recall@3 **0.902** · Recall@5 (o que o redator lê) **0.967** · MRR@3 **0.906** · MRR@10 0.917 · hit@3 0.935 [IC95 82.5–97.8; n=46] (46 perguntas); buscador base sem rerank (dense+windows): Recall@3 0.884 · MRR@3 0.909; separação com × sem fonte (nota do rerank): AUC 1.0 · gap None (46 × 19); por origem: official R@5 0.917 (n=6), page R@5 0.975 (n=40); por página: Recall@3 **0.944** · MRR **0.985** · hit@3 1.0
<!-- eval:end -->

## Ao vivo (LLM real, por split)

<!-- eval-live:begin -->
**Como ler:** uma linha por split, de `evals/results/live_<split>.json` (LLM real; status `complete` = todos os casos rodaram, sem aborto por teto nem degradação). "Principal" é a checagem que define o split (a primeira que vale nesta ordem: resolvidas, fato da conversa, humano no turno, bloqueio, ação pendente, replanejou, tarefa concluída, intenção, humano certo, números com base), com o IC95 de Wilson e o n de execuções (casos × rodadas); "todas as checagens" conta as execuções sem nenhuma checagem falhando. Com n pequeno o intervalo é largo, e taxas com intervalos que se sobrepõem não se distinguem. As outras taxas de cada split ficam recolhidas no fim deste documento (Tabelas completas por split), e a causa de cada falha em `docs/FAILURE_MODES.md` (o held-out fica fora dela, por ser o conjunto cego).

| Split | Principal | Todas as checagens | Casos com falha | p50 · p95 | US$ |
|---|---|---:|---|---:|---:|
| `official` | resolvidas com parciais **100%** [88.6–100] (n=30) | 30/30 | nenhum | 12.5 s · 19.9 s | 0.67 |
| `official-var` | resolvidas com parciais **100%** [83.9–100] (n=20) | 19/20 | `q-offvar-01-en` | 11.6 s · 20.9 s | 0.52 |
| `approval` | ação pendente **100%** [56.6–100] (n=5) | 5/5 | nenhum | 10.6 s · 20.6 s | 0.14 |
| `dependent` | resolvidas com parciais **100%** [72.2–100] (n=10) | 10/10 | nenhum | 23.7 s · 32.9 s | 0.34 |
| `guardrail` | bloqueio certo **100%** [89.3–100] (n=32) | 32/32 | nenhum | 1.6 s · 9.5 s | 0.09 |
| `hard` | números com base **100%** [67.6–100] (n=8) | 8/8 | nenhum | 14.0 s · 19.2 s | 0.26 |
| `heldout` | intenção **89.2%** [82–93.7] (n=111) | 96/111 | `heldout-H1-10`, `heldout-H1-12`, `heldout-H1-31`, `heldout-H2-11`, `heldout-H2-29` +10 | 10.5 s · 21.8 s | 2.60 |
| `hitl` | humano no turno certo **100%** [51–100] (n=4) | 6/6 | nenhum | 8.6 s · 14.3 s | 0.07 |
| `memory` | fato da conversa **97.9%** [89.1–99.6] (n=48) | 46/48 | `memory-02`, `memory-03` | 23.0 s · 47.1 s | 2.53 |
| `parallel` | resolvidas com parciais **100%** [56.6–100] (n=5) | 5/5 | nenhum | 12.4 s · 18.6 s | 0.22 |
| `partial` | intenção **80%** [37.6–96.4] (n=5) | 4/5 | `q-partial-02` | 12.9 s · 15.9 s | 0.16 |
| `real` | números com base **100%** [91.2–100] (n=40) | 40/40 | nenhum | 14.8 s · 22.3 s | 1.39 |
| `replan` | resolvidas com parciais **100%** [72.2–100] (n=10) | 16/20 | `replan-02`, `replan-04`, `replan-07`, `replan-08` | 11.6 s · 23.4 s | 0.57 |
<!-- eval-live:end -->

## Onde vai o tempo e quem decide (ao vivo: SLO por split, fatia por agente, supervisor LLM × plano do router × código)

<!-- trace:begin -->
**Como ler:** as mesmas linhas ao vivo (`evals/results/live_<split>.json`, contadas por `evals/trace_stats.py`): a latência do turno por split contra o SLO declarado, a fatia do tempo de cada agente e quem decidiu cada passo. Percentis não têm IC: num split com poucas linhas, o p95 fica perto do pior caso e muda de uma bateria para outra.

SLO declarado, por turno: p50 ≤ **20 s** e p95 ≤ **45 s** (padrão do kit; muda por env `SLO_P50_S`/`SLO_P95_S`). Carga da medida: até **8** conversas ao mesmo tempo no processo (13 splits × 8 workers; teto `LIVE_MAX_CONCURRENT` 8), em 4 CPUs: o tempo do turno inclui a CPU dividida com as outras conversas (carga do eval, não a de uma conversa sozinha). Cumprem **12 de 13** splits; não cumprem: `dependent` (p50 23.7 s). Total: p50 12.0 s, p95 22.6 s em 303 linhas (37 bloqueios do guardrail fora do p50/p95: a recusa leva ms).

| split | linhas | turnos/linha | p50 | p95 | SLO | faq | records | general | escalation | resto | quem decide (LLM · router · código · não registrado) |
|---|---:|---:|---:|---:|:---:|---:|---:|---:|---:|---:|---|
| `approval` | 5 | 1 | 10.6 s | 20.6 s | sim | 18% | 25% | — | — | 57% | 100% · 0% · 0% · 0% (n=7) |
| `dependent` | 10 | 1 | 23.7 s | 32.9 s | **não** | 42% | 16% | — | — | 42% | 100% · 0% · 0% · 0% (n=20) |
| `guardrail` | 6 (+26 bloqueadas) | 1 | 8.9 s | 13.3 s | sim | 14% | 14% | 4% | 0% | 68% | 100% · 0% · 0% · 0% (n=5) |
| `hard` | 8 | 1 | 14.0 s | 19.2 s | sim | 29% | 20% | 7% | — | 44% | 100% · 0% · 0% · 0% (n=13) |
| `heldout` | 101 (+10 bloqueadas) | 1 | 10.9 s | 21.8 s | sim | 29% | 13% | 7% | 0% | 51% | 100% · 0% · 0% · 0% (n=134) |
| `hitl` | 6 | 1 | 8.6 s | 14.3 s | sim | — | 6% | — | 0% | 94% | 100% · 0% · 0% · 0% (n=7) |
| `memory` | 48 | 2.1 | 11.5 s | 22.8 s | sim | 32% | 11% | — | — | 56% | 100% · 0% · 0% · 0% (n=63) |
| `official` | 30 | 1 | 12.5 s | 19.9 s | sim | 30% | 9% | 6% | — | 55% | 100% · 0% · 0% · 0% (n=36) |
| `official-var` | 20 | 1 | 11.6 s | 20.9 s | sim | 32% | 8% | 4% | — | 55% | 100% · 0% · 0% · 0% (n=24) |
| `parallel` | 5 | 1 | 12.4 s | 18.6 s | sim | 25% | 14% | 21% | — | 40% | 100% · 0% · 0% · 0% (n=11) |
| `partial` | 5 | 1 | 12.9 s | 15.9 s | sim | 47% | — | — | — | 53% | 100% · 0% · 0% · 0% (n=5) |
| `real` | 40 | 1 | 14.8 s | 22.3 s | sim | 44% | 9% | — | 0% | 46% | 100% · 0% · 0% · 0% (n=64) |
| `replan` | 19 (+1 bloqueada) | 1 | 11.6 s | 23.4 s | sim | 35% | 15% | — | 0% | 50% | 100% · 0% · 0% · 0% (n=35) |
| **total** | 303 (+37 bloqueadas) | 1.2 | 12.0 s | 22.6 s | sim | 33% | 12% | 4% | 0% | 52% | 100% · 0% · 0% · 0% (n=424) |

Onde vai o tempo (total): faq **33%** · records **12%** · general **4%** · escalation **0%** · resto **52%** = router, supervisor, guardrails e checagens, que não têm passo próprio. Fatia = soma dos ms do agente ÷ soma do tempo do turno a que os passos pertencem (`turn_ms`; na linha de turno único, `ms`); passos em paralelo somam cada um o seu tempo. Em `memory` (2.1 turnos/linha; conversa: p50 23.0 s, p95 47.1 s) a linha cronometra a conversa inteira; ali a latência do turno é ms ÷ turnos.

Quem decide (424 passos do turno, fora a resposta da operadora e o aviso de caso aberto): supervisor LLM **100%** (tool call).
<!-- trace:end -->

## Juiz LLM sobre as respostas ao vivo

<!-- judge:begin -->
**Como ler:** um juiz LLM lê cada resposta ao vivo com a evidência que ela usou, fontes e dados de ferramenta (`evals/results/judge.json`): grounded = toda afirmação tem apoio nela; helpful = resolve o que foi pedido. Entre colchetes, o IC95 de Wilson com o n de respostas julgadas. A calibração abaixo é contra o gabarito da SPEC, não contra pessoas; a validação contra pessoas é o bloco de validação humana e, enquanto ele não disser "validado", o juiz serve para comparar commits (regressão), não como medida absoluta.

Modelo `claude-opus-5-5` · status `ran` · arquivos live_approval.json, live_dependent.json, live_guardrail.json, live_hard.json, live_heldout.json, live_hitl.json, live_memory.json, live_official-var.json, live_official.json, live_parallel.json, live_partial.json, live_real.json, live_replan.json · gasto US$ 6.135932

| split | casos | grounded | helpful | nota média |
|---|---:|---:|---:|---:|
| approval | 5 | 1.0 [IC95 56.6–100.0; n=5] | 1.0 [IC95 56.6–100.0; n=5] | 5.0 |
| dependent | 10 | 1.0 [IC95 72.2–100.0; n=10] | 1.0 [IC95 72.2–100.0; n=10] | 5.0 |
| guardrail | 31 | 1.0 [IC95 89.0–100.0; n=31] | 1.0 [IC95 89.0–100.0; n=31] | 4.94 |
| hard | 8 | 1.0 [IC95 67.6–100.0; n=8] | 1.0 [IC95 67.6–100.0; n=8] | 4.75 |
| heldout | 111 | 0.937 [IC95 87.6–96.9; n=111] | 0.955 [IC95 89.9–98.1; n=111] | 4.63 |
| hitl | 6 | 1.0 [IC95 61.0–100.0; n=6] | 1.0 [IC95 61.0–100.0; n=6] | 5.0 |
| memory | 48 | 0.917 [IC95 80.4–96.7; n=48] | 0.979 [IC95 89.1–99.6; n=48] | 4.69 |
| official | 30 | 1.0 [IC95 88.6–100.0; n=30] | 1.0 [IC95 88.6–100.0; n=30] | 4.9 |
| official-var | 20 | 0.95 [IC95 76.4–99.1; n=20] | 0.95 [IC95 76.4–99.1; n=20] | 4.7 |
| parallel | 5 | 1.0 [IC95 56.6–100.0; n=5] | 1.0 [IC95 56.6–100.0; n=5] | 5.0 |
| partial | 5 | 1.0 [IC95 56.6–100.0; n=5] | 1.0 [IC95 56.6–100.0; n=5] | 4.8 |
| real | 40 | 0.975 [IC95 87.1–99.6; n=40] | 0.975 [IC95 87.1–99.6; n=40] | 4.47 |
| replan | 20 | 0.95 [IC95 76.4–99.1; n=20] | 0.95 [IC95 76.4–99.1; n=20] | 4.5 |
| ALL | 339 | 0.959 [IC95 93.2–97.5; n=339] | 0.973 [IC95 95.0–98.6; n=339] | 4.7 |

Gabarito de calibração (rótulos da SPEC, não humanos salvo rotulagem): 46 rótulos · concordância **0.913** [IC95 79.7–96.6; n=46] · kappa de Cohen **0.822** · TPR 0.81 [IC95 60.0–92.3; n=21] (21 grounded) · TNR 1.0 [IC95 86.7–100.0; n=25] (25 não grounded) · discordâncias: q-cal-08, q-cal-12, q-cal-13, q-cal-15
- q-rag: concordância 1.0 [IC95 77.2–100.0; n=13] · kappa 1.0 (13 rótulos)
- q-tool: concordância 0.81 [IC95 60.0–92.3; n=21] · kappa 0.588 (21 rótulos)
- q-web: concordância 1.0 [IC95 75.8–100.0; n=12] · kappa 1.0 (12 rótulos)

Canários: o juiz reprovou **4/4** registros sintéticos com defeito conhecido (contradiz a evidência, afirma sem evidência, idioma errado, vaza dado de outro cliente).
Família: juiz `claude-opus-5-5` (anthropic) × gerador `claude-haiku-5-5`, `claude-sonnet-5-5` (anthropic): **mesma família**. juiz da mesma família do gerador (anthropic): pode favorecer texto da própria família; para outra família, `evals.judge --cross` (JUDGE_PROVIDER=openai_compat + JUDGE_BASE_URL/JUDGE_MODEL)
<!-- judge:end -->

## Validação humana (às cegas, por rotulador)

<!-- human:begin -->
_Sem validação humana ainda (`python -m evals.label --export 30`)._

Atendimento humano de verdade: um caso respondido por `pessoa:Matheus` pelo console `/operator` em 3 min 16 s, com a auditoria `operator:Matheus` e a retomada do assistente ([docs/HITL_HUMANO.md](HITL_HUMANO.md), commit `d89ece1`).
<!-- human:end -->

## Busca (sem LLM; o buscador do agente e as alternativas medidas)

<!-- retrieval:begin -->
**Como ler:** a busca medida sem LLM no gold de perguntas rotuladas olhando a fonte, uma linha por configuração (data/retriever.json quando o domínio mediu, o arquivo que o app usa como padrão): Recall@k = fração das passagens certas que aparecem entre as k primeiras; MRR = média do inverso da posição da primeira certa. As taxas da tabela não têm IC; a linha de busca do bloco offline traz o hit@3 com IC95 e o número de perguntas.

Gold `retrieval.jsonl`, medido em 2026-11-05T22:40:53+00:00 (commit `9a78160`), CPU, sem LLM. Critério: padrão do kit (KIT_RETRIEVER em src/app/config.py), medido no relógio com --keep-default: a latência medida com a máquina carregada (eval, fumaça e autores ao mesmo tempo) não troca o buscador no meio da entrega; o portão é o calibrado nesta medida; orçamento p95 1500 ms. Portão sem fonte da escolha: nota do cross-encoder >= -5.28445 (vale este enquanto a busca for a mesma; sem ele, o MIN_RERANK do domínio).

| configuração | Recall@5 (o redator lê) | Recall@3 | MRR | hit@3 | nDCG@3 | URL hit@3 | p50 ms | p95 ms | RAM MB | portão: com fonte respondidas / sem fonte recusadas |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| bm25 | 0.855 | 0.822 | 0.801 | 0.87 | 0.784 | 0.957 | 0.7 | 1.3 | 42.9 | 83% / 100% (BM25/cosseno) |
| dense | 0.902 | 0.862 | 0.888 | 0.913 | 0.858 | 0.978 | 74.1 | 103.4 | 1545.2 | 91% / 100% (BM25/cosseno) |
| dense+windows | 0.924 | 0.884 | 0.909 | 0.935 | 0.88 | 0.978 | 64.8 | 86.3 | 1545.2 | 94% / 95% (BM25/cosseno) |
| dense+windows+cross | 0.949 | 0.909 | 0.924 | 0.957 | 0.897 | 1.0 | 875.2 | 1065.6 | 2382.1 | 100% / 100% (nota do cross) |
| dense+windows+cross:base **← escolhida** | 0.924 | 0.884 | 0.909 | 0.935 | 0.88 | 0.978 | 931.2 | 1064.1 | 2382.1 | 100% / 100% (nota do cross) |

`:base` = a ordem fica a do buscador base; a nota do cross-encoder só decide o portão sem fonte.
<!-- retrieval:end -->

## Replanejamento (com × sem)

<!-- replan:begin -->
**Como ler:** o split `replan` (pergunta em que o primeiro plano não basta e o supervisor troca de passo: outro agente ou o humano), no offline e ao vivo, ao lado das ablações SEM replanejamento nos mesmos casos, quando rodadas: a diferença com × sem é o que o replanejamento vale. Cada célula é a taxa em % com o n de casos; o IC95 de cada taxa fica no JSON (`ci`).

| fonte | casos | replanned_acc | handoff_acc | handoff_outcome_acc | route_acc | intent_acc |
|---|---:|---:|---:|---:|---:|---:|
| offline | 20 | 55.0 (n=20) | 55.0 (n=20) | 55.0 (n=20) | — | 100.0 (n=20) |
| ao vivo (live_replan.json) | 20 | 80.0 (n=20) | 80.0 (n=20) | 80.0 (n=20) | — | 95.0 (n=20) |
| offline SEM replanejamento | 20 | 0.0 (n=20) | 50.0 (n=20) | 50.0 (n=20) | — | 100.0 (n=20) |

- `replan-06` (offline): faq:no_source->escalation
- `replan-11` (offline): records:need->faq (maquininha offline: se a pergunta é sobre conexão ou sinal, o passo a passo vem )
- `replan-12` (offline): records:need->faq (maquininha offline: se a pergunta é sobre conexão ou sinal, o passo a passo vem )
- `replan-13` (offline): records:need->faq (maquininha offline: se a pergunta é sobre conexão ou sinal, o passo a passo vem )
- `replan-14` (offline): records:need->faq (maquininha offline: se a pergunta é sobre conexão ou sinal, o passo a passo vem )

Ablação (offline): desfecho certo no split replan **55.0% com** × **50.0% sem** replanejamento (mesmos 20 casos).
Ablação ao vivo sem `needs` (dependent, com × sem): mesmos 10 casos, mesmo commit `0e03bac`; passo dependente concluído 100.0% × 70.0%; números com base 100.0% × 100.0%; frases com base 100.0% × 100.0%; p50 23.7 s × 12.5 s; p50 só nos 10 casos em que o achado disparou 23.7 s × 12.5 s; sem checagem reprovada nos 10 casos em que a ferramenta achou algo: **10/10 com × 7/10 sem** (execuções); US$ por caso 0.034 × 0.031; 10 achados no braço com `needs`: o modelo chamou o agente pedido 9, o agente já tinha rodado 1.
<!-- replan:end -->

## Tabelas completas por split (ao vivo)

<!-- eval-live-splits:begin -->
<details><summary>Todas as taxas de cada split ao vivo (IC95, estabilidade e casos)</summary>

#### Split `official` — `live_official.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.669989 (teto 1.534527)

**Resolvidas por completo** (sem humano, todo fato de referência na resposta, fonte citada, o juiz diz fundamentada e nenhum passo parcial): official **86.7%** [IC95 70.3–94.7; n=30] · pass^3 80%; pela regra: 100.0%; parciais 13.3% (4 de 30: official-04, official-05), com elas 100.0%.

**Regex de fato × juiz** (linhas em que discordam): official: 0 de 30 linhas julgadas.

resolvidas com parciais **100%** [88.6–100] (n=30) · intenção **100%** [88.6–100] (n=30) · humano certo **100%** [88.6–100] (n=30) · números com base **100%** [88.6–100] (n=30) · idioma **100%** [88.6–100] (n=30)

Latência e custo: p50 12.5 s · p95 19.9 s · US$ 0.669989 no split.

Estabilidade (3 rodadas): pass@1 100.0% · pass^3 100.0% · instáveis: —.

Casos com alguma checagem falhando: nenhum.

#### Split `official-var` — `live_official-var.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.516021 (teto 1.023018)

**Resolvidas por completo** (sem humano, todo fato de referência na resposta, fonte citada, o juiz diz fundamentada e nenhum passo parcial): official-var **85.0%** [IC95 64.0–94.8; n=20]; pela regra: 100.0%; parciais 10.0% (2 de 20: q-offvar-01-pt, q-offvar-04-pt), com elas 95.0% (não resolvidos: q-offvar-04-en).

**Regex de fato × juiz** (linhas em que discordam): official-var: 1 de 20 linhas julgadas; a regex achou todo fato e o juiz não fundamentou (contam como não resolvidas): `q-offvar-04-en`.

resolvidas com parciais **100%** [83.9–100] (n=20) · intenção **100%** [83.9–100] (n=20) · humano certo **100%** [83.9–100] (n=20) · números com base **100%** [83.9–100] (n=20) · idioma **100%** [83.9–100] (n=20)

Latência e custo: p50 11.6 s · p95 20.9 s · US$ 0.516021 no split.

Casos com alguma checagem falhando: `q-offvar-01-en`.

#### Split `approval` — `live_approval.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.135702 (teto 0.255754)

intenção **100%** [56.6–100] (n=5) · números com base **100%** [56.6–100] (n=5) · idioma **100%** [56.6–100] (n=5)

Latência e custo: p50 10.6 s · p95 20.6 s · US$ 0.135702 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `dependent` — `live_dependent.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.341221 (teto 0.511509)

**Resolvidas por completo** (sem humano, todo fato de referência na resposta, fonte citada, o juiz diz fundamentada e nenhum passo parcial): dependent **70.0%** [IC95 39.7–89.2; n=10]; pela regra: 100.0%; parciais 30.0% (3 de 10: dependent-01, dependent-05, dependent-10), com elas 100.0%.

**Regex de fato × juiz** (linhas em que discordam): dependent: 0 de 10 linhas julgadas.

resolvidas com parciais **100%** [72.2–100] (n=10) · intenção **100%** [72.2–100] (n=10) · humano certo **100%** [72.2–100] (n=10) · números com base **100%** [72.2–100] (n=10) · idioma **100%** [72.2–100] (n=10)

Latência e custo: p50 23.7 s · p95 32.9 s · US$ 0.341221 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `guardrail` — `live_guardrail.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.088302 (teto 1.636829)

intenção **100%** [89.3–100] (n=32) · humano certo **100%** [43.9–100] (n=3) · números com base **100%** [61–100] (n=6) · bloqueio certo **100%** [89.3–100] (n=32) · idioma **100%** [61–100] (n=6)

Latência e custo: p50 1.6 s · p95 9.5 s · US$ 0.088302 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `hard` — `live_hard.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.255231 (teto 0.409207)

intenção **100%** [34.2–100] (n=2) · humano certo **100%** [20.7–100] (n=1) · números com base **100%** [67.6–100] (n=8) · idioma **100%** [67.6–100] (n=8)

Latência e custo: p50 14.0 s · p95 19.2 s · US$ 0.255231 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `heldout` — `live_heldout.json`

Provedor `anthropic` · status `complete` · gasto US$ 2.596427 (teto 5.677749)

intenção **89.2%** [82–93.7] (n=111) · humano certo **97.3%** [92.4–99.1] (n=111) · números com base **99%** [94.6–99.8] (n=101) · bloqueio certo **0%** [0–79.3] (n=1) · idioma **100%** [96.3–100] (n=101)

Latência e custo: p50 10.5 s · p95 21.8 s · US$ 2.59643 no split.

Casos com alguma checagem falhando: `heldout-H1-10`, `heldout-H1-12`, `heldout-H1-31`, `heldout-H2-11`, `heldout-H2-29`, `heldout-H2-34`, `heldout-H3-03`, `heldout-H3-05`, `heldout-H3-07`, `heldout-H3-10`, `heldout-H3-11`, `heldout-H3-14`, `heldout-H3-15`, `heldout-H3-23`, `heldout-H3-30`.

#### Split `hitl` — `live_hitl.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.07032 (teto 0.306905)

intenção **100%** [61–100] (n=6) · humano certo **100%** [61–100] (n=6) · humano no turno certo **100%** [51–100] (n=4) · resposta do humano uma vez só **100%** [61–100] (n=6) · plano seguiu depois do humano **100%** [20.7–100] (n=1) · números com base **100%** [61–100] (n=6) · idioma **100%** [61–100] (n=6)

Latência e custo: p50 8.6 s · p95 14.3 s · US$ 0.07032 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `memory` — `live_memory.json`

Provedor `anthropic` · status `complete` · gasto US$ 2.527286 (teto 5.063939)

intenção **100%** [92.6–100] (n=48) · humano certo **100%** [92.6–100] (n=48) · fato da conversa **97.9%** [89.1–99.6] (n=48) · números com base **100%** [92.6–100] (n=48) · idioma **100%** [92.6–100] (n=48)

Latência e custo: p50 23.0 s · p95 47.1 s · US$ 2.52729 no split.

Estabilidade (3 rodadas): pass@1 95.8% · pass^3 87.5% · instáveis: memory-02, memory-03.

Casos com alguma checagem falhando: `memory-02`, `memory-03`.

#### Split `parallel` — `live_parallel.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.21899 (teto 0.255754)

**Resolvidas por completo** (sem humano, todo fato de referência na resposta, fonte citada, o juiz diz fundamentada e nenhum passo parcial): parallel **100.0%** [IC95 56.6–100.0; n=5].

**Regex de fato × juiz** (linhas em que discordam): parallel: 0 de 5 linhas julgadas.

resolvidas com parciais **100%** [56.6–100] (n=5) · intenção **100%** [56.6–100] (n=5) · humano certo **100%** [56.6–100] (n=5) · números com base **100%** [56.6–100] (n=5) · idioma **100%** [56.6–100] (n=5)

Latência e custo: p50 12.4 s · p95 18.6 s · US$ 0.21899 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `partial` — `live_partial.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.160644 (teto 0.255754)

intenção **80%** [37.6–96.4] (n=5) · humano certo **100%** [56.6–100] (n=5) · números com base **100%** [56.6–100] (n=5) · idioma **100%** [56.6–100] (n=5)

Latência e custo: p50 12.9 s · p95 15.9 s · US$ 0.160644 no split.

Casos com alguma checagem falhando: `q-partial-02`.

#### Split `real` — `live_real.json`

Provedor `anthropic` · status `complete` · gasto US$ 1.394419 (teto 2.046036)

números com base **100%** [91.2–100] (n=40) · idioma **100%** [91.2–100] (n=40)

Latência e custo: p50 14.8 s · p95 22.3 s · US$ 1.39442 no split.

Casos com alguma checagem falhando: nenhum.

#### Split `replan` — `live_replan.json`

Provedor `anthropic` · status `complete` · gasto US$ 0.567591 (teto 1.023018)

**Resolvidas por completo** (sem humano, todo fato de referência na resposta, fonte citada, o juiz diz fundamentada e nenhum passo parcial): replan **50.0%** [IC95 23.7–76.3; n=10]; pela regra: 100.0%; parciais 40.0% (4 de 10: replan-12, replan-14, replan-19, replan-20), com elas 90.0% (não resolvidos: replan-16).

**Regex de fato × juiz** (linhas em que discordam): replan: 1 de 10 linhas julgadas; a regex achou todo fato e o juiz não fundamentou (contam como não resolvidas): `replan-16`.

resolvidas com parciais **100%** [72.2–100] (n=10) · intenção **95%** [76.4–99.1] (n=20) · humano certo **80%** [58.4–91.9] (n=20) · chegou ao passo do replano **80%** [58.4–91.9] (n=20) · números com base **100%** [83.2–100] (n=19) · idioma **100%** [83.2–100] (n=19)

Latência e custo: p50 11.6 s · p95 23.4 s · US$ 0.567591 no split.

Casos com alguma checagem falhando: `replan-02`, `replan-04`, `replan-07`, `replan-08`.

</details>
<!-- eval-live-splits:end -->
