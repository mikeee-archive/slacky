from server import server
import yaml
import os

def getConfig():
    if os.path.isfile('config.yml'):
        with open("config.yml", 'r') as stream:
            try:
                configmap = yaml.load(stream)
                return configmap
            except yaml.YAMLError as exc:
                print(exc)
    return None

def _run():
    config = getConfig()
    if config != None:
        port = int(config['port'])
    else:
        port = 8000
    server.Run(port)

if __name__ == "__main__":
    _run()