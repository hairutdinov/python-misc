# import sys
# import re
#
# pattern = r"cat"
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(pattern, line)) > 1:
#         print(line)
#
# import re
# import sys
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r"\\", line):
#         print(line)


# import re
# import sys
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub("\b[aA]+\b", "argh", line, count=1))

# import re
# line = 'There’ll be no more "Aaaaaaaaaaaaaaa"'
# print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))


# import re
# import sys
# # for line in sys.stdin:
# for idx, line in enumerate(["this is a text", "\"this' !is. ?n1ce,"]):
#     pattern = r"\b(\w)(\w)(\w*)\b"
#     result = re.sub(pattern, "\g<2>\g<1>\g<3>", line, flags=re.MULTILINE)
#     print(result)
#     if idx == 0:
#         assert result == "htis si a etxt"
#     elif idx == 1:
#         assert result == "\"htis' !si. ?1nce,"


import re
import sys

for line in sys.stdin:
    pattern = r"\b(\w)(\w)"
    result = re.sub(pattern, r"\2\1", line.rstrip())
    print(result)
