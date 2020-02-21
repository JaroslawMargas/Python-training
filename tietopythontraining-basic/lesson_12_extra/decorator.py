def other_function():
    print("other_function")


def decorator(obj):
    return other_function


@decorator
def function():
    print("hello")


function()

# other_function
