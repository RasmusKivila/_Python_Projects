import json

with open("person.json") as f:
    persons = json.load(f)
    print(persons['persons'][0])