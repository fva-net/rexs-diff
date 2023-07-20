from parse_json import parse_json
from sort_refs import sort_refs
from sort_data import sort_data
from pydantic import BaseModel, root_validator
from typing import Any, Union

def import_data(filename:str, relations_roles:list):

    """
    This function will import the provided data and turn it into classes. \n
    Input: 
      - filename of a json file with the data
      - role_ordering: list of possible roles in the relations \n
    Output: 
      - components: list of components
      - relations: list of relations
      - components_dict: dictionary of the components 
    """
    data = parse_json(filename)

    relations = data["model"]["relations"]
    components = data["model"]["components"]

    # Class for the attributes of the components
    class Attribute(BaseModel):
        id: str
        unit: str
        origin: Union[str , None]
        param_type: Union[str, None]
        param_value: Union[Any, None]
        

        @root_validator(pre=True, allow_reuse = True)
        def extract_param_type_value(cls, values: dict[str, Any]) -> dict[str, Any]:
            # Get the set difference to find the key of the parameter
            keys = set(values.keys()) - {"id", "unit"}
            if keys:
                param_type = keys.pop()
                values["param_type"] = param_type
                if param_type == "boolean":
                    values["param_value"] = bool(values[param_type])
                elif param_type == "string":
                    values["param_value"] = str(values[param_type])
                elif param_type == "integer":
                    values["param_value"] = int(values[param_type])
                elif param_type == "floating_point":
                    values["param_value"] = float(values[param_type])
                elif param_type == "enum":
                    values["param_value"] = str(values[param_type])
                elif param_type == "reference_component":
                    values["param_value"] = int(values[param_type])
                elif param_type == "file_reference":
                    values["param_value"] = str(values[param_type])
                elif param_type == "floating_point_array":
                    values["param_value"] = [float(v) for v in values[param_type]]
                elif param_type == "integer_array":
                    values["param_value"] = [int(v) for v in values[param_type]]
                elif param_type == "boolean_array": 
                    values["param_value"] = [bool(v) for v in values[param_type]]
                elif param_type == "string_array":
                    values["param_value"] = [str(v) for v in values[param_type]]
                elif param_type == "enum_array":
                    values["param_value"] = [str(v) for v in values[param_type]]
                elif param_type == "floating_point_matrix":
                    values["param_value"] = [[float(v) for v in row] for row in values[param_type]]
                elif param_type == "integer_matrix":
                    values["param_value"] = [[int(v) for v in row] for row in values[param_type]]
                elif param_type == "boolean_matrix":
                    values["param_value"] = [[bool(v) for v in row] for row in values[param_type]]
                elif param_type == "string_matrix":
                    values["param_value"] = [[str(v) for v in row] for row in values[param_type]]
                elif param_type == "arrray_of_integer_arrays":
                    values["param_value"] = [[int(v) for v in row] for row in values[param_type]]
                else:
                    values["param_value"] = values[param_type]
            return values


    # Class for components
    class Component(BaseModel):
        id: int
        type: str
        name: Union[str , None]
        attributes:list[Attribute]


    # Class for reference components for the relations
    class Ref(BaseModel):
        id: int
        role: str
        hint: Union[str , None]


    # Class for relations
    class Relation(BaseModel):
        id: int
        type: str
        order: Union[int , None]
        refs: list[Ref]


    # Read in the data
    relations = [Relation(**r) for r in relations]
    components = [Component(**c) for c in components]

    # Sort the components and relations according to their ids
    components = sort_data(components)
    relations = sort_data(relations)

    # Sort the refs in the relations by their role
    relations = sort_refs(relations,relations_roles)
    
    return components, relations 



