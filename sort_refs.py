def sort_refs(relations: list):
    """
    This function sorts the refs of the relations alphabetically. \n
    Input: 
        - relations: list of relations. \n
    Output:
        - list of relations with sorted refs.
    """
    for rel in relations:
        rel.refs.sort(key=lambda x: x.role)
    return relations