import operator as op

inventory = [("apple", 3), ("banana", 2), ("pear", 5), ("orange", 1)]

# print(list(map(lambda i: i[1], inventory)))
getcount = op.itemgetter(1)
print(list(map(getcount, inventory)))
print(sorted(inventory, key=getcount))
