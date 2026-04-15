def predict_trend_label(score_data: dict) -> dict:
    """
    Convert a numeric trend score into a label and confidence estimate.
    """
    final_score = score_data["final_score"]

    if final_score >= 24:
        label = "Rising"
        confidence = 0.85
    elif final_score >= 18:
        label = "Peaking"
        confidence = 0.72
    else:
        label = "Fading"
        confidence = 0.81

    return {
        "label": label,
        "confidence": confidence,
    }