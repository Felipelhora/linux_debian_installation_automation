import json
from src.config import local_path, system, version_system


class CommandsText:
    
    def __init__(self) -> None:
        self.commands = self.load_commands()

            
    ## read o que tem    
    def load_commands(self):
            with open(f"{local_path}/commands.json", 'r+') as json_commands:
                json_commands = json.loads(json_commands.read())
                if system == 'ubuntu':
                   return json_commands["ubuntu_debian"]  

                

    ## create
    
    
    
    ## deletar
    
    ## adicionar