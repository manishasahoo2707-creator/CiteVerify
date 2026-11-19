def explore_debate_sides(claim: str, corpus: list[dict]) -> dict:
    q = (claim or "").lower()
    supporting = []
    opposing_or_alt = []

    for p in corpus:
        entry = {
            "paper": f"{p['title']} ({p['year']})",
            "doi": p.get("doi", ""),
            "summary": p["abstract"],
            "caveat": p["limitations"],
        }
        if p.get("stance") == "agree_integration":
            supporting.append(entry)
        else:
            opposing_or_alt.append(entry)

    if any(k in q for k in ["quantum", "microtubule", "orch or"]):
        supporting, opposing_or_alt = opposing_or_alt, supporting

    return {
        "explorer": "Debate Explorer",
        "supporting": supporting[:2],
        "opposing_or_alternative": opposing_or_alt[:2],
    }