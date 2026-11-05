"""Identidade só do token: o `user_id` do corpo ou da query nunca vira identidade (o modo demo saiu, ADR 0001)."""
import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.auth import issue_token

client = TestClient(app)
MSG = {"message": "Onde está meu pedido 1002?", "user_id": "u1"}  # 1002 é de u1


def bearer(user):
    return {"Authorization": f"Bearer {issue_token(user)}"}


# --- required (padrão) --------------------------------------------------------------------------
def test_required_rejects_body_identity():
    assert client.post("/chat", json=MSG).status_code == 401
    assert client.post("/chat", json=MSG, headers={"Authorization": "Bearer u1.forjado"}).status_code == 401


def test_required_identity_comes_from_token_not_body():
    body = client.post("/chat", json=MSG, headers=bearer("u2")).json()  # u2 tenta se passar por u1
    assert body["user_id"] == "u2" and body["identity_verified"] is True and "Livro B" not in body["answer"]


# --- o antigo modo demo não existe mais ------------------------------------------------------------
@pytest.fixture
def old_demo_env(monkeypatch):
    monkeypatch.setenv("AUTH_MODE", "demo")  # a variável antiga é ignorada


def test_old_demo_variable_does_not_accept_the_body_identity(old_demo_env):
    assert client.post("/chat", json=MSG).status_code == 401
    assert client.get("/health").json()["auth_mode"] == "required"


def test_valid_token_is_the_identity_even_with_old_demo_variable(old_demo_env):
    body = client.post("/chat", json=MSG, headers=bearer("u2")).json()
    assert body["user_id"] == "u2" and body["identity_verified"] is True and "Livro B" not in body["answer"]


def test_query_user_id_never_opens_someone_elses_conversation(old_demo_env):
    conv = client.post("/chat", json=MSG, headers=bearer("u1")).json()["conversation_id"]
    assert client.get(f"/conversations/{conv}", headers=bearer("u1")).status_code == 200
    assert client.get(f"/conversations/{conv}", params={"user_id": "u1"}).status_code == 401
    assert client.get(f"/conversations/{conv}", params={"user_id": "u1"}, headers=bearer("u2")).status_code == 404
