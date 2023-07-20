from parse_json import parse_json
from pydantic import BaseModel

filename = "Sample_Data/model_matching_test_1.json"

data = parse_json(filename="Sample_Data/model_matching_test_1.json")

# print(data)
# print(data["model"]["relations"])
# print(data["model"]["components"])

from typing import Dict, Union

class Test(BaseModel):
    id: int
    unit: str
    attr: Dict[str, Union[float, int, str]]

test = Test(id = 1, unit = "bar", attr = {"name": 2})
print(test.id)
print(test.unit)
print(test.attr) 