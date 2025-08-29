# Experiment 1: Demonstrating Python Data Types

# --------- Numeric Data Types ---------
print("\n--- Numeric Data Types ---")

num1 = 10
print(num1)
print("Datatype of num1 is", type(num1))

num2 = 2.5
print(num2)
print("Datatype of num2 is", type(num2))

num3 = 2 + 6j
print(num3)
print("Datatype of num3 is", type(num3))

# Example 1 - Arithmetic with integers
x = 5
y = -6
print("\nExample 1 - Integer Arithmetic")
print("Sum:", x + y)
print("Difference:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

# Example 2 - Comparison with integers
a = 10
b = 20
print("\nExample 2 - Integer Comparison")
print("Greater than:", a > b)
print("Less than or equal to:", a <= b)
print("Equal to:", a == b)
print("Not equal to:", a != b)

# Example 3 - Arithmetic with floats
x = 3.14
y = 2.5
print("\nExample 3 - Float Arithmetic")
print("Sum:", x + y)
print("Difference:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

# Example 4 - Comparison with floats
a = 1.2
b = 2.7
print("\nExample 4 - Float Comparison")
print("Greater than:", a > b)
print("Less than or equal to:", a <= b)
print("Equal to:", a == b)
print("Not equal to:", a != b)

# Example 5 - Arithmetic with complex numbers
x = 2 + 3j
y = -1 + 2j
print("\nExample 5 - Complex Arithmetic")
print("Sum:", x + y)
print("Difference:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

# Example 6 - Comparison with complex
a = 1 + 2j
b = 3 + 4j
print("\nExample 6 - Complex Comparison")
print("Equal to:", a == b)
print("Not equal to:", a != b)


# --------- String Data Types ---------
print("\n--- String Data Types ---")

st1 = "ICT Department 3EK1"
print(st1)
print(st1[0])
print(st1[0:4])

st1 = "ICT"
st2 = "Department"
st3 = "3EK1"
print(st1 + st2 + st3)

# Repetition
print(4 * st1)

# Membership
st1 = "ICT Department 3EK1"
print("p" in st1)
print("f" not in st1)


# --------- Collection Data Types ---------
print("\n--- Collection Data Types ---")

# Lists
list1 = [123, 567, 89]
list2 = ["hello", "how", "are"]
list3 = ["hey", 1223, "hello"]
print(list1)
print(list2)
print(list3)

list1 = ["apple", "mango", 123, 345]
list2 = ["grapes"]
print(list1 + list2)

# Dictionaries
dict1 = {"comp": "computer", "sci": "science"}
dict2 = {"123": "computer", 456: "maths"}
print(dict1["comp"])
print(dict2["123"])
print(dict1["comp"] + dict2["123"])

# Sets
my_set = {1, 2, 3, 4, 5}
print(my_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# Tuples
my_tuple = (1, 2, 3, 4, 5)
t1 = (2, 3, 4)
t2 = (5, 6, 7)
print(t1 + t2)


# --------- Post Lab Exercises ---------
print("\n--- Post Lab Exercises ---")

# 1. Display message 5 times
for _ in range(5):
    print("Welcome to Python")

# 2. Display a table (Example: Numbers and Squares)
print("\nNumber\tSquare")
for i in range(1, 6):
    print(i, "\t", i**2)

# 3. Display some results
x, y = 15, 4
print("\nResults:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Power:", x ** y)
