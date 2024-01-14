import json   

def readData(path):
    file: Final = open(path)
    json_data: Final = json.load(file)
    return json_data

def readList(path):
    json_data: Final = readData(path)
    json_list: Final = list(json_data)
    return json_list