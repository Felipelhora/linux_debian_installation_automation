from src.services.CommandsText import CommandsText
from src.services.ExecuteActions import ExecuteActions






def start(filter_actions:list) -> None:
    actions = ExecuteActions()
    commandsText = CommandsText()
    commands  = commandsText.load_commands()
    # SEPARA POR GRUPOS
    for command_group in commands:
        # VERIFICA SE ESTÁ NA LISTA DE INSTALAÇÃO
        if command_group in filter_actions:
           # EXECUTA COMANDO POR COMANDO
            for promt in command_group:
                output = actions.prompt_commands(prompt=promt, invisible=False)
    
    






