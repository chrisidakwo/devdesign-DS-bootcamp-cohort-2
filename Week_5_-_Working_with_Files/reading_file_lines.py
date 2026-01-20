file_ = open("files/Sample - Superstore.csv", "r")

# Read first line (header)
header = file_.readline().strip()
header = header.split(",")

# Read all other lines
for line in file_:
    print(line.strip().split(","))
    print("="*20)

file_.close()

# Read all lines into a list
with open('files/example.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # List of strings, one per line