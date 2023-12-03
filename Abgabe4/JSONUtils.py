import json   

def readData(path):
    file = open(path)
    json_data = json.load(file)
    return json_data

def readList(path):
    json_data = readData(path)
    json_list = list(json_data)
    return json_list