# Unified Data Ingestion & API App

## Overview
This project is a local Flask application that:
- Reads data from CSV, PPTX, JSON, and PDF files.
- Cleans and merges the data into a unified format.
- Provides two REST API endpoints:
    - `GET /api/data` returns the full merged dataset in JSON.
    - `GET /api/data/<file_type>` returns data only from the specified file type.
- Displays the unified dataset as both a table and a bar chart on a simple frontend.

## Directory Structure
project-root/ ├── app/ │ ├── init.py │ ├── main.py │ ├── data_ingestion.py │ ├── data_processor.py │ ├── api_handler.py │ └── visualization.py ├── data_files/ │ ├── sample.csv │ ├── sample.pptx │ ├── sample.json │ └── sample.pdf ├── tests/ │ ├── init.py │ ├── test_data_ingestion.py │ ├── test_data_processor.py │ └── test_api_handler.py ├── requirements.txt └── README.md


## Setup and Testing Instructions

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/naythee169/GenericDataReader.git>
   cd GenericDataReader
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   python -m app.main

   # to run the tests, use
   pytest tests/

## Access Data Through API
1. you can use a tool like cURL to interact with the API
   For example, to retrieve all data using cURL
   ```bash
   curl http://127.0.0.1:5000/api/data

## Challenges faced

1. some version requirements were very specific. For example,
   the Werkzeug and numpy versions. I had to search stackexchange to solve this issue
2. The Json file data was initially not in the format I assumed it was in and
3. Initially, Matplotlib was using a GUI backend, which wasn't allowed when rendering images in a Flask route running outside the main thread. The solution was to switch to a non-interactive backend (such as "Agg") that doesn’t require a GUI.
4. Had to figure out how to make the app automatically open up a browser page when it was run

**AI was used to assist in certain parts of the code and with debugging

