num_list = [-9, 29, -100, 64, 26, 73, -96, 28, -92, 11, -14, -86, -54, -67]

for i in num_list:
    if num_list.index(i) == 0:
        prv = i
    else:
        if prv < i:
            print(i)
        prv = i
