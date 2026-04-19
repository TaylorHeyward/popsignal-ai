from src.retriever import get_trend_records
from src.scorer import calculate_trend_score
from src.predictor import predict_trend_label


def test_retriever_finds_existing_trend():
    records = get_trend_records("doechii")
    assert len(records) > 0


def test_retriever_returns_empty_for_unknown_trend():
    records = get_trend_records("something totally fake")
    assert records == []


def test_scorer_returns_zero_for_empty_records():
    score_data = calculate_trend_score([])
    assert score_data["final_score"] == 0


def test_predictor_returns_valid_label():
    score_data = {"final_score": 25}
    prediction = predict_trend_label(score_data)
    assert prediction["label"] in ["Rising", "Peaking", "Fading"]


def test_doechii_is_classified_as_rising():
    records = get_trend_records("doechii")
    score_data = calculate_trend_score(records)
    prediction = predict_trend_label(score_data)
    assert prediction["label"] == "Rising"


def test_mob_wife_aesthetic_is_not_rising():
    records = get_trend_records("mob wife aesthetic")
    score_data = calculate_trend_score(records)
    prediction = predict_trend_label(score_data)
    assert prediction["label"] in ["Peaking", "Fading"]