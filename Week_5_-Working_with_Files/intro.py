

# Step 1: Opening and Reading a File
# file = open("Sample - Superstore.csv", "r")
# content = file.read()
# file.close()

# print(content)

# Absolute file path: Path to the file on your laptop/deskop or cloud/online
# c:/Users/chris/Documents/Personal/Bootcamp/Python/intro.py
# C:\Users\ADMIN\Source\Data Science Bootcamp\Cohort 2\Week_5_-Working_with_Files\Sample - Superstore.csv

# Relative file path: Path to the file relative to the Python file importing it.

# Step 2: Reading Line by Line (Row by Row)
# file_ = open("Sample - Superstore.csv", "r")

# # Read first line (header)
# header = file_.readline()
# header.split(",")

# # Read all other lines
# for line in file_:
#     print(line.split(","))
#     print("="*20)

# file_.close()


# Step 3: Using 'with' statement (Best practice)
with open("Sample - Superstore.csv", "r") as file:
    # Read header
    header = file.readline().strip()
    print("Columns:", header)

    for line in file:
        print(line.strip())
        print("="*20)


