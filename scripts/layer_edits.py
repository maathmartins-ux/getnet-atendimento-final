"""Quanto cada camada depois do LLM muda as respostas reais: replay das gravações ao vivo (evals/cassettes/, sem rede
e sem gasto) contando `answer_layer_edits_total{layer}` por turno. Grava evals/results/layer_edits.json.

Uso: python scripts/layer_edits.py [--splits official,memory] [--workers 4]
Camada que não muda nenhuma resposta gravada é candidata a sair (medido em 05/11 sobre 289 turnos gravados: a que punha
"a resposta primeiro" mudou 0 e saiu); a que muda diz em quantas e por quê (docstring dela).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT / "src")]

LAYERS = ("numbers_and_language", "scrub_internal", "claims", "must_escalate", "drop_wait_notice")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--splits", default="", help="splits a reproduzir (padrão: todos os gravados)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default=str(ROOT / "evals" / "results" / "layer_edits.json"))
    args = ap.parse_args(argv)
    from app.observability import METRICS
    from evals import run_evals

    cmd = ["--replay", "--workers", str(args.workers), "--out", str(ROOT / "var" / "replay" / "layer_edits_run.json")]
    if args.splits:
        cmd += ["--splits", args.splits]
    code = run_evals.main(cmd)
    turns = int(METRICS.get("answer_layer_turns_total"))
    edits = {layer: int(METRICS.get("answer_layer_edits_total", layer=layer)) for layer in LAYERS}
    report = {"turns": turns, "edits": edits, "replay_exit": code,
              "rate": {k: round(v / turns, 4) if turns else None for k, v in edits.items()}}
    Path(args.out).write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if turns else 1


if __name__ == "__main__":
    raise SystemExit(main())
