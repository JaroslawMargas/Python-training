my_list = [1, 2, 3, 4, 5]

# 0,1,2,3,4,5 -> -6,-5,-4,-3,-2,-1
print(my_list[2:-1])
# [3, 4]
# --------------------------------

print([n ** 2 for n in range(10) if n % 2 == 0])
# x^2 for 0,2,4,6,8 -> [0, 4, 16, 36, 64]

# --------------------------------

dict_data = {n: n ** 2 for n in range(10)}
print(dict_data)


# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}