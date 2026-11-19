def explore_evidence_strength(claim: str, paper: dict, concept_overlap: float) -> dict:
    base = int(paper.get("source_quality", 80))
    if paper.get("retracted"):
        base = 15
    elif "Preprint" in paper.get("publication_type", ""):
        base -= 5

    relevance_pct = int(min(1.0, concept_overlap * 1.5) * 100)
    score = int(max(10, min(98, round(0.65 * base + 0.35 * relevance_pct))))
    label = "Strong" if score >= 78 else ("Moderate" if score >= 52 else "Weak")

    factors = [
        f"Study Design: {paper.get('study_design', 'Theoretical / Conceptual Analysis')}",
        f"Sample & Method Scope: {paper.get('sample_notes', 'Evaluated against framework scope')}",
        f"Key Limitation: {paper.get('limitations', 'Requires full-text context verification')}",
        f"Claim Relevance: {relevance_pct}% concept alignment with '{paper.get('title', 'Matched Work')}'",
    ]

    return {
        "explorer": "Evidence Strength Explorer",
        "score": score,
        "label": label,
        "relevance_pct": relevance_pct,
        "factors": factors,
    }