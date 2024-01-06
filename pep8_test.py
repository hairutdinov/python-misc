a = [i for i in range(21)]
lower = 5
upper = 16
offset = 1
step = 2

a[lower + offset:upper + offset]
a[lower : : upper]
a[lower + offset : upper + offset]
a[lower+offset : upper+offset]
a[lower:upper], a[lower:upper:], a[lower::step]