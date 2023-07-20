def get_component_types(components):
    component_types=[]
    for i in range(len(components)):
        type=components[i].type
        if type not in component_types:
            component_types.append(type)
    return component_types