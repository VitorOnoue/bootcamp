# # use with
# from pathlib import Path

# ROOT_PATH = Path(__file__).parent

# with open(ROOT_PATH/"readexample.txt", "r") as file: # this ensures the file is gonna be closed
#     print()
# print(file.read()) # wont work as file is closed



# # make sure file was opened

# try:
#     with open("file.txt") as file:
#         print()
# except IOError as exc:
#     print(f"error opening the file, {exc}")



# # make sure correct encoding
# try:
#     with open("file.txt", "w", encoding="utf-8") as file:
#         file.write("test123")
# except IOError as exc:
#     print(f"error opening the file, {exc}")
# except UnicodeDecodeError as exc:
#     print(exc)