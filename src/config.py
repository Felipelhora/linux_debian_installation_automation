import os
import json
import subprocess








def get_route_path():
    process = subprocess.Popen('logname', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return f"/home/{stdout.strip()}/"
    
def load_pack_language():
    with open (f"{local_path}/languages.json") as languages:
         return json.loads(languages.read())
     
def env_load():
    envs = {}
    with open (f"{os.getcwd()}/.env") as env:
        for line in env.readlines():
            line = line.strip()
            if line[0] != '#':
                line = line.replace('#', '').strip()
                content = line.split('=')
                if len(content) == 2:
                    envs[content[0]] = content[1]
    return envs



path_home = get_route_path()
local_path = os.getcwd()
path_download = f'{local_path}/downloads/'

config = {
            "menu_options" : load_pack_language()[env_load()["language"]],
}