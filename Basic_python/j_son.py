import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
print(json.dumps(x, indent=2, sort_keys=True))