def message(name):
    print(f"running message")
    return f"hi {name}"

def long_message(name):
    print(f"running long message")
    return f"hey ho hope ur doing great {name}"

def run(function, name):
    print("running something")
    return function(name)

print(run(message, "vkko"))
print(run(long_message, "vkko"))