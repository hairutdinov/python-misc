def process_classes():
    parents = {}
    for tpl in [input().split(" ") for _ in range(int(input()))]:
        parents[tpl[0]] = tpl[2:]

    def is_parent(parent, child):
        visited = set()
        queue = [child]
        visited.add(child)
        if parent == child:
            return True
        while queue:
            vertex = queue.pop(0)
            for _parent in parents.get(vertex, []):
                if _parent not in visited:
                    visited.add(_parent)
                    queue.append(_parent)
                if _parent == parent:
                    return True
        return False

    for tpl in [input().split(" ") for _ in range(int(input()))]:
        print("Yes" if is_parent(tpl[0], tpl[1]) else "No")
