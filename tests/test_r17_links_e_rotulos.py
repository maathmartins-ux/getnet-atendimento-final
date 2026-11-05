"""Rodada 17 (produção): link do bloco gerado relativo ao arquivo que o recebe, e um nome por medida de resolução."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_block_links_are_relative_to_the_file_that_receives_them():
    fill = _load("fill_readme")
    md = "caso real ([docs/HITL_HUMANO.md](docs/HITL_HUMANO.md)), juiz ([j](evals/results/judge.json#x)), [w](https://a.b)"
    assert fill.relink(md, "README.md") == md
    out = fill.relink(md, "docs/RESULTS.md")
    assert "](HITL_HUMANO.md)" in out and "](../evals/results/judge.json#x)" in out and "](https://a.b)" in out


def test_resolution_with_partials_has_its_own_name():
    """A linha de cada split diz "resolvidas pela regra" (sem parciais); a tabela usava o mesmo nome para a medida que
    conta as parciais, e o check --docs reprovava a entrega (2 valores para uma medida no mesmo split)."""
    from evals.run_evals import SUMMARY_KEYS

    assert dict(SUMMARY_KEYS)["resolved_acc"] == "resolvidas com parciais"


def test_demo_never_calls_complete_an_answer_the_judge_rejected():
    from scripts.demo_md import checks_line

    row = {"checks": {"intent": True, "facts": True}, "steps": [{"status": "ok"}]}
    assert "completa" in checks_line(row)
    line = checks_line(row, {"grounded": False, "failure_type": "false_absence"})
    assert "não resolvida (o juiz reprova: false_absence)" in line and "**juiz:** reprovada" in line
    assert "**juiz:** fundamentada" in checks_line(row, {"grounded": True})


def test_two_pass_k_measures_have_two_names():
    from scripts.scorecard import TARGETS

    names = {t.key: t.label for t in TARGETS}
    assert "pass^k" not in names["official_pass_k"] and "sem o juiz" in names["official_pass_k"]


def test_timesheet_lists_the_commits_where_live_answers_were_measured(tmp_path):
    import json
    import subprocess

    ts = _load("timesheet")
    run = lambda *a: subprocess.run(["git", *a], cwd=tmp_path, check=True, capture_output=True, text=True)  # noqa: E731
    run("init", "-q", "-b", "main")
    run("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "--allow-empty", "-m", "chore: scaffold x")
    sha = run("rev-parse", "HEAD").stdout.strip()
    (tmp_path / "evals" / "results").mkdir(parents=True)
    (tmp_path / "evals" / "results" / "live_official.json").write_text(json.dumps({"git_sha": sha[:7]}))
    ev = ts.evidence_commits(tmp_path)
    assert [e["sha"] for e in ev] == [sha[:7]] and ev[0]["splits"] == ["official"] and ev[0]["merge"] is False


def test_live_headline_is_a_check_that_covers_the_split():
    fr = _load("fill_readme")
    report = {"split": "heldout", "status": "complete", "rows": [], "metrics": {"ALL": {
        "blocked_acc": 0.0, "intent_acc": 89.2, "cases": 111,
        "ci": {"blocked_acc": {"lo": 0, "hi": 79.3, "n": 1}, "intent_acc": {"lo": 82, "hi": 94, "n": 111}}}}}
    row = fr.live_row(report, "live_heldout.json")
    assert "intenção **89.2%**" in row and "bloqueio" not in row


def test_table_row_inside_mermaid_fails_the_docs_check(tmp_path):
    check = _load("check")
    (tmp_path / "docs").mkdir()
    broken = "# x\n\n```mermaid\nflowchart LR\n| a | b |\n  A --> B\n```\n"
    (tmp_path / "README.md").write_text(broken, encoding="utf-8")
    _, ok, _, detail = check.diagrams_intact(tmp_path)
    assert not ok and "README.md:5" in detail
    fine = "# x\n\n```mermaid\nflowchart LR\n  A -->|x| B\n```\n\n| a | b |\n"
    (tmp_path / "README.md").write_text(fine, encoding="utf-8")
    assert check.diagrams_intact(tmp_path)[1]
