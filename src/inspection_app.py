
import os
from src.config import local_path, config
import sys
import time


def verify_download_folder() -> None:
    if os.path.exists(f"{local_path}/downloads"):
       return True
    else:
        try:
            os.mkdir(f"{local_path}/downloads")
            return True
        except Exception as error:
            print ("salvar log")
            return False
    

def verify_env_file() -> None:
    ...

def verify_commands_file() -> None:
    if os.path.isfile(f"{local_path}/commands.json"):
       return True
    else:
        try:
            with open (f"{local_path}/commands.json", 'a+') as create_json:
                 create_json.write("{}")
                 return True
        except Exception as error:
            print ("salvar log")
            return False


def start_inspection_app():
    if  verify_download_folder() == False:
        print (config["text_language"]["menu"]["alert_create_download_path"])
        print ("\n\n")
        time.sleep(1)
        sys.exit()
    if verify_commands_file() == False:
        print (config["text_language"]["menu"]["alert_create_commands_json"])
        print ("\n\n")
        time.sleep(1)
        sys.exit()
