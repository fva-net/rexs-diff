def sort_refs(relations: list, role_ordering: list):
    """
    This function sorts the refs in the relations according to the role_ordering defined in the main.py file. \n
    Input: 
        - relations: list of relations
        - role_ordering: list of possible roles in the relations \n
    Output:
        - list of relations with sorted refs
    """
    for rel in relations:
        rel.refs.sort(key=lambda x: role_ordering.index(x.role))
    return relations