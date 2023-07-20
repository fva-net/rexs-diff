import json

def increase_id(json_data):
    if "relations" in json_data["model"]:
        for relation in json_data["model"]["relations"]:
            if "id" in relation:
                relation["id"] += 1
            if "refs" in relation:
                for ref in relation["refs"]:
                    if "id" in ref:
                        ref["id"] += 1
    
    if "components" in json_data["model"]:
        for component in json_data["model"]["components"]:
            if "id" in component:
                component["id"] += 1
    
    return json_data

def new_json(filename_input, filename_output):
    # Read the JSON file
    with open(filename_input, "r",encoding="utf-8-sig") as file:
        json_data = json.load(file)

    # Increase the IDs
    json_data = increase_id(json_data)

    # Write the updated JSON back to the file
    with open(filename_output, "w") as file:
        json.dump(json_data, file, indent=4)

filename_input = "Sample_Data/model_matching_test_1.json"
filename_output = "Sample_Data/model_matching_test_2_new.json"

new_json(filename_input, filename_output)