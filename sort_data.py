def sort_data(components:list):
    """
    This function Sorts the data according to their ids.
    Input:\n
        - list: list of components or relations \n
    Output:\n
        - list: sorted list of components or relations
    """
    sorted_list = sorted(components, key=lambda x: x.id)

    return sorted_list