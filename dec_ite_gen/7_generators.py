def my_generator(numbers):
    for n in numbers:
        print("execution:", n)
        yield n
        print("execution:", n)

for n in my_generator([1,2,3,4,5]): # my_generator returns a value, and when the iteration calls it again, it comes back to where it stopped (after yield)
    print(n)
    print("test")