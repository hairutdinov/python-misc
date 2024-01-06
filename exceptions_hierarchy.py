user_exceptions = []

# exceptions = {}
# for e in [input().split(" ") for _ in range(int(input()))]:
#     exceptions[e[0]] = e[2:]
exceptions = {d: set(b[1:]) for _ in range(int(input())) for d, *b in [input().split()]}
# exceptions = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError'], 'OSError': [], 'FileNotFoundError': ['OSError']}

def exception_parent_already_caught(exc):
    visited = set()
    visited.add(exc)
    queue = [exc]
    while queue:
        vertex = queue.pop(0)
        for _parent in exceptions.get(vertex, []):
            if _parent not in visited:
                visited.add(_parent)
                if _parent in user_exceptions:
                    return True
                queue.append(_parent)
    return False

for e in [input() for _ in range(int(input()))]:
# for e in ["ZeroDivisionError", "OSError", "ArithmeticError", "FileNotFoundError"]:
    if exception_parent_already_caught(e):
        print(e)
        continue
    user_exceptions.append(e)