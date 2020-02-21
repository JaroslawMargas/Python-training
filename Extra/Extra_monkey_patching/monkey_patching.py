from Extra_monkey_patching import m


def monkey_f(self):
    print("monkey_f()")


m.MyClass.function = monkey_f
obj = m.MyClass()
obj.function()
