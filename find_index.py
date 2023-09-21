def find_index(id: int, components: list):
    """
    This function finds the index of an item in a list of objects by its ID.\n
    Input: 
        - id: ID of the item
        - components: list of components or relations\n
    Output:
        - index of the item in the list

    """
    index = next((i for i, item in enumerate(components) if item.id == id), None)
    return index