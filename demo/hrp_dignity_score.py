def dignity_score(decision):
    score = 0

    if decision.get("human_context"):
        score += 2
    if decision.get("stakeholder_impact"):
        score += 2
    if decision.get("long_term_view"):
        score += 1
    if decision.get("efficiency_only"):
        score -= 2
    if decision.get("ignores_vulnerability"):
        score -= 2

    if score >= 3:
        return "High dignity"
    elif score >= 0:
        return "Moderate dignity"
    else:
        return "Low dignity"
