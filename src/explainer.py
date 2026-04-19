def generate_explanation(trend_name, score_data, prediction, record_count):
    label = prediction["label"]
    score = score_data["final_score"]
    avg_mentions = score_data["average_mentions"]
    avg_sentiment = score_data["average_sentiment"]
    avg_recency = score_data["average_recency"]

    if avg_recency >= 2.5 and avg_mentions >= 8:
        momentum_note = "Recent signals show strong acceleration in attention."
    elif avg_recency < 2 and avg_sentiment < 1.5:
        momentum_note = "Signals suggest declining interest and weaker sentiment."
    else:
        momentum_note = "Momentum appears stable with mixed signals."

    return (
        f"'{trend_name}' is classified as {label.lower()} based on {record_count} retrieved signals. "
        f"It achieved a momentum score of {score}. "
        f"Average mentions ({avg_mentions}) and sentiment ({avg_sentiment}) indicate overall engagement levels, "
        f"while recency ({avg_recency}) reflects how current the trend is. "
        f"{momentum_note}"
    )