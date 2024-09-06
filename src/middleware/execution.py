from src.services.CommandsText import CommandsText
from src.services.ExecuteActions import ExecuteActions
from src.config import path_home, path_download
from src.view.Menu import Menu
import os



def organize_command(command:str, type_command:str, sudo:bool) ->str:
    type_command = type_command.replace('_', ' ')
    command = command.replace("'", '"')
    command = command.replace("-|", "'")
    command = command.replace("||", '"')
    command = command.format(path_home=path_home, path_download=path_download)
    command = f"{type_command} {command}"
    if type_command != 'snap' and sudo == True:
        command = f"{command} -y"
    return command    
    


def execute_sudo_commands(sudo_commands:dict, password:str, actions:object):
    if len(sudo_commands) == 0:
        return True
    for type_commands in sudo_commands:
        for command in sudo_commands[type_commands]:
            prompt = organize_command(command=command, type_command=type_commands, sudo=True)            
            actions.prompt_commands(prompt=f"echo '{password}' | sudo -S {prompt}", invisible=False)


def execute_simple_commands(simple_commands:list, actions:object):
    if len(simple_commands) == 0:
        return True
    for type_commands in simple_commands:
        for command in simple_commands[type_commands]:
            prompt = organize_command(command=command, type_command=type_commands, sudo=False)            
            actions.prompt_commands(prompt=prompt, invisible=False)

def execute_download_commads(download_instrutions:list, actions:object):
    if len(download_instrutions) == 0:
        return True
    for command in download_instrutions:
        actions.download_packges(url=command[0], file_name=command[1])

def execute_install_packages(password:str, actions:object):
    files = os.listdir(path_download)
    for file in files:
        if '.deb' in file:
            actions.prompt_commands(prompt=f"echo '{password}' | sudo -S dpkg -i {path_download}/{file}", invisible=False)  


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
           execute_simple_commands(simple_commands=commands[command_group]['simple'], actions=actions)
           execute_download_commads(download_instrutions=commands[command_group]['download'], actions=actions)
           execute_install_packages(password=password, actions=actions)
          # EXECUTA COMANDO POR COMANDO
        #   for promt in commands[command_group]['sudo']:
              
        #         promt = promt.replace("'", '"')
        #         promt = promt.replace("-|", "'")
                
        #         promt = promt.format(path_home=path_home, path_download=path_download)
        #         print (promt)    
        #         output = actions.prompt_commands(prompt=promt, invisible=False)
    
    






