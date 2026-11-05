"""Frente Q: os 10 oficiais pela API HTTP com o Bearer JWT; token ruim ou ausente = 401, e o `user_id` do corpo é
ignorado (não há modo que o aceite: a identidade é só do token).

O conteúdo da resposta é medido pelo eval (split official); aqui o contrato HTTP: status, identidade e campos."""

import json

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.auth import LIMITER, issue_token
from app.config import ROOT

USER = "cliente1988"


def _officials() -> list[dict]:
    rows = [json.loads(line) for line in (ROOT / "evals" / "cases.jsonl").read_text("utf-8").splitlines()
            if line.strip()]
    return [r for r in rows if r.get("split") == "official"]


@pytest.fixture
def client(domain_data, monkeypatch):
    monkeypatch.setattr(LIMITER, "allow", lambda key: True)  # 20 chamadas seguidas não podem cair no 429
    return TestClient(app)


def _check_contract(body: dict, case: dict) -> None:
    assert body["user_id"] == USER
    assert body["answer"].strip() and body["trace_id"] and body["conversation_id"]
    assert body["blocked"] is False, f"{case['id']}: oficial não pode ser bloqueado"


def test_there_are_ten_officials():
    assert len(_officials()) == 10


@pytest.mark.parametrize("case", _officials(), ids=lambda c: c["id"])
def test_official_over_http_with_bearer(client, case):
    r = client.post("/chat", json={"message": case["message"]},
                    headers={"Authorization": f"Bearer {issue_token(USER)}"})
    assert r.status_code == 200, r.text
    _check_contract(r.json(), case)


def test_bad_token_is_401(client):
    r = client.post("/chat", json={"message": "Quanto vendi ontem?", "user_id": USER},
                    headers={"Authorization": "Bearer token-forjado-pela-lojadojoao"})
    assert r.status_code == 401


@pytest.mark.parametrize("auth_mode", [None, "demo"])
def test_body_user_id_without_token_is_401(client, monkeypatch, auth_mode):
    """Sem token, o `user_id` do corpo não vira identidade, nem com a antiga variável AUTH_MODE=demo no ambiente."""
    if auth_mode:
        monkeypatch.setenv("AUTH_MODE", auth_mode)
    r = client.post("/chat", json={"message": "Quanto vendi ontem?", "user_id": USER})
    assert r.status_code == 401


def test_body_user_id_cannot_override_token_identity(client):
    r = client.post("/chat", json={"message": "Quanto vendi ontem?", "user_id": "cliente2024"},
                    headers={"Authorization": f"Bearer {issue_token(USER)}"})
    assert r.status_code == 200 and r.json()["user_id"] == USER
