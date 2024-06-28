def my_decorator(function):
    def envelope():
        print("before running")
        function()
        print("after running")

    return envelope

@my_decorator
def helloworld():
    print("hello world!")

helloworld()

# using @ is easier

"""def helloworld():
    print("hello world!")

helloworld = my_decorator(helloworld)    # now helloworld contains envelope, which is its own function + two prints
helloworld()
"""