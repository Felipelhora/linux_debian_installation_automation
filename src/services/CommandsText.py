import json
from src.config import local_path


class CommandsText:
    
    def __init__(self) -> None:
        self.commands = self.load_commands()
        
    ## ler o que tem    
    def load_commands(self):
            with open(f"{local_path}/commands.json", 'r+') as json_commands:
                return json.loads(json_commands.read())

    ## modificar
    
    
    
    ## deletar
    
    ## adicionar