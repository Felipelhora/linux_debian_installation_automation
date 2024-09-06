
import subprocess
from src.config import config, path_download
import urllib.request
from src.services.logs import save_erros_log


class ExecuteActions:
    
    def __init__(self):
        ...
    def prompt_commands(self, prompt:str, invisible:bool) -> str:
        try:
            process = subprocess.Popen(prompt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print (config["menu_options"]["messages_execution"]["running"], '--->', prompt)
            while True:
                line = process.stdout.readline()
                if line:
                    if invisible !=True:
                        print(line, end='\r')
                elif process.poll() is not None:
                    break
            print (process.communicate(), end='\r')
            return True
        except Exception as error_:
            save_erros_log(message=error_, command=prompt)
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
        
        