def sort_data(components: list):
    """
    This function sorts the data according to their IDs.\n
    Input:\n
        - list of components or relations. \n
    Output:\n
        - sorted list of components or relations.
    """
    sorted_list = sorted(components, key=lambda x: x.id)

    return sorted_list