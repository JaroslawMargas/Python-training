lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

print(lst)

# idx, string
for idx, s in enumerate(lst):
    print("%s has an index of %d" % (s, idx))

# alpha has an index of 0
# bravo has an index of 1
# charlie has an index of 2
# delta has an index of 3
# echo has an index of 4

for i in range(2, 4):
    print("lst at %d contains %s" % (i, lst[i]))

# list (0,1,2,...)
# range for item 2 and 4-1
# i=2
# itm [2] = charlie (list 0,1,2,...)
# i=3
# itm [3] = delta
# print
# lst at 2 contains charlie
# lst at 3 contains delta

print("From 1 to 2: ")
for s in lst[1::2]:
    print(s)

# goes from element at index 1 to the end with a step of 2
# jump 2 step !
# 1 bravo JUMP 2 ___ JUMP 3 delta

# bravo
# delta
