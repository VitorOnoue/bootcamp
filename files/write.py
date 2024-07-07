file = open("files/writeexample.txt", "w")
file.write("lorem ipsum dolor sit amet")
file.writelines("\nlorem") # works fine, but shouldnt be used like this
file.writelines(["\nlorem ", "ipsum ", "dolor ", "sit ", "amet"])
file.close()