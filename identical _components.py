def identical_components(components):
    # identical_components = []
    # for i in range(len(components)):
    #     if components[i].attribute

    identical_components = []
    visited = set()

    for i in range(len(components)):
        if i in visited:
            continue

        identical = [components[i].id]
        visited.add(i)

        for j in range(i + 1, len(components)):
            if j in visited:
                continue

            if (components[i].type == components[j].type and components[i].attributes == components[j].attributes):
                identical.append(components[j].id)
                visited.add(j)

        if len(identical) > 1:
            identical_components.append(identical)

    return identical_components

def find_list_index(identical_components, id):
    for i in range(len(identical_components)):
        if id in identical_components[i]:
            return i
    return None

def identical_relations(relations, identical_components):
    identical_relations = []
    visited = set()

    for i in range(len(relations)):
        if i in visited:
            continue

        identical = [relations[i].id]
        visited.add(i)

        for j in range(i + 1, len(relations)):
            if j in visited:
                continue

            if relations[i].type == relations[j].type :
                if relations[i].type in ["ordered_assembly", "ordered_reference"]:
                    if relations[i].order == relations[j].order:
                        ident_refs = 0
                        for k in range(len(relations[i].refs)):
                            if relations[i].refs[k].id == relations[j].refs[k].id:
                                ident_refs += 1
                            else:
                                for l in range(len(identical_components)):                        
                                    if relations[i].refs[k].id in identical_components[l]:
                                        index = find_list_index(identical_components, relations[i].refs[k].id)
                                        if relations[j].refs[k].id in identical_components[index]:
                                            ident_refs += 1
                        if ident_refs == len(relations[i].refs):
                            identical.append(relations[j].id)
                            visited.add(j)

        if len(identical) > 1:
            identical_relations.append(identical)

    return identical_relations
            
if __name__ == "__main__":
    from import_data import import_data

    relations_roles = ["assembly", "part", "stage", "gear_1", "gear_2", "gear", "stage_gear_data", "inner_part", "outer_part", "left", "right", "origin", "referenced", "workpiece", "tool", "manufacturing_settings", "planetary_stage", "shaft"]
    components, relations = import_data("Sample_Data/2-stage_industry-gearbox/fva_2-stage_industry-gearbox_1-2.rexsj", relations_roles)
    identical_components = identical_components(components)
    print(identical_components)
    identical_relations = identical_relations(relations, identical_components)
    print(identical_relations)