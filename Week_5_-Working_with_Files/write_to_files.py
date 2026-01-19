file_path = "files/greeting.txt"

with open(file_path, "w") as file:
    # Write content to line
    file.write("Hello, this is a new line entry in a new file!\n")
    file.write("This is another new line!\n")
    file.write("Now I'm just having fun at it!")
    file.write("\n\n")
    file.write("=" * 80)
    file.write("\n\n")

    # Write multiple lines at once
    names = ["Gospel Ibekwe", "Kabeke Mukanzu", "Doyinsola Simbiat", "Deborah Enitan", "Tech World"]

    # Option 1: Introduce a new line character to each name in the list using a for loop
    newNames = []
    for name in names:
        newNames.append(f"{name}\n")

    # Option 2: Introduce a new line character to each name in list using a list comprehension
    newNames = [f"{name}\n" for name in names]

    file.writelines(newNames)
