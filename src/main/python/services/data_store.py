from services.json_file_proc import JsonFileProcessor

class DataStore:
    def __init__(self):
      self.json_file_processor = JsonFileProcessor()


    def find_by_key(self, key):
        data = self.json_file_processor.read_file_contents("datastore\data.json")
        if data and key in data:
            value = data[key]
            return value if isinstance(value, list) else [value]
        else:
            return []