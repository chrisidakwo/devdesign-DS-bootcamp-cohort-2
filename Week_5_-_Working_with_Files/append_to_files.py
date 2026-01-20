from datetime import datetime

file_path = "files/log.txt"

# Add content to the end of an existing file
with open(file_path, "a") as file:
    file.write("New entry: " + str(datetime.now()) + "\n")
    
