from src.middleware.execution import start


start(['system'])





'''import subprocess
import os
import time
import json




local_path = os.getcwd()
with open(f"{local_path}/commands.json", 'r+') as json_commands:
    json_commands = json.loads(json_commands.read())
    


# comando = f"python -m unittest {local_path}/src/TestCalculadoraDiferente.py"
# saida = subprocess.check_output(comando, shell=True)


# print(saida.decode('utf-8'))

# time.sleep(3)'''

# from src.view.Menu import Menu


# Menu().menu_main()


# from services.CommandsText import CommandsText



# ola = CommandsText()


# commands = ola.load_commands()

# for command_group in commands:
#     for command in commands[command_group]:
#         print (command)
