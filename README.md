# bootcamp python

### variable types - 5/8
+ there is not a keyword for constants:
  + the convention is to "declare" constants is to use full upper-case variables:
    + e.g., SIZE = 10

+ another convention: variable names are snake case:
  + e.g., size_array = 10

+ its possible to assign two variables at the same time, just like in other languages:
  + e.g.: name, age = "vkko", 2

+ its possible to change variable types when assigning another value:
  + e.g.: x = ["g", "3", "x"] - x = 2

---

### type casting - 5/8

+ to typecast, just call the method with the variable inside of it:
  + e.g., x = 10 - x = float(x) - now x is a float

+ dividing an int will turn it into a float
  + e.g., x = 10 - x = x/2 - now x is a float
    + using // will keep it an int

+ you can put an int inside a string using {}:
  + e.g., x = 10 - text = "the result is {x}"

---

### input, print - 5/8

+ print() has end and sep arguments
  + default end is \n
  + default sep is a space (" ")
    + so, behind the scenes, print is like this: print(x, end="\n", sep=" ")