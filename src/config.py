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

def get_release():
    process = subprocess.Popen('lsb_release -a', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    if "ubuntu" in stdout.lower():
        return "ubuntu"
    if "debian" in stdout.lower():
        return "debian"
    
def get_version():
    process = subprocess.Popen('cat /etc/issue', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    if "22.04" in stdout.lower():
        return "22.04"
    if "24.04" in stdout.lower():
        return "24.04"


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
path_download = f'{local_path}/downloads'
system = get_release()
version_system = get_version()

config = {
            "menu_options" : load_pack_language()[env_load()["language"]],
            
}