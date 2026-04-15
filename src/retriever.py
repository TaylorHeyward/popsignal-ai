import csv
from pathlib import Path


DATA_PATH = Path("data/trend_signals.csv")


def get_trend_records(trend_name: str) -> list[dict]:
    """
    Return all rows from the dataset that match the given trend name.
    """
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    matches = []
    normalized_query = trend_name.strip().lower()

    with DATA_PATH.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["trend"].strip().lower() == normalized_query:
                matches.append(row)

    return matches