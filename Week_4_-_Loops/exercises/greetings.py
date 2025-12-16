name = input("Enter your name: ")
times = input("How many greetings do you want? ")

if times.isnumeric():
    for i in range(int(times)):
        print(f"Hello {name}")
else:
    print("Please enter a valid number")