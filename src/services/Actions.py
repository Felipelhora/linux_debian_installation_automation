
import subprocess

class Actions:
    
    def __init__(self):
        ...
        
    def prompt_commands(self, prompt):
        output = subprocess.check_output(prompt, shell=True)
        return output.decode('utf-8')
    
    def wget_commands(self, prompt):
        ...
    
    def curl_commands(self, prompt):
        ...
        
    def dpkg_commands(self, prompt):
        ...
        
    def snap_commands(self, prompt):
        ...
        
        