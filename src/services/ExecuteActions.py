
import subprocess
from src.config import config, path_download
import urllib.request
from src.services.logs import save_log, save_console_history


class ExecuteActions:
    
    def __init__(self):
        ...
    def prompt_commands(self, prompt:str, password:str=None, invisible:bool=True, input_command:str=None) -> str:
        try:
            process = subprocess.Popen(prompt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if password:
                visible_command = prompt.replace(password, ' ********* ')
            else:
                visible_command = prompt
            print (config["text_language"]["messages_execution"]["running"], '--->', visible_command)
            while True:
                line = process.stdout.readline()
                save_console_history(status=True, command=visible_command, message_additional=line.strip())
                if line:
                    if invisible !=True:
                        print(line, end='\r')
                elif process.poll() is not None:
                    break
            print (process.communicate(), end='\r')
            save_log(status=True, command=visible_command)
            print('\n\n')
            return True
        except Exception as error_:
            save_log(status=False, message_additional=error_, command=visible_command)
            return False
    
    def download_packges(self, url:str, file_name:str):
        try:
            with urllib.request.urlopen(url) as response:
                with open(f"{path_download}/{file_name}", 'wb') as out_file:
                    data = response.read()
                    out_file.write(data)
        except Exception as error_:
            save_erros_log(message=error_, command=f"download->{url}")
            return False

    
    def curl_commands(self, prompt):
        ...
        
    def dpkg_commands(self, prompt):
        ...
        
    def snap_commands(self, prompt):
        ...
        
        