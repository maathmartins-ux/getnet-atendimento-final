"""official-04 ("Do I need a bank account to receive my sales via Pix?") perdia 3/3 o fato "Get Conta": o router
escrevia a busca do requisito ("Pix recebimento conta bancária requisito"), a mesma que o sistema já faz
(requirement_query), e o trecho da Get Conta (sup-get-conta-02) ficava fora do top-5. Medido sem LLM no caminho do
agente: com a busca do router voltada à conta da Getnet, os dois trechos do gold (domicílio Santander e Get Conta)
entram no top-5, em inglês e em português."""
from __future__ import annotations

from pathlib import Path

from app import domain

PROMPTS = Path(__file__).resolve().parents[1] / "src" / "app" / "domain" / "challenge_prompts"


def test_router_prompt_points_the_account_question_to_get_conta():
    router_md = (PROMPTS / "router.md").read_text("utf-8")
    assert "PRECISA DE CONTA" in router_md
    assert "Get Conta conta digital gratuita receber vendas <produto>" in router_md
    assert "não repita essa busca" in router_md


def test_the_requirement_search_stays_with_the_system(domain_data):
    """A busca dos critérios continua a do sistema: é ela que traz o domicílio bancário (o outro fato)."""
    for text in ("Do I need a bank account to receive my sales via Pix?",
                 "Para receber Pix das vendas preciso abrir conta em banco?"):
        assert domain.active().requirement_query(text) == "critérios de elegibilidade para habilitação do Pix"
