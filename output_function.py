import json
import sys


def output_function(components: list, components_prime: list, sol_x: list, input_file: str, input_file_prime: str, output_file_json: str, components_unique: bool, relations_unique: bool, components_prime_unique: bool, relations_prime_unique: bool, infeasible: bool):
    """"
    This function gives the resulting matching in a json format.\n
    Input: \n
        - components: list of components of model A.\n
        - components_prime: list of components of model B.\n
        - sol_x: solution of the optimization problem for the components as a list.\n
        - input_file: name of the input file of model A.\n
        - input_file_prime: name of the input file of model B.\n
        - output_file_json: name of the output file.\n
        - components_unique: boolean if the IDs of the components in model A are unique.\n
        - relations_unique: boolean if the IDs of the relations in model A are unique.\n
        - components_prime_unique: boolean if the IDs of the components in model B are unique.\n
        - relations_prime_unique: boolean if the IDs of the relations in model B are unique.\n
        - infeasible: boolean if the optimization problem is infeasible.\n
    Output: \n
         json file with the resulting matching and possible warnings for further use.\n
    """
    # Initialization of the dictionaries that will be transformed into the json file
    component_matches = []
    components_only_a = []
    components_only_b = []
    warnings = []

    if infeasible == False:
        # Filling the dictionary with the resulting matching
        for i in range(len(sol_x)):
            for j in range(len(sol_x[0])):
                if sol_x[i][j]==1:
                    match = {}
                    type = components[i].type
                    comp_a_id = components[i].id
                    comp_a_name = components[i].name
                    if comp_a_name == None:
                        component_a = {"id": comp_a_id, "name": ""}
                    else:
                        component_a = {"id": comp_a_id, "name": comp_a_name}
                    comp_b_id = components_prime[j].id
                    comp_b_name = components_prime[j].name
                    if comp_b_name == None:
                        component_b = {"id": comp_b_id, "name": ""}
                    else:
                        component_b = {"id": comp_b_id, "name": comp_b_name}
                    attributes_comp_a = components[i].attributes
                    attributes_comp_b = components_prime[j].attributes
                    attributes_list =[]
                    for attribute_a in attributes_comp_a:
                        match_found = False
                        for attribute_b in attributes_comp_b:
                            if attribute_a.id == attribute_b.id:
                                match_found = True
                                if attribute_a.param_value == attribute_b.param_value and attribute_a.unit == attribute_b.unit:
                                        attribute = {
                                            "result": "values_equal", 
                                            "id": attribute_a.id, 
                                            "unit": attribute_a.unit, 
                                            attribute_a.param_type: attribute_a.param_value}
                                elif (attribute_a.param_value == attribute_b.param_value and attribute_a.unit != attribute_b.unit) or (attribute_a.param_value != attribute_b.param_value):
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
                    component_matches.append(match)
        
        # Filling the dictionary with the components that are only in model A
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
                if components[i].name == None:
                    component={"type": components[i].type, 
                            "id": components[i].id, 
                            "name": "",
                            "attributes": attributes_list}
                else:
                    component={"type": components[i].type, 
                            "id": components[i].id, 
                        "name": components[i].name,
                        "attributes": attributes_list}
                components_only_a.append(component)

        # Filling the dictionary with the components that are only in model B
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
                if components_prime[j].name == None:
                    component={"type": components_prime[j].type, 
                            "id": components_prime[j].id, 
                                "name": "",
                            "attributes": attributes_list}
                else:
                    component={"type": components_prime[j].type, 
                        "id": components_prime[j].id, 
                        "name": components_prime[j].name,
                        "attributes": attributes_list}
                components_only_b.append(component)

    # Filling the dictionary with the warnings
    if components_unique == False:
        warning = {"warning": f"The IDs of the components in {input_file} are not unique."}
        warnings.append(warning)
    
    if relations_unique == False:
        warning = {"warning": f"The IDs of the relations in {input_file} are not unique."}
        warnings.append(warning)

    if components_prime_unique == False:
        warning = {"warning": f"The IDs of the components in {input_file_prime} are not unique."}
        warnings.append(warning)
    
    if relations_prime_unique == False:
        warning = {"warning": f"The IDs of the relations in {input_file_prime} are not unique."}
        warnings.append(warning)

    if infeasible == True:
        warning = {"warning": f"The optimization problem is infeasible."}
        warnings.append(warning)
        
    output_dict = {"component_matches": component_matches,
            "components_only_a": components_only_a,
            "components_only_b": components_only_b,
            "warnings": warnings}
    

    with open(output_file_json, "w", encoding= "utf-8") as outputfile:
        # outputfile.write(json_object)
        json.dump(output_dict, outputfile, ensure_ascii=False, indent = 3)
