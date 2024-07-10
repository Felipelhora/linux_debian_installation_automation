import json
from src.config import local_path


class Commands:
    
    def __init__(self) -> None:
        self.commands = self.load_commands()
        
    ## ler o que tem        
    def load_commands(self):
        try:
            with open(f"{local_path}/commands.json", 'r+') as json_commands:
                return json.loads(json_commands.read())
        except:
            return None
    ## modificar
    
    ## deletar
    
    ## adicionar