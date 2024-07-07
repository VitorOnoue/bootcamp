file = open("files/readexample.txt", "r")
# print(file.read())
# print()
# print(file.readline())
# print(file.readline())
# print(file.readline()) # the file contains only two lines, returns empty

# to iterate through lines, two options:
# 1 - use readlines() (which returns an array), and iterate through it directly
# 2 - iterate some other way (for example, while the length of the line is not 0), and use readline()
# 2 may be better, if the file is too big (the array size can be an issue) 
# if readline() is used, the iteration is gonna happen for each character of the returned line


# while len(line := file.readline()):
#     print(line)

for line in file.readlines():
    print(line)
    
file.close()