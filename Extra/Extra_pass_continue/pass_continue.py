for i in 'hello':
    if i == 'e':
        print('pass executed')
        pass
    print(i)

print('----')

for i in 'hello':
    if i == 'e':
        print('continue executed')
        continue
    print(i)

# h
# pass executed
# e
# l
# l
# o
# ----
# h
# continue executed
# l
# l
# o
