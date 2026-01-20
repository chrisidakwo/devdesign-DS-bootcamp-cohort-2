# Step 1: Opening and Reading a File
file = open("files/Sample - Superstore.csv", "r")
content = file.read()
file.close()

print(content)

# Absolute file path: Path to the file on your laptop/deskop or cloud/online
# c:/Users/chris/Documents/Personal/Bootcamp/Python/intro.py
# C:\Users\ADMIN\Source\Data Science Bootcamp\Cohort 2\Week_5_-Working_with_Files\files\Sample - Superstore.csv

# Relative file path: Path to the file relative to the Python file importing it.

# Step 2: Using 'with' statement (Best practice)
with open("files/Sample - Superstore.csv", "r") as file:
    # Read header
    header = file.readline().strip()
    print("Columns:", header)

    for line in file:
        print(line.strip())
        print("="*20)




