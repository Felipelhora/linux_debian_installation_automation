import json
from src.config import local_path, system, version_system


class CommandsText:
    
    def __init__(self) -> None:
        self.commands = self.load_commands()

            
    ## ler o que tem    
    def load_commands(self):
            with open(f"{local_path}/commands.json", 'r+') as json_commands:
                json_commands = json.loads(json_commands.read())
                if system == 'ubuntu':
                   json_commands["ubuntu_debian"]  
                

    ## modificar
    
    
    
    ## deletar
    
    ## adicionar