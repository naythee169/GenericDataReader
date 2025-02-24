class DataProcessor:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def clean_record(self, record):
        # For demonstration, trim string fields
        cleaned = {}
        for key, value in record.items():
            if isinstance(value, str):
                cleaned[key] = value.strip()
            else:
                cleaned[key] = value
        return cleaned

    def process_data(self):
        cleaned_data = []
        for record in self.raw_data:
            cleaned = self.clean_record(record)
            cleaned_data.append(cleaned)
        return cleaned_data

    def merge_data(self):
        # In this demo, merging is simply processing the list of records.
        return self.process_data()