# replace single "i" with "I"

import os
import re

current = os.path.dirname(__file__)
file_name = "text.txt"
path_file = os.path.join(current, file_name)

with open(file_name) as fp:
    text = fp.read()
fp.close()

reg_exp = r"\b[i]\b"
exp = re.compile(reg_exp)
new = re.sub(exp, "I", text)
print(new)
