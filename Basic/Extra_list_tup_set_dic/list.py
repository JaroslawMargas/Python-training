# List is MUTABLE, ordered, changeable, indexes

variable1 = [1, 2, 3, 4]

# range
print("two elements: " + str(variable1[0:2]))
# two elements: [1, 2]

# List * value
print("two times: " + str(variable1 * 2))
# two times: [1, 2, 3, 4, 1, 2, 3, 4]

# list: value can be changed
variable1[0] = 100
print(variable1)

# list append
variable1.append("5")
print("list append 5")
print(variable1)

# list insert
print("list insert 2.1")
variable1.insert(2, "2.1")
print(variable1)

# list remove
print("list remove 2.1")
variable1.remove("2.1")
print(variable1)


