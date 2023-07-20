from parse_json import parse_json
from sort_refs import sort_refs
from pydantic import BaseModel, root_validator
from typing import Any
from find_index import find_index
from sort_data import sort_data
from get_component_types import get_component_types

filename = "Sample_Data/model_matching_test_comp_49-1150.json"

data = parse_json(filename)


relations = data["model"]["relations"]
components = data["model"]["components"]


# class for the attributes of the components
class Attribute(BaseModel):
    id: str
    unit: str
    origin: str | None
    param_name: str
    param_value: Any
    

    @root_validator(pre=True, allow_reuse = True)
    def extract_param_name_value(cls, values: dict[str, Any]) -> dict[str, Any]:
        # Get the set difference to find the key of the parameter
        keys = set(values.keys()) - {"id", "unit"}
        if keys:
            param_name = keys.pop()
            values["param_name"] = param_name
            if param_name == "boolean":
                values["param_value"] = bool(values[param_name])
            elif param_name == "string":
                values["param_value"] = str(values[param_name])
            elif param_name == "integer":
                values["param_value"] = int(values[param_name])
            elif param_name == "floating_point":
                values["param_value"] = float(values[param_name])
            elif param_name == "enum":
                values["param_value"] = str(values[param_name])
            elif param_name == "reference_component":
                values["param_value"] = int(values[param_name])
            elif param_name == "file_reference":
                values["param_value"] = str(values[param_name])
            elif param_name == "floating_point_array":
                values["param_value"] = [float(v) for v in values[param_name]]
            elif param_name == "integer_array":
                values["param_value"] = [int(v) for v in values[param_name]]
            elif param_name == "boolean_array": 
                values["param_value"] = [bool(v) for v in values[param_name]]
            elif param_name == "string_array":
                values["param_value"] = [str(v) for v in values[param_name]]
            elif param_name == "enum_array":
                values["param_value"] = [str(v) for v in values[param_name]]
            elif param_name == "floating_point_matrix":
                values["param_value"] = [[float(v) for v in row] for row in values[param_name]]
            elif param_name == "integer_matrix":
                values["param_value"] = [[int(v) for v in row] for row in values[param_name]]
            elif param_name == "boolean_matrix":
                values["param_value"] = [[bool(v) for v in row] for row in values[param_name]]
            elif param_name == "string_matrix":
                values["param_value"] = [[str(v) for v in row] for row in values[param_name]]
            elif param_name == "arrray_of_integer_arrays":
                values["param_value"] = [[int(v) for v in row] for row in values[param_name]]
            else:
                values["param_value"] = values[param_name]
        return values



# class for components
class Component(BaseModel):
    id: int
    type: str
    name: str | None
    attributes:list[Attribute]

# class for reference components for the relations
class Ref(BaseModel):
    id: int
    role: str
    hint: str | None

# class for relations
class Relation(BaseModel):
    id: int
    type: str
    order: int | None
    refs: list["Ref"]


# read in the data
relations = [Relation(**r) for r in relations]
components = [Component(**c) for c in components]
components_dict = {c.id: c for c in components}
relations_dict = {r.id: r for r in relations}

# sort the data
components = sort_data(components)
relations = sort_data(relations)
# id = 1
# print(components_dict[id]) # returns the component mit id = 3

#[c for c in components if c.id == id][0] # liste mit componenten, die die id = id haben

role_ordering = ["assembly", "part", "stage", "gear_1", "gear_2", "gear", "stage_gear_data", "inner_part", "outer_part", "left", "right", "origin", "referenced", "workpiece", "tool", "manufacturing_settings", "planetary_stage", "shaft"]
relations = sort_refs(relations, role_ordering)
component_types = get_component_types(components)

print(component_types)

if __name__ == "__main__":
    no_attr = len(components[0].attributes)
    print(f"The first component has {no_attr} attributes")
    # print(relations[16])
    # print(relations_dict[494])
    # print (components[0])
    print(components_dict[494])
    # index = find_index(39, relations)
    # print(index)
    