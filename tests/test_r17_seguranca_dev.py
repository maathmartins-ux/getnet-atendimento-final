"""Sem senha padrão no Grafana do compose: ele sobe sem conta admin, só leitura e só em loopback."""
from pathlib import Path

import yaml

COMPOSE = yaml.safe_load((Path(__file__).resolve().parents[1] / "docker-compose.yml").read_text(encoding="utf-8"))


def test_grafana_has_no_default_admin_password():
    g = COMPOSE["services"]["grafana"]
    env = {k: str(v) for k, v in g["environment"].items()}
    assert "GF_SECURITY_ADMIN_PASSWORD" not in env and not any("change-me" in v for v in env.values())
    assert env["GF_SECURITY_DISABLE_INITIAL_ADMIN_CREATION"] == "true"
    assert env["GF_AUTH_ANONYMOUS_ORG_ROLE"] == "Viewer"
    assert all(str(p).startswith("127.0.0.1:") for p in g["ports"])
