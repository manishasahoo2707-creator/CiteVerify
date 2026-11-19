def explore_network_and_timeline() -> dict:
    nodes = [
        {"id": "iit-2004", "label": "Tononi (2004)\nIIT", "x": 105, "y": 135},
        {"id": "gwt-2004", "label": "Baars (2004)\nGWT", "x": 275, "y": 65},
        {"id": "orchor-2014", "label": "Hameroff & Penrose (2014)\nOrch OR", "x": 275, "y": 200},
        {"id": "iit-2025", "label": "Tononi & Boly (2025)\nConsciousness-First", "x": 455, "y": 135},
    ]
    edges = [
        {"from": "gwt-2004", "to": "iit-2004"},
        {"from": "orchor-2014", "to": "gwt-2004"},
        {"from": "iit-2025", "to": "iit-2004"},
        {"from": "iit-2025", "to": "gwt-2004"},
    ]
    timeline = [
        {
            "year": 2004,
            "title": "Integration & Global Workspace Foundations",
            "detail": "Information integration across differentiated states and global workspace broadcasting emerge as foundational models.",
        },
        {
            "year": 2014,
            "title": "Quantum Microtubule Review (Orch OR)",
            "detail": "Quantum coherent microtubule mechanisms are reviewed alongside active debate on biological feasibility.",
        },
        {
            "year": 2025,
            "title": "Consciousness-First Causal Structure Framing",
            "detail": "Emphasis shifts toward consciousness-first formulations and intrinsic cause-effect structures.",
        },
    ]
    return {"explorer": "Graph Explorer", "nodes": nodes, "edges": edges, "timeline": timeline}