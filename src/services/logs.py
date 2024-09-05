from src.config import local_path
from datetime import datetime



def save_erros_log(message:str, command:bool):
    with open (f"{local_path}/logs.txt", '+a') as logs:
         logs.write(f"{str(datetime.now())}|{command}|{message}|\n\n")
    return True





