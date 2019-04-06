import os
import yaml
from server import server
import sys

def getConfig():
    if os.path.isfile('config.yml'):
        with open("config.yml", 'r') as stream:
            try:
                configmap = yaml.safe_load(stream)
                return configmap
            except yaml.YAMLError as exc:
                print(exc)
    return None

def _run():
    config = getConfig()
    if config != None:
        port = int(config['port'])
        slack_token = config['slack_token']
        api_key = config['api_key']
    else:
        sys.exit('no config specified')
    
    server.Run(port, slack_token, api_key)

if __name__ == "__main__":
    _run()
