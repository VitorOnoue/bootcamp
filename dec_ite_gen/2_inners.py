def outer():
    print("running outer")

    def inner1():
        print("running inner 1")

    def inner2():
        print("running inner 2")
    
    inner1()
    inner2()

outer()