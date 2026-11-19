def explore_retraction_status(paper: dict) -> dict:
    retracted = bool(paper.get("retracted", False))
    corrected = bool(paper.get("corrected", False))
    pub_type = paper.get("publication_type", "Peer-Reviewed")

    if retracted:
        alert_level = "CRITICAL"
        status = "Retracted Publication"
        message = "Flagged as RETRACTED; do not rely on this work as valid scientific support."
    elif corrected:
        alert_level = "WARNING"
        status = "Corrected / Erratum Issued"
        message = "Work has a published correction/erratum; verify exact section details."
    elif "Preprint" in pub_type:
        alert_level = "INFO"
        status = "Preprint (Unrefereed)"
        message = "Preprint detected; verify whether a peer-reviewed version has superseded it."
    else:
        alert_level = "OK"
        status = "Active / Indexed"
        message = "No retraction or erratum notice found for this reference."

    return {
        "explorer": "Retraction Explorer",
        "alert_level": alert_level,
        "status": status,
        "publication_type": pub_type,
        "message": message,
    }