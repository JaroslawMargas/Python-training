A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i * i for i in A1}
A6 = [[i, i * i] for i in A1]

print(A0)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(A1)
# 0,1,2,3,4,5,6,7,8,9
print(A2)
# []
print(A3)
# [1, 2, 3, 4, 5]
print(A4)
# [1, 2, 3, 4, 5]
print(A5)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(A6)

# Check A3
dic = {"a": 1, "b": 5}
x = 5
for x in dic:
    print(dic[x])
