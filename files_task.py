with open("in.txt") as f, open("out.txt", "w") as fw:
    fw.write("".join(reversed([line for line in f])))

# with open("in.txt") as f, open("out.txt", "w") as fw:
#     fw.writelines(reversed([line for line in f]))

# print(*reversed(open("in.txt").readlines()), sep="")