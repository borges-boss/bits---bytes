import json

class JsonFileProcessor:

    def read_file_contents(self,filename):
        try:
          with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Arquivo '{filename}' nao encontrado.")
        except PermissionError:
            print(f"Permissao negada para ler o arquivo '{filename}'.")
        except Exception as e:
            print(f"Um erro ocorreu ao tentar ler o arquivo '{filename}': {str(e)}")

    def write_to_file(self,filename, content):
        try:
           with open(filename, 'w') as file:
                json.dump(content, file)
        except PermissionError:
            print(f"Permissao negada para ler o arquivo '{filename}'.")
        except Exception as e:
            print(f"Um erro ocorreu ao tentar ler o arquivo '{filename}': {str(e)}")
