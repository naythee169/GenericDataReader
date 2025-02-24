import pytest
from app.data_processor import DataProcessor

def test_clean_record():
    sample = {"name": "  John Doe ", "age": 30}
    processor = DataProcessor([])
    cleaned = processor.clean_record(sample)
    assert cleaned["name"] == "John Doe"
    assert cleaned["age"] == 30

def test_merge_data():
    raw = [{"name": " Alice ", "file_type": "csv"}, {"name": " Bob ", "file_type": "json"}]
    processor = DataProcessor(raw)
    merged = processor.merge_data()
    # Check that strings have been trimmed
    assert merged[0]["name"] == "Alice"
    assert merged[1]["name"] == "Bob"