# Imagem construída e testada no ambiente de construção

Gerado por `scripts/docker_proof.sh` em 2026-11-05T23:08Z, commit `1a38cbd` (árvore com mudanças);
Docker 29.9.2; imagem 5.28GB. Resultado: VERDE.

| etapa | resultado | s |
|---|---|---:|
| docker build (hybrid) | PASS | 229.9 |
| imagem sem dev/extras | PASS | 1.6 |
| docker run | PASS | 0.3 |
| container /health com dados | PASS | 8.0 |
| eval via HTTP (oficiais) | PASS | 13.6 |
| mcp no container (401 sem token, initialize com JWT) | PASS | 0.2 |
| container sem rede (--network none) | PASS | 11.9 |
| réplicas (conversa, caso único, queda) | PASS | 47.2 |

O mesmo teste roda na CI (job `check (docker)`); este arquivo é a prova para quem lê o repositório sem abrir o Actions.
