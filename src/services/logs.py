from src.config import local_path
from datetime import datetime



def save_log(status:bool, command:str, message_additional:str=None):
     if message_additional:
         ...
     else:
         message_additional == ''
     with open (f"{local_path}/logs.txt", '+a') as logs:
         logs.write(f"{str(datetime.now())}|{str(status)}|{command}|{message_additional}|\n")
     return True



def save_console_history(status:bool, command:str, message_additional:str=None):
     if message_additional:
         ...
     else:
         message_additional == ''
     with open (f"{local_path}/history_console.txt", '+a') as logs:
         logs.write(f"{str(status)}|{str(datetime.now())}|{command}|{message_additional}|\n")
     return True



