import json

def parse_json(filename:str):
    """
    This function parses the json file and returns the data as a dictionary.
    """
    with open(filename, "r", encoding="utf-8-sig") as file:
        txt = file.read()
    data = json.loads(txt)
    return(data)
