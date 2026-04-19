from src.retriever import get_trend_records
from src.scorer import calculate_trend_score
from src.predictor import predict_trend_label


def run_evaluation():
    test_trends = [
        "doechii",
        "labubu",
        "balletcore",
        "mob wife aesthetic",
        "brat aesthetic",
    ]

    print("Running PopSignal AI evaluation...\n")

    for trend in test_trends:
        records = get_trend_records(trend)
        score_data = calculate_trend_score(records)
        prediction = predict_trend_label(score_data)

        print(f"Trend: {trend}")
        print(f"Prediction: {prediction['label']}")
        print(f"Confidence: {prediction['confidence']}")
        print(f"Score: {score_data['final_score']}")
        print("-" * 40)


if __name__ == "__main__":
    run_evaluation()

correct_predictions = 0
total = len(test_trends)

# (pretend expected labels)
expected = {
    "doechii": "Rising",
    "labubu": "Rising",
    "mob wife aesthetic": "Fading"
}

for trend in test_trends:
    ...
    if trend in expected and prediction["label"] == expected[trend]:
        correct_predictions += 1

print(f"\nAccuracy: {correct_predictions}/{total}")