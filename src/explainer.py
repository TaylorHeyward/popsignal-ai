def generate_explanation(trend_name: str, score_data: dict, prediction: dict, record_count: int) -> str:
    """
    Create a plain-English explanation of the prediction.
    """
    label = prediction["label"]
    score = score_data["final_score"]
    avg_mentions = score_data["average_mentions"]
    avg_sentiment = score_data["average_sentiment"]
    avg_recency = score_data["average_recency"]

    return (
        f"PopSignal AI predicts that '{trend_name}' is {label.lower()}. "
        f"This prediction is based on {record_count} retrieved trend signals. "
        f"The trend earned a momentum score of {score}, with an average mentions score of {avg_mentions}, "
        f"an average sentiment score of {avg_sentiment}, and an average recency score of {avg_recency}. "
        f"These signals suggest the trend's current cultural momentum is best classified as {label.lower()}."
    )