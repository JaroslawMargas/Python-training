# Python program to explain property() function

# Alphabet class
class Alphabet:
    def __init__(self, value):
        self._value = value

        # getting the values

    def getValue(self):
        return self._value

        # setting the values

    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value

        # deleting the values

    def delValue(self):
        del self._value

    value = property(getValue, setValue, delValue, )


# passing the value
x = Alphabet('GeeksforGeeks')
print("Value: {0}" .format(x.value))

# setting value
x.value = 'GfG'
print("Value: {0}" .format(x.value))

del x.value
