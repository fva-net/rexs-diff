import json


def output_function(components: list, components_prime: list, sol_x: list, sol_z: list, output_file_json= "output/output.json"):
    """"
    This function gives the resulting matching in a json format.
    It oputputs a jsonfile with the name "output.json" in the folder "output" if not specified otherwise
    """
    component_matches = []
    components_only_a = []
    components_only_b = []

    for i in range(len(sol_x)):
        for j in range(len(sol_x[0])):
            if sol_x[i][j]==1:
                match = {}
                type = components[i].type
                comp_a_id = components[i].id
                comp_a_name = components[i].name
                component_a = {"id": comp_a_id, "name": comp_a_name}
                comp_b_id = components_prime[j].id
                comp_b_name = components_prime[j].name
                component_b = {"id": comp_b_id, "name": comp_b_name}
                attributes_comp_a = components[i].attributes
                attributes_comp_b = components_prime[j].attributes
                attributes_list =[]
                for attribute_a in attributes_comp_a:
                    match_found = False
                    for attribute_b in attributes_comp_b:
                        if attribute_a.id == attribute_b.id:
                            match_found = True

                            if attribute_a.param_value == attribute_b.param_value:
                                if attribute_a.unit == attribute_b.unit:
                                    attribute = {
                                        "result": "values_equal", 
                                        "id": attribute_a.id, 
                                        "unit": attribute_a.unit, 
                                        attribute_a.param_type: attribute_a.param_value}
                                else:
                                    comp_a = {"unit": attribute_a.unit, attribute_a.param_type: attribute_a.param_value}
                                    comp_b = {"unit": attribute_b.unit, attribute_b.param_type: attribute_b.param_value}
                                    attribute = {
                                        "result": "values_different", 
                                        "id": attribute_a.id, 
                                        "component_a": comp_a, 
                                        "component_b": comp_b }                            
                            else:
                                comp_a = {"unit": attribute_a.unit, attribute_a.param_type: attribute_a.param_value}
                                comp_b = {"unit": attribute_b.unit, attribute_b.param_type: attribute_b.param_value}
                                attribute = {
                                    "result": "values_different", 
                                    "id": attribute_a.id, 
                                    "component_a": comp_a, 
                                    "component_b": comp_b }
                            attributes_list.append(attribute)
                            break
                    if not match_found:
                        attribute = {
                            "result": "only_a", 
                            "id": attribute_a.id, 
                            "unit": attribute_a.unit, 
                            attribute_a.param_type: attribute_a.param_value}
                        attributes_list.append(attribute)

                for attribute_b in attributes_comp_b:
                    match_found = False
                    for attribute_a in attributes_comp_a:
                        if attribute_a.id == attribute_b.id:
                            match_found = True
                            break
                    if not match_found:
                        attribute = {
                            "result": "only_b", 
                            "id": attribute_b.id, 
                            "unit": attribute_b.unit, 
                            attribute_b.param_type: attribute_b.param_value}
                        attributes_list.append(attribute)
                match = {"type": type, 
                         "component_a": component_a, 
                         "component_b": component_b, 
                         "attributes": attributes_list}
                component_matches.append(match)#
    
    for i in range(len(components)):
        match_found = False
        for j in range(len(components_prime)):
            if sol_x[i][j]==1:
                match_found = True
                break
        if not match_found:
            attributes_list =[]
            for attribute_a in components[i].attributes:
                attribute = {
                    "id": attribute_a.id,
                    "unit": attribute_a.unit,
                    attribute_a.param_type: attribute_a.param_value}
                attributes_list.append(attribute)
            component={"type": components[i].type, 
                       "id": components[i].id, 
                       "name": components[i].name,
                       "attributes": attributes_list}
            components_only_a.append(component)

    for j in range(len(components_prime)):
        match_found = False
        for i in range(len(components)):
            if sol_x[i][j]==1:
                match_found = True
                break
        if not match_found:
            attributes_list =[]
            for attribute_b in components_prime[j].attributes:
                attribute = {
                    "id": attribute_b.id,
                    "unit": attribute_b.unit,
                    attribute_b.param_type: attribute_b.param_value}
                attributes_list.append(attribute)
            component={"type": components_prime[j].type, 
                       "id": components_prime[j].id, 
                       "name": components_prime[j].name,
                       "attributes": attributes_list}
            components_only_b.append(component)

    output_dict = {"component_matches": component_matches,
            "components_only_a": components_only_a,
            "components_only_b": components_only_b}
    
    json_object = json.dumps(output_dict, indent = 3)

    with open(output_file_json, "w") as outfile:
        outfile.write(json_object)
    