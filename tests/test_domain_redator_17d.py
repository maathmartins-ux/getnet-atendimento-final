"""official-08 colou "Today…" a um total de 7 dias ("In the same period there were
6 approved sales") e, noutra rodada, disse que não dava para saber se o problema do T1988B tinha a ver com as recusas,
quando os registros mostram que as 2 recusas foram no T1988A; e official-01 (Clássica × Smart) fechou com "The
sources don't give a full side-by-side comparison" depois de comparar. As regras ficam nos prompts do domínio."""
from __future__ import annotations

import re
from pathlib import Path

PROMPTS = Path(__file__).resolve().parents[1] / "src" / "app" / "domain" / "challenge_prompts"


def _flat(name: str) -> str:
    return re.sub(r"\s+", " ", (PROMPTS / name).read_text("utf-8"))


def test_records_names_the_period_of_each_total():
    md = _flat("records.md")
    assert "Cada total ou contagem diz o seu período por extenso" in md
    assert 'Nunca "no mesmo período"' in md


def test_records_answers_a_relation_question_by_comparing_the_records():
    md = _flat("records.md")
    assert "Pergunta de relação entre registros" in md and "comparando os registros" in md
    assert '"Não dá para concluir" vale só para a causa que nenhum campo traz' in md


def test_records_examples_carry_no_number_from_the_data():
    """Exemplo do prompt com número de verdade vira número sem base na resposta (o juiz o reprova)."""
    md = _flat("records.md")
    assert "995" not in md and "T1988" not in md


def test_faq_compares_side_by_side_and_never_closes_with_the_gap():
    md = _flat("faq.md")
    assert "nunca abra nem feche com o que as fontes não dizem" in md
    assert "responda lado a lado com o que os trechos trazem de cada um" in md
    assert 'a comparação é a sua resposta' in md
