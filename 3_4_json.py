import json
from operator import itemgetter
from collections import defaultdict
from itertools import chain

# json_string = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'

# data = [
#    {"name": "B", "parents": ["A", "C"]},
#    {"name": "C", "parents": ["A"]},
#    {"name": "A", "parents": []},
#    {"name": "D", "parents":["C", "F"]},
#    {"name": "E", "parents":["D"]},
#    {"name": "F", "parents":[]}
# ]
# data = json.loads(input())
data = [{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]

# {'B': ['A', 'C'], 'C': ['A'], 'A': [], 'D': ['C', 'F'], 'E': ['D'], 'F': []}
classes_with_parents = {c["name"]: c["parents"] for c in data}

# {'B': [], 'C': [], 'A': [], 'D': [], 'E': [], 'F': []}
parents_and_children = {
    k: [] for k in set(chain(
        *classes_with_parents.keys(),
        *classes_with_parents.values()
    ))
}

for p, children in classes_with_parents.items():
    for child in children:
        parents_and_children[child].append(p)
# ключ - родитель, значение - список прямых потомков
# {'A': ['B', 'C'], 'E': [], 'C': ['B', 'D'], 'D': ['E'], 'F': ['D'], 'B': []}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph.get(vertex, "")) - visited)
    return visited


# for p in set(chain(*map(itemgetter("parents"), data))):
for c in sorted(map(itemgetter("name"), data)):
    print("%s : %s" % (c, len(dfs(parents_and_children, c))))