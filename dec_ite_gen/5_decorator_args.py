def my_decorator(function):
    def envelope(*args, **kwargs):
        print("before running")
        x = function(*args, **kwargs)
        print("after running")
        return x

    return envelope

@my_decorator
def helloworld(name):
    print(f"hello world {name}!")
    return "123"

x = helloworld("vkko")
print(x)

# using @ is easier

"""def helloworld():
    print("hello world!")

helloworld = my_decorator(helloworld)    # now helloworld contains envelope, which is its own function + two prints
helloworld()
"""