import yaml
import json

class ReadConfigs:
    def __init__(self):
        pass

    def read_yaml(self, file_path):
        file = open(file_path)
        data = yaml.safe_load(file)
        return data
    
    def read_json(self, file_path):
        file = open(file_path)
        data = json.load(file_path)
        return data