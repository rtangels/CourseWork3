import json
way = 'operations.json'
def born_list(path):
    with open(path, 'r', encoding='utf-8') as file:
         data=json.load (file)
    return data
print(born_list(way))