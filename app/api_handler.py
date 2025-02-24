from flask import Blueprint, jsonify, request
from app.data_ingestion import DataIngestion
from app.data_processor import DataProcessor

api = Blueprint("api", __name__)

# Instantiate data ingestion and process the unified dataset on startup
ingestor = DataIngestion()
raw_data = ingestor.read_all()
processor = DataProcessor(raw_data)
unified_data = processor.merge_data()

@api.route("/api/data", methods=["GET"])
def get_all_data():
    return jsonify(unified_data)

@api.route("/api/data/<string:file_type>", methods=["GET"])
def get_data_by_type(file_type):
    # Read fresh data for the requested file type
    file_type_data = ingestor.read_by_type(file_type.lower())
    # Process/clean the data
    processor = DataProcessor(file_type_data)
    data = processor.merge_data()
    return jsonify(data)