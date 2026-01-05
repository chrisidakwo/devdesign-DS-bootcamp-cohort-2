names = ["Mike", "Jane", "Blessing", "Peter", "Joe", "Sarah", "Chris", "Daniel", "Jasper", "Irine"]
print(len(names))

# traverse through a list

print("Returns the 1st item", names[0])
print("Returns the 2nd item", names[1])
print("Returns the 3rd item", names[2])
print("Returns the 4th item", names[3])
print("Returns the 5th item", names[4])
print("Returns the 6th item", names[5])
print("Returns the last item", names[9])

# In the case you're not sure the number of tiems in a list, you can retrieve the last item using negative index
# Also note that using negtive index let's you read a list from the back
print("Returns the last item using negative index", names[-1])

# Alternatively, you can use the example below 
# print(names[len(names) - 1])
