

class FileReader:

    def read_file_contents(self,filename):
        try:
          with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except PermissionError:
            print(f"Permission denied to read the file '{filename}'.")
        except Exception as e:
            print(f"An error occurred while reading the file '{filename}': {str(e)}")
