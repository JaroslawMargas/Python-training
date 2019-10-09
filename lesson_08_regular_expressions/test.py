import re
list_arg = ["a.jpg", "j.png", "b.jpg"]

for i in list_arg:
    x = re.search("jpg$", i)
    if x:
        print("yes re.search", x.string)

# is the same as
    if i.endswith("jpg"):
        print("yes engswith", i)