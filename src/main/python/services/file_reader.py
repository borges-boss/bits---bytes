

class FileReader:

    def read_file_contents(self,filename):
        try:
          with open(filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except PermissionError:
            print(f"Permissao negada para ler o arquivo '{filename}'.")
        except Exception as e:
            print(f"Um erro ocorreu ao tentar ler o arquivo '{filename}': {str(e)}")
