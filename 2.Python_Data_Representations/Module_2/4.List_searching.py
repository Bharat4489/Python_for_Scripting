"""
Searching lists.
"""

toys = ["blocks", "slinky","legos", "fidget spinner", "cards", "doll house", "legos", "blocks", "teddy bear"]

# Finding items in a list
print(toys.index("legos")) # giving the first occurrence of "legos"
print(toys.index("blocks"))
#print(toys.index("video game"))

print("")

# Checking if items are in a list
print("legos" in toys)
print("blocks" in toys)
print("video game" in toys)
print("teddy bear" not in toys)
print("dice" not in toys)

print("")

# Counting items in list
print(toys.count("slinky"))
print(toys.count("blocks"))