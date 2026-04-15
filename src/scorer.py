from datetime import datetime


def sentiment_to_score(sentiment: str) -> int:
    sentiment_map = {
        "positive": 2,
        "neutral": 1,
        "negative": 0,
    }
    return sentiment_map.get(sentiment.strip().lower(), 1)


def calculate_trend_score(records: list[dict]) -> dict:
    """
    Calculate a trend momentum score using mentions, sentiment, and recency.
    """
    if not records:
        return {
            "final_score": 0,
            "average_mentions": 0,
            "average_sentiment": 0,
            "average_recency": 0,
        }

    today = datetime(2026, 4, 15)

    mentions_scores = []
    sentiment_scores = []
    recency_scores = []

    for record in records:
        mentions = int(record["mentions_score"])
        mentions_scores.append(mentions)

        sentiment_score = sentiment_to_score(record["sentiment"])
        sentiment_scores.append(sentiment_score)

        record_date = datetime.strptime(record["date"], "%Y-%m-%d")
        days_old = (today - record_date).days

        if days_old <= 3:
            recency = 3
        elif days_old <= 7:
            recency = 2
        else:
            recency = 1

        recency_scores.append(recency)

    avg_mentions = sum(mentions_scores) / len(mentions_scores)
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    avg_recency = sum(recency_scores) / len(recency_scores)

    final_score = (avg_mentions * 0.6) + (avg_sentiment * 10) + (avg_recency * 5)

    return {
        "final_score": round(final_score, 2),
        "average_mentions": round(avg_mentions, 2),
        "average_sentiment": round(avg_sentiment, 2),
        "average_recency": round(avg_recency, 2),
    }