# bootcamp python - notes

### variable types - 5/8

+ there is not a keyword for constants:
  + the convention is to "declare" constants is to use full upper-case variables:
    + e.g., `SIZE = 10`

+ another convention: variable names are snake case:
  + e.g., ``size_array = 10``

+ its possible to assign two variables at the same time, just like in other languages:
  + e.g.: `name, age = "vkko", 2`

+ its possible to change variable types when assigning another value:
  + e.g.: `x = ["g", "3", "x"] - x = 2`

---

### type casting - 5/8

+ to typecast, just call the method with the variable inside of it:
  + e.g., `x = 10 - x = float(x)` - now x is a float

+ dividing an int will turn it into a float
  + e.g., `x = 10 - x = x/2` - now x is a float
    + using // will keep it an int

+ you can put an int inside a string using {}:
  + e.g., `x = 10 - text = "the result is {x}"`

---

### input, print - 5/8

+ `print()` has end and sep arguments
  + default end is `\n`
  + default sep is a blank space (" ")
    + so, behind the scenes, print is like this: `print(x, end="\n", sep=" ")`

---

### strings - 5/14

+ methods:
  + `.upper()`, `.lower()` do what they say

  + `.title()` uppers the first letter and lowers the others

  + `.strip()` removes all left and right blank spaces, and writes its name (ts pun intended)
    + `.lstrip()` and `.rstrip()` remove only left and right, respectively

  + `.center(x, "something")` will center the string with "something" on its left and right, until the string reaches x chars
    + e.g., `s = "hi" - s.center(10, "x")` - now s = "xxxxhixxxx"
    + 2nd argument is optional, default = blank space

  + `.join(str1.join(str2))`, for each char in str2, str1 will be concatenated
    + e.g., `s = "1234" - "-".join(s)` - now s = "1-2-3-4"
  
+ string formats:
  + using %: just like in C (old style, not normally used)
    + e.g., `name = "vkko" - print("hi, im %s" % (name))`
      + name is an argument here
    
  + using format: similar to the previous method, but uses {} instead of %"something"
    + e.g., `name = "vkko" - print("hi, im {}" .format(name))`
      + name is also an argument here

#### continuing strings - 5/21

  + using f-string: {variable}
    + e.g., `name = "vkko" - print(f"hi, im {name}")`
    + formatting with f-string:
      + e.g., PI = 3.1415 - printf(f"PI for engineers = {PI:.0f}")

#### string slicing - 5/21

  + syntax: `var[x:y:z]`, x/y are indexes, z is a number, x/y/z can be negative
    + with x only: will return only the character in the x index
      + e.g, `name = "vkko" - print(name[0])` - prints "v"
    + with x and y (x omitted = all the left side, y omitted = all the right side): string between x and y
      + the character is included, the character in y is NOT
        + e.g. 1, `name = "vkko" - print(name[:3])` - prints "vkk"
        + e.g. 2, `name = "vkko" - print(name[:])` - prints "vkko"
    + including z: kind of a counter that gets the character after z steps, then resets
      + starting point is included
        + e.g., `name = "vkko" - print(name[::2])` - prints "vk"
      + negative z = inverts the string order
        + e.g., `name = "vkko" - print(name[::-1])` - prints "okkv"
  
#### multiple-line string - 5/21

  + by using triple quotes (either), strings can be written in more than one line
    + e.g,
      ```
      msg = """hi

      im

      vkko"""
      ```
      the output will be exactly like the assigned string

---

## simple bank system challenge done - 6/4

### lists - 6/4

+ lists can store any type of object - types can be mixed
  + e.g., `array = ["vkko", 20, 1.65, True]`

+ can be created with list() constructor
  + e.g., `numbers = list(range(10))` - list contains 0-9 numbers

+ accessing values by index:
  + we can use negative indexes (-1 = last, -2 = second last, etc)
    + e.g, `n = [1,2,3,4]` - n[-1] = 4

+ lists can have lists inside too (nested)
  + matrix (2d list) is the same as `m = [[1,2],[3,4]]`
    + accessing its values: m[1][0] = 3

+ slicing lists work just like on strings (theoretically, strings are lists, so actually it's the other way around)

+ iterating through lists: `for x in array:`
  + with enumerate(array), we can get the index by passing another variable
    + e.g., `for i, x in enumerate(array)`
  + this is good for list comprehension (new list based on another list)
    + e.g.,
      ```
      ns = [1,2,3,4,5]
      ns2 = []
      for n in ns:
        ns2.append(n * 2)
      ```

#### continuing lists - 6/7

+ methods:
  + `.append(x)` adds x at the end of the list
    + e.g., `x = [] - x.append("vkko")`
      + reminder: an element can be another list too

  + `.clear()` empties the list

  + `.copy()` creates a copy of the list (better to store it in a var)
    + e.g, `x = [] - y = x.copy()`

  + `.count(x)` returns how many x occurrences are in the list

  + `.extend(list)` appends another list
    + reminder: appending x to a list will treat x as an element (so, we will have nested lists)
    + by using `.extend(x)`, we are appending all elements of x
  
  + `.index(x)` returns the index of the first x occurrence

  + `.pop(n)` removes the element in n index
    + if no n, default is -1, which is the last element
      + so, `.pop()` works like a stack's pop

  + `.remove(x)` removes the first occurrence of x in the list

  + `.reverse()` reverses the list (last element becomes first, etc)

  + `.sort()` sorts the list - ascending
    + with `reverse=True`, descending
  
  + `len(list)` returns the length of the list

---

### tuples - 6/7

+ tuples are similar to lists, but they are not mutable

+ to create a tuple, we can use either the tuple class, or parenthesis + commas
  + e.g, `names = ("vkko", "kkov", "kovk",)` or `numbers = tuple[1, 2, 3, 4]`
    + the last comma is to make sure the interpreter considers "names" as a tuple

+ tuples work the same way as lists, so, indexes, nesting, accessing, iterating, slicing, etc, are all equal

+ methods leftover: `.count(x)`, `.index(x)` and `len(tuple)`

---

### sets - 6/7

+ used for/remembers mathematics' sets

+ a set is a collection of data that contains no duplicates (removes duplicates)
  + the elements inside of it are not sorted
    + e.g., `x = set("vkko")` will leave only one 'k' + if you print x, it wont necessarily print "vko"

+ accessing data = transform the set into a list
  + because there are no indexing and no slicing
  + e.g, `x = {1, 2, 3, 4} - x = list(x) - print(x[0])`

+ iterating through sets is doable

+ methods:
  + `.union(set)` just like in math, if x and y are sets, x.union(y) will x U y

  + `.intersection(set)` x.intersection(y) will x U* y (thats how I used to write this symbol in my notes)

  + `.difference(set)` inverse of `.intersection()`
    + if x.difference(y), it gets of x what is not inside of y
      + e.g, if x = {1,2,3} and y = {3,4,5}, x.difference(y) = {1,2}
    + `.symmetric_difference` gets both sides' differences
  
  + `.issubset(set)` if x and y are sets, x.issubset(y) returns true if x is inside y
    + `.issuperset(set)` is the exact contrary of this (true if x contains y)

  + `.isdisjoint(set)` if x and y are sets, x.isdisjoint(y) returns true if x has no equal elements with y

  + `.add(e)` adds e, if not exists already

  + `.clear(set)` empties the set

  + `.copy(set)` just like in lists, will copy the set

  + `.discard(e)` removes e from the set, if exists

  + `.pop()` removes the first element of the set (not the last like in a list)

  + `.remove(e)` just like discard, but returns an error if e is not inside the set

  + `len(set)` length of the set

  + `e in set` returns true if e is inside set

---

### dictionaries - 6/7

+ key:value list, keys are unique

+ created with {}, filled with 'key:value's, or the class dict
  + e.g, `person = {"name": "vkko", "age": 20}` or `person = dict(nome="vkko", idade=20)`

+ to add a new key:value in a dict = dict["key"] = "value"
  + e.g, `person[number] = "11 98765-4321"`

+ iterating through dicts with for:
  + with one argument, gets the key
    + e.g.,
      ```
      for key in person:
        print(key, person[key])
      ```
  + with two arguments and using `.items()`, we get both key and value
    + `dict.items()` returns a list of tuples
    + e.g.,
      ```
      for key, value in person.items():
        print(key, value)
      ```

---

### functions - 6/10

+ syntax: `def function(parameters)`
  + by assigning a value to a parameter, you actually set ups its default value
    + e.g., `def vkko(name="vkko")` - if name is not received, then, name will be vkko
    + if the argument is not sent and there is no default, then error

+ calling the function: `function(parameters)`
  + e.g, `vkko("vitor")`

+ ofc, you can set the return with `return` just like in all languages
  + functions return None by default
  + functions can return more than multiple values (in a tuple)
    + e.g.,
      ```
      def pred_succ(n):
        pred = n - 1
        succ = n + 1
        return pred, succ
      ```

+ functions can also be called with key:value arguments
  + e.g., `vkko(name="vitor")`
    + may use dicts for this: `vkko(**{"name": "vitor"})`

+ *args and **kwargs parameters:
  + *args stores the arguments (that are not key:value) in a tuple
    + e.g., `def vkko(*args)`
      + if `vkko("vitor", "onoue")`, args will contain ("vitor", "onoue")
  + **kwargs stores the arguments in dictionary

+ / and * inside the parameters in a function:
  + all parameters before / wont be able to get key:value arguments
    + e.g, `def vkko(name, /)` - this will return an error: `vkko(name="vitor")`

## bank system improvement challenge done - 6/12

### OOP - 6/16

+ programming paradigms refers to the way (thought process, etc) a code is designed to solve a problem

+ examples:
  + imperative/procedural
  + functional
  + event-driven
  + object-oriented

+ object-oriented programming (OOP): code works around objects
  + **classes and objects** are its key concepts

#### classes and objects - 6/16

+ a class defines its characteristics and "what actions the class can perform"
  + the class itself "is just the settings/rules"

+ an object is something generated from a class
  + the object that is capable of performing the actions itself and contains its characteristics

+ good analogy: house plan and the furnitures

## first OOP program (oop.py) - 6/17

### constructors and destructors - 6/17

+ the constructor method will always be run whenever an instance is created
  + a constructor initializes/starts an object
  + to declare a constructor, create a method called \_\_init\_\_

+ the destructor method will always be run whenever an instance is destroyed (to destroy it, need to call a method)
  + they are not as needed though, python can manage memory by itself
    + the garbage collector will destroy the object after the end of the program
    + not the case in C and C++
  + to declare a destructor, create a method called \_\_del\_\_
    + to call it: `del object`