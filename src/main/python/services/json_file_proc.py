import json

class JsonFileProcessor:

    def read_file_contents(self,filename):
        try:
          with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except PermissionError:
            print(f"Permission denied to read the file '{filename}'.")
        except Exception as e:
            print(f"An error occurred while reading the file '{filename}': {str(e)}")

    def write_to_file(self,filename, content):
        try:
           with open(filename, 'w') as file:
                json.dump(content, file)
        except PermissionError:
            print(f"Permission denied to write to the file '{filename}'.")
        except Exception as e:
            print(f"An error occurred while writing to the file '{filename}': {str(e)}")
