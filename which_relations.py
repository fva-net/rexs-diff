def which_relations(comp_id, relations):
    """
    This function returns the relations of a component.
    """
    # Get the relations of the component
    relations_of_comp = []
    for relation in relations:
        for i in range(len(relation.refs)):
            if comp_id == relation.refs[i].id:
                relations_of_comp.append(relation.id)
    return relations_of_comp