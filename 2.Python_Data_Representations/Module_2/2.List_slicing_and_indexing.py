"""
List indexing and slicing.
"""

print("List Indexing")
print("=============")

groceries = ["butter", "milk", "bacon", "spaghetti", "asparagus"]
print(groceries)


# first item
print(groceries[0])

# third item
print(groceries[2])

# length of list
numitems = len(groceries)
print(numitems)

# last item
print(groceries[-1])
print(groceries[numitems - 1])

# third from last item
print(groceries[-3])

# Out of bounds
#print(groceries[numitems])
#print(groceries[-17])

# Indices
# list = [7, 8, 3, 2, 9, 4]
# item        7  8  3  2  9  4
# pos index   0  1  2  3  4  5
# neg index  -6 -5 -4 -3 -2 -1

print("")
print("List Slicing")
print("============")

numbers = list(range(0,132,12))
print(numbers)

# Sublists
print("Sublists")
print(numbers[2:3])
print(numbers[1:4])

# Open ended slices
print("Open ended slices")
print(numbers[1:])
print(numbers[:3])

# Using negative indices
print("Using negative indices")
print(numbers[-2:])
print(numbers[1:-4])

# Empty slices
print("Empty slices")
print(numbers[3:2])
print(numbers[11:12])

# Slicing with step
print("Slicing with step")
print(numbers[1:10:2])
# Take every 3rd element starting from index 0:
#[0, 36, 72, 108]
print(numbers[::3])
