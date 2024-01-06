import json
from operator import itemgetter

# json_string = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'

# data = [
#    {"name": "B", "parents": ["A", "C"]},
#    {"name": "C", "parents": ["A"]},
#    {"name": "A", "parents": []},
#    {"name": "D", "parents":["C", "F"]},
#    {"name": "E", "parents":["D"]},
#    {"name": "F", "parents":[]}
# ]
data = json.loads(input())
# data = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]

def find_cls_parents_by_name(cls_name):
    """
        Находит родителей по имени класса
        :param str cls_name: ключ <name> из словаря {"name": "cls_name", "parents": [...]}
        :return: список родителей
    """
    try:
        idx = list(map(itemgetter('name'), data)).index(cls_name)
        return data[idx].get("parents", [])
    except ValueError:
        return None

def parents_tree(cls_obj):
    parents = []
    visited = set()
    parents.extend(cls_obj["parents"])
    while parents:
        parent = parents.pop(0)
        visited.add(parent)
        for p in find_cls_parents_by_name(parent):
            if p not in visited:
                parents.append(p)
    return list(visited)

child_and_parents = {item["name"]: parents_tree(item) for item in data}

for cls in sorted(child_and_parents.keys()):
    count = 1
    for parents in child_and_parents.values():
        if cls in parents:
            count += 1
    print("%s : %s" % (cls, count))