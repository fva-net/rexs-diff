def check_unique_ids(components: list):
    """
    This function checks if there are any non unique IDs in the components/relations lists.\n
    Input: 
        components: list of components or relations.\n
    Output: 
        True/False: True, if all IDs are unique; False, if there are non unique IDs.\n
    """
    # Check if there are any double IDs 

    # Initialize lists for already ssen IDs and non unique IDs
    ids = [] 
    doubles = []

    # Go through every component and add its ID to doubles if it is already in ids or to ids if it is not
    for element in components:
        if element.id in ids:
            doubles.append(element.id)
        
        else:
            ids.append(element.id)
    
    # Return True if there are no doubles and False if there are 
    if doubles != []:
        return False      
    else:
        return True
    
    