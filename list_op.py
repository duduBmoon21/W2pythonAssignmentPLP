# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending:", my_list)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Index 1 is the second position
print("After inserting 15:", my_list)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending:", my_list)

# Remove the last element from my_list
my_list.pop()  # pop() without index removes last element
print("After removing last element:", my_list)

# Sort my_list in ascending order
my_list.sort()
print("After sorting:", my_list)

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Final result
print("Final my_list:", my_list)