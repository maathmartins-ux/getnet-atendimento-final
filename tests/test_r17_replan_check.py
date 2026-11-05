"""O caso de replanejamento pede que o turno chegue ao passo que o 1º especialista sozinho não cobre."""
from evals.run_evals import score

CASE = {"id": "replan-x", "expect": {"replanned": True}}


def _got(route, replans=(), handoff=False):
    return {"intent": "troubleshoot", "route": route, "replans": list(replans), "handoff_required": handoff,
            "answer": ""}


def test_deviation_from_the_router_plan_counts():
    assert score(CASE, _got(["router", "faq", "records"], replans=["faq->records"]))["replanned"]


def test_plan_that_already_had_the_step_counts():
    assert score(CASE, _got(["router", "records", "faq"]))["replanned"]


def test_one_specialist_or_a_human_is_not_the_step():
    assert not score(CASE, _got(["router", "faq"]))["replanned"]
    assert not score(CASE, _got(["router", "records", "faq", "escalation"], handoff=True))["replanned"]


def test_case_that_must_not_replan_still_fails_on_a_deviation():
    case = {"id": "x", "expect": {"replanned": False}}
    assert score(case, _got(["router", "records", "faq"]))["replanned"]
    assert not score(case, _got(["router", "faq", "records"], replans=["faq->records"]))["replanned"]
