def check_unique_ids(list: list, type: str ):
    """"
    Check if there are any double IDs in the components/relations lists.\n
    Can also be used for the relations list to ckeck if there are any double IDs in the relations.
    Input: 
        - list: list of components or relations\n
        - type: string, either "component" or "relation"
    """
    # Check if there are any double IDs 
    ids = []
    doubles = []
    for element in list:
        if element.id in ids:
            doubles.append(element.id)
        
        else:
            ids.append(element.id)
    if doubles != []:
        return False, doubles       
    else:
        return True, doubles
    
    