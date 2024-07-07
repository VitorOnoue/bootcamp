import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# try:
#     with open(ROOT_PATH/"newfile.csv", "w", encoding="utf-8", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["id", "name"])
#         writer.writerow(["1", "vitor"])
#         writer.writerow(["2", "kenzo"])

# except IOError as exc:
#     print(f"Error creating the file, {exc}")

try:
    with open(ROOT_PATH/"newfile.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0], row[1])

except IOError as exc:
    print(f"Error creating the file, {exc}")

# tip - DictReader reads the line as a dictionary
# tldr, now, instead of accessing by indexes (0, 1, 2, etc), it can be acessed by the key (the column of the .csv)

try:
    with open(ROOT_PATH/"newfile.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row["id"], row["name"])

except IOError as exc:
    print(f"Error creating the file, {exc}")