def find_index(id:int, component:list):
    """
    This function finds the index of an item in a list of objects by its id.
    """
    index = next((i for i, item in enumerate(component) if item.id == id), None)
    return index