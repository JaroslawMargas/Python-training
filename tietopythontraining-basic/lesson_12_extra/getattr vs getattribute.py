class Count:
    def __init__(self, my_min, my_max):
        self.my_min = my_min
        self.my_max = my_max

    # def __getattr__(self, item):
    #     self.__dict__[item] = 0
    #     return 0

    def __getattribute__(self, item):
        if item.startswith('cur'):
            # prevent
            # raise AttributeError
            #
            # or return
            return 0
        return object.__getattribute__(self, item)
        # or you can use ---return super().__getattribute__(item)


obj1 = Count(1, 10)
print(obj1.my_min)
print(obj1.my_max)
print(obj1.current1)

# __getattr__
# 1
# 10
# 0

# __getattribute__
# raise AttributeError
# 0
