import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent # setting the path of the folder

os.mkdir(ROOT_PATH/"new folder") # creating a folder

file = open(ROOT_PATH/"newfile.txt", "w") # creating a file in the correct folder already
file.close()

os.rename(ROOT_PATH/"newfile.txt", ROOT_PATH/"newname.txt") # renaming file

file2 = open("testfile.txt", "w") # will be moved to the correct folder
file2.close()

shutil.move("testfile.txt", ROOT_PATH/"testfile.txt") # moves the file to the correct folder

os.remove(ROOT_PATH/"newname.txt")
os.remove(ROOT_PATH/"testfile.txt")