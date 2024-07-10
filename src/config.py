import os
import json


local_path = os.getcwd()





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



config = {
            "menu_options" : load_pack_language()[env_load()["language"]]
}