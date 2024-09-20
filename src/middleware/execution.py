from src.services.CommandsText import CommandsText
from src.services.ExecuteActions import ExecuteActions
from src.config import path_home, path_download
from src.view.Menu import Menu
import os
from src.config import local_path
from src.inspection_app import start_inspection_app
import sys
import json

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
            actions.prompt_commands(prompt=f"echo '{password}' | sudo -S {prompt}", invisible=False, password=password)


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




def execution_commands(filter_actions:list) -> None:
    password = Menu().get_password()
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
    

def get_system():
    list_systems = []
    with open (f"{local_path}/commands_teste.json") as commands:
        systems =  json.loads(commands.read())
        for index, system in enumerate(systems):
            option_number = str(index + 1)
            list_systems.append(f"{option_number} - {system.strip()}")
    menu_answer = Menu().menu_create_commands(list_systems)
    return list_systems[(menu_answer -1)].split('-')[1].strip()
    
            # ...           
            # for service in systems[system]:
            #     print (service)

def get_services_to_run(system:str)->list:
    list_services = []
    with open (f"{local_path}/commands_teste.json") as commands:
        systems =  json.loads(commands.read())
        for index, service in enumerate(systems[system]):
            option_number = str(index + 1)
            list_services.append(service)
    menu_answer = Menu().main(list_services)
    print(menu_answer)


def start() -> None:
    start_inspection_app()
    while True:
        menu_answer = Menu().menu_main()
        if menu_answer == 1:
            execution_commands(['system','python', 'php', 'javascript','snap', 'packages' 'rust'])
        elif  menu_answer == 2:
            system = get_system()
            get_services_to_run(system=system)

        elif  menu_answer == 3:
            ...
        elif  menu_answer == 4:
            sys.exit()






