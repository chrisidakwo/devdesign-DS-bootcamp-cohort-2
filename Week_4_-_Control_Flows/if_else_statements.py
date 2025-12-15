# Take input and validate to ensure it's amongst allowed/permitted colors
light = input("What color is the traffic light? ").lower()

# One "equal to" symbol means assignment
# Doube "equal to" symbol is for comparison

# allowed colors: red, yellow, green

# TODO: Modify colors into a list

# Syntax of an if clause:

# if condition: 
    # 	code that runs of the condition is true

if light == "red" or light == "yellow" or light == "green":
    if light == "green" or light == "blinking": # if clause
        print("Go")
    elif light == "yellow": # elif clause
        print("Slow down")
    # elif light == "red": # elif clause
    else: # else clause
        print("Stop")
else:
    print("Valid colors are red, green, and yellow ONLY!")

print("")
print("---------------------------------------------")
print("")

temperature = 15
humidity = 15

# Read more: Truth Tables
if temperature > 30 or humidity < 20:
    print("Warning: Unusual weather condition detected!")
else:
    print("Weather conditions are normal")






