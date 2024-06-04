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

### simple bank system challenge done - 4/6