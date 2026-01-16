with open("Sample - Superstore.csv", "r") as file:
    # Read and clean header
    header_line = file.readline().strip()
    columns = header_line.split(",")

    print("========== SUPERSTORE DATASET COLUMNS ==========")
    for (count, column) in enumerate(columns, 1):
        print(f"{count:2}. {column}")
