import os
import re
import sys

try :
    regexp_format = re.compile(r'{}'.format(input("Provide regexp")))
except re.error :
    print("bad regexp")
    sys.exit()

for file in os.listdir(os.getcwd()) :
    if file.endswith(".txt") :
        file = open(file, "r")
        for line in file.readlines() :
            z = re.search(regexp_format, line)
            if z :
                print(file.name + ": ")
                print(line)
        file.close()
