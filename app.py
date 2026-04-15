from src.retriever import get_trend_records
from src.scorer import calculate_trend_score
from src.predictor import predict_trend_label
from src.explainer import generate_explanation


def main():
    print("Welcome to PopSignal AI")
    print("Predict whether a pop culture trend is Rising, Peaking, or Fading.")
    print()

    trend_name = input("Enter a trend name: ").strip()

    if not trend_name:
        print("Please enter a valid trend name.")
        return

    records = get_trend_records(trend_name)

    if not records:
        print(f"No data found for trend: {trend_name}")
        return

    score_data = calculate_trend_score(records)
    prediction = predict_trend_label(score_data)
    explanation = generate_explanation(
        trend_name=trend_name,
        score_data=score_data,
        prediction=prediction,
        record_count=len(records),
    )

    print("\n--- PopSignal Result ---")
    print(f"Trend: {trend_name}")
    print(f"Prediction: {prediction['label']}")
    print(f"Confidence: {prediction['confidence']}")
    print(f"Score: {score_data['final_score']}")
    print(f"Explanation: {explanation}")


if __name__ == "__main__":
    main()