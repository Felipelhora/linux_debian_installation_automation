from src.services.CommandsText import CommandsText
from src.services.ExecuteActions import ExecuteActions
from src.config import path_home, path_download
from src.view.Menu import Menu




def execute_sudo_commands(sudo_commands:list, password:str, actions):
    if len(sudo_commands) == 0:
        return True
    for promt in sudo_commands:
        actions.prompt_commands(prompt=f"echo '{password}' | sudo -S {promt}", invisible=False)


def execute_user_commands(user_commands:list):
    if len(user_commands) == 0:
        return True
    for command in user_commands:
        print (command)
    

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
           execute_user_commands(user_commands=commands[command_group]['user'])
          # EXECUTA COMANDO POR COMANDO
        #   for promt in commands[command_group]['sudo']:
              
        #         promt = promt.replace("'", '"')
        #         promt = promt.replace("-|", "'")
                
        #         promt = promt.format(path_home=path_home, path_download=path_download)
        #         print (promt)    
        #         output = actions.prompt_commands(prompt=promt, invisible=False)
    
    






