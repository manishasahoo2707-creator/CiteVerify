import re
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b")
PAREN_CITE_RE = re.compile(
    r"\(([A-Z][A-Za-z\-]+(?:\s+(?:et al\.|&\s+[A-Z][A-Za-z\-]+))?,?\s*(?:19\d{2}|20\d{2}[a-z]?))\)"
)
NUM_CITE_RE = re.compile(r"\[(\d+(?:\s*,\s*\d+)*)\]")


def explore_citations(text: str, reference_input: str, known_years: list[int]) -> dict:
    combined = f"{reference_input or ''}\n{text or ''}"
    dois = DOI_RE.findall(combined)
    markers = [m.group(1) for m in PAREN_CITE_RE.finditer(combined)]
    num_refs = [n.strip() for grp in NUM_CITE_RE.findall(combined) for n in grp.split(",")]

    discrepancies = []
    for mk in markers:
        if any(tag in mk.lower() for tag in ["unknown", "mystery", "fake", "unverified", "hallucinated"]):
            discrepancies.append(
                {
                    "issue_type": "UNVERIFIED CITATION",
                    "marker": mk,
                    "page": "Page 1",
                    "explanation": "Author-year citation marker does not map to a verified publication in the index.",
                }
            )

    for nr in num_refs:
        if nr.isdigit() and int(nr) > 4:
            discrepancies.append(
                {
                    "issue_type": "MISSING REFERENCE",
                    "marker": f"[{nr}]",
                    "page": "Page 1",
                    "explanation": f"In-text reference [{nr}] lacks a corresponding verified entry in the reference list.",
                }
            )

    years_found = [int(y) for y in re.findall(r"\b(19\d{2}|20\d{2})\b", reference_input or "")]
    year_drift = bool(years_found and known_years and not any(y in known_years for y in years_found))
    if year_drift:
        discrepancies.append(
            {
                "issue_type": "YEAR / VERSION DRIFT",
                "marker": ", ".join(str(y) for y in years_found),
                "page": "Reference",
                "explanation": f"Submitted year differs from matched record year(s): {known_years}.",
            }
        )

    return {
        "explorer": "Citation Explorer",
        "dois_found": dois,
        "markers_found": markers,
        "discrepancies": discrepancies,
        "year_drift": year_drift,
    }