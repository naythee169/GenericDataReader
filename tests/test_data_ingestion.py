import os
import pytest
from app.data_ingestion import DataIngestion

@pytest.fixture
def ingestor():
    return DataIngestion(data_dir="data_files")

def test_read_csv(ingestor):
    data = ingestor.read_csv()
    # Expect a list (even if empty) and file_type marked as 'csv'
    assert isinstance(data, list)
    if data:
        assert data[0].get("file_type") == "csv"

def test_read_json(ingestor):
    data = ingestor.read_json()
    assert isinstance(data, list)
    if data:
        assert data[0].get("file_type") == "json"

def test_read_pptx(ingestor):
    data = ingestor.read_pptx()
    assert isinstance(data, list)
    if data:
        assert data[0].get("file_type") == "pptx"

def test_read_pdf(ingestor):
    data = ingestor.read_pdf()
    assert isinstance(data, list)
    if data:
        assert data[0].get("file_type") == "pdf"