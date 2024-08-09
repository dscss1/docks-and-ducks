import sys
import os

try:
    import requests
    import json
    from mysql import connector
    import yaml
except ImportError as e:
    print(f"Error initialization Docks and ducks: Library {e.name} not found.")
    print("The requirements.txt file was created from the necessary libraries.")
    with open("requirements.txt", "x") as f:
        f.write("""
        requests
        PyYAML
        mysql-connector-python
        aioconsole
        aiohttp
        """)
    sys.exit()

class Main:
    def __init__(self):
        self.config = None

    def load_config(self, filepath):
        try:
            self.config = yaml.safe_load(open(filepath))
        except FileNotFoundError as e:
            print("Config file not found.")
            reponse = requests.get("https://raw.")
        return self.config