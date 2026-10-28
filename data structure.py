# List: ordered and changeable
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("List:", fruits)
print("First fruit:", fruits[0])

# Tuple: ordered and unchangeable
coordinates = (10, 20)
print("\nTuple:", coordinates)
print("X coordinate:", coordinates[0])

# Set: stores unique values
numbers = {1, 2, 2, 3, 4, 4}
numbers.add(5)
print("\nSet (duplicates removed):", numbers)

# Dictionary: key-value pairs
student = {
    "name": "Anchal",
    "course": "BTech",
    "year": 3
}
student["year"] = 4
print("\nDictionary:", student)
print("Student name:", student["name"])