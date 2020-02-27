import re

string = "aba"

reg = "a"
exp = re.compile(reg)

result = re.findall(exp, string)

if len(result) > 1:
    print("There are: {0} chars {1}".format(str(len(result)), reg))
else:
    print("NO more than one")
