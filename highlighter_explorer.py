import re


def explore_sentence_highlights(text: str, claim: str) -> list[dict]:
    claim_words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", claim or "")}
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", (text or "").strip()) if len(s.strip()) > 12]

    results = []
    for s in sentences[:20]:
        s_words = {w.lower() for w in re.findall(r"[A-Za-z]{4,}", s)}
        low = s.lower()
        if any(k in low for k in ["limitation", "debate", "contradict", "unverified", "missing", "[9]", "[7]", "fake"]):
            tag = "contradict_or_flag"
        elif (claim_words & s_words) or any(k in low for k in ["integrat", "consciousness", "workspace", "cause-effect"]):
            tag = "support"
        else:
            tag = "context"
        results.append({"text": s, "tag": tag})
    return results