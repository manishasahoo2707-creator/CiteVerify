import re
def decompose_atomic_claims(claim: str) -> list[str]:
    text = (claim or "").strip()
    if not text:
        return []
    parts = re.split(
        r"\b(?:and|while|whereas|although|however|which|that)\b|;|,",
        text,
        flags=re.IGNORECASE,
    )
    cleaned = [p.strip(" .") for p in parts if len(p.strip(" .")) >= 16]
    return cleaned[:4] if cleaned else [text]


def explore_claim(claim: str, paper: dict) -> dict:
    sub_claims = decompose_atomic_claims(claim)
    c_tokens = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", claim or "")}
    a_tokens = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", paper.get("abstract", ""))}

    overlap = (len(c_tokens & a_tokens) / len(c_tokens)) if c_tokens else 0.0
    neg_words = {"not", "never", "false", "refutes", "contradicts", "impossible", "denies", "hoax", "fake"}
    has_neg = bool(c_tokens & neg_words)

    overgeneralized = bool(
        re.search(
            r"\b(always|proves beyond doubt|100%|universal law|completely solved|definitively proven)\b",
            (claim or "").lower(),
        )
    )

    if overlap >= 0.20 and not has_neg:
        verdict = "Supported"
    elif overlap >= 0.20 and has_neg:
        verdict = "Contradicted"
    elif overlap >= 0.08:
        verdict = "Partially Supported"
    else:
        verdict = "Unsupported / Needs Escalation"

    return {
        "explorer": "Claim Explorer",
        "verdict": verdict,
        "concept_overlap": round(overlap, 2),
        "overgeneralization_flag": overgeneralized,
        "sub_claims": sub_claims,
        "note": (
            "Overgeneralization alert: claim uses absolute/certainty phrasing that goes beyond typical empirical qualification."
            if overgeneralized
            else "Atomic sub-claims parsed and compared against source abstract terminology."
        ),
    }