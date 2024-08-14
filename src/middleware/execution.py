from src.services.CommandsText import CommandsText
from src.services.ExecuteActions import ExecuteActions
from src.config import path_home, path_download





def start(filter_actions:list) -> None:
    actions = ExecuteActions()
    commandsText = CommandsText()
    commands  = commandsText.load_commands()
    # SEPARA POR GRUPOS
    for command_group in commands:
        # VERIFICA SE ESTÁ NA LISTA DE INSTALAÇÃO
        if command_group in filter_actions:
           # EXECUTA COMANDO POR COMANDO
            for promt in commands[command_group]:
                promt = promt.replace("'", '"')
                promt = promt.replace("-|", "'")
                
                promt = promt.format(path_home=path_home, path_download=path_download)
                print (promt)    
                output = actions.prompt_commands(prompt=promt, invisible=False)
    
    






