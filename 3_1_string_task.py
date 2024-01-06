# s, a, b = [input() for _ in range(3)]
# operation_count = 0
# while a in s:
#     operation_count += 1
#     if operation_count > 1000:
#         print("Impossible")
#         break
#     s = s.replace(a, b)
# else:
#     print(operation_count)

def indexer(s, t):
    offset = 0
    while offset != -1:
        if s[offset:].startswith(t):
            yield offset
        offset = s.find(t, offset + 1)


s, t = input(), input()
print(len(list(indexer(s, t))))

# for offset in range(0, len(s) - len(t) + 1):
#     if s[offset:offset + len(t)] == t:
#         count += 1
# print(count)