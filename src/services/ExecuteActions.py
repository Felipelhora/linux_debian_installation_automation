
import subprocess
from src.config import config

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
                        print(line, end='')
                elif process.poll() is not None:
                    break
            print (process.communicate())
            return True
        except:
            return False
    
    def wget_commands(self, prompt):
        output =  self.prompt_commands(prompt=f'wget {prompt}')
        return output
        
    
    def curl_commands(self, prompt):
        ...
        
    def dpkg_commands(self, prompt):
        ...
        
    def snap_commands(self, prompt):
        ...
        
        