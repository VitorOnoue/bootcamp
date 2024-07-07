# whenever we try to open a file that doesnt exist, python returns an error
# by doing this code below, its possible to change what happens when this error occurs
try:
    file = open("this_file_doesnt_exist.txt")
except FileNotFoundError:
    print("file not found")

# its possible to have more than one except with the same try (it should have, most likely)
# also, by using the keyword Exception, the except will catch all types of errors (this is not recommended ofc, as usually this is used to take care of specific errors)