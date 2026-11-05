"""A CI não vetoriza o corpus do zero em cada job: o cache dos vetores sobrevive ao cancelamento e chega ao build."""
from pathlib import Path

import yaml

CI = yaml.safe_load((Path(__file__).resolve().parents[1] / ".github/workflows/ci.yml").read_text(encoding="utf-8"))


def _steps(job: str) -> list[dict]:
    return CI["jobs"][job]["steps"]


def test_core_saves_vectors_before_the_long_check():
    steps = _steps("check")
    names = [str(s.get("run", "")) + str(s.get("uses", "")) for s in steps]
    check = next(i for i, n in enumerate(names) if "scripts/check.py" in n)
    early = [i for i, s in enumerate(steps) if "cache/save" in str(s.get("uses", ""))
             and str(s.get("with", {}).get("key", "")).endswith("-early")]
    assert early and early[0] < check


def test_image_build_gets_the_vectors_and_no_layer_cache_export():
    steps = _steps("supply-chain")
    restore = next(i for i, s in enumerate(steps) if "cache/restore" in str(s.get("uses", "")))
    build = next(i for i, s in enumerate(steps) if "build-push-action" in str(s.get("uses", "")))
    assert restore < build and "var/embeddings" in steps[restore]["with"]["path"]
    assert "cache-to" not in steps[build]["with"]
