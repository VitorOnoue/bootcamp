class FileIterator:
    def __init__(self, file):
        self.file = open(file)

    def __iter__(self):
        return self
    
    def __next__(self):
        row = self.file.readline()
        if row == "":
            self.file.close()
            raise StopIteration
        return row

for row in FileIterator("dec_ite_gen/example.txt"):
    print(row)