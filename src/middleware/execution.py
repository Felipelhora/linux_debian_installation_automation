from src.services.CommandsText import CommandsText
from src.services.ExecuteActions import ExecuteActions
from src.config import path_home, path_download
from src.view.Menu import Menu




def organize_command(command:str) ->str:
    command = command.replace("'", '"')
    command = command.replace("-|", "'")
    command = command.format(path_home=path_home, path_download=path_download)
    return command    
    


def execute_sudo_commands(sudo_commands:list, password:str, actions:object):
    if len(sudo_commands) == 0:
        return True
    for command in sudo_commands:
        prompt = organize_command(command)
        actions.prompt_commands(prompt=f"echo '{password}' | sudo -S {prompt}", invisible=False)


def execute_user_commands(user_commands:list, actions:object):
    if len(user_commands) == 0:
        return True
    for command in user_commands:
        prompt = organize_command(command)
        actions.prompt_commands(prompt=prompt, invisible=False)
    

def start(filter_actions:list) -> None:
    password = Menu().menu_main()
    actions = ExecuteActions()
    commandsText = CommandsText()
    commands  = commandsText.load_commands()
    # SEPARA POR GRUPOS
    for command_group in commands:
        # # VERIFICA SE ESTÁ NA LISTA DE INSTALAÇÃO
        if command_group in filter_actions:
           execute_sudo_commands(sudo_commands=commands[command_group]['sudo'], password=password, actions=actions)
           execute_user_commands(user_commands=commands[command_group]['user'], actions=actions)
          # EXECUTA COMANDO POR COMANDO
        #   for promt in commands[command_group]['sudo']:
              
        #         promt = promt.replace("'", '"')
        #         promt = promt.replace("-|", "'")
                
        #         promt = promt.format(path_home=path_home, path_download=path_download)
        #         print (promt)    
        #         output = actions.prompt_commands(prompt=promt, invisible=False)
    
    






