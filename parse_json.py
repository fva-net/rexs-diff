import json

def parse_json(filename: str):
    """
    This function parses the json file and returns the data as a dictionary.\n 
    Input:
        filename: path to the json file\n
    Output:
        data: dictionary with the data from the json file\n
    """
    with open(filename, "r", encoding="utf-8-sig") as file:
        txt = file.read()
    data = json.loads(txt)
    return(data)
