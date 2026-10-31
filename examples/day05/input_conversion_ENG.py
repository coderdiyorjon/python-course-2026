"""
Day 05 — input(), type conversion, and f-strings
Date: 29 October 2026

This file demonstrates the concepts covered in the lesson.
"""

# 1. Receiving input from the user

print("=== User information ===")

name = input("Enter your name: ")
age_text = input("Enter your age: ")

# input() always returns str
print("Entered age:", age_text)
print("Data type:", type(age_text))


# 2. Converting the data type

age = int(age_text)

print("Age after conversion:", age)
print("New data type:", type(age))


# 3. Receiving values of different types

height = float(input("Enter your height in meters (for example, 1.75): "))
city = input("Which city do you live in: ")

print()
print("=== Information ===")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("City:", city)


# 4. Calculations using user input

next_year_age = age + 1

# This is only an estimate.
# We also need the day and month to determine the exact birth year.
approximate_birth_year = 2026 - age

print()
print("=== Calculations ===")
print(f"Next year, you will be {next_year_age} years old.")
print(f"You were approximately born in {approximate_birth_year}.")


# 5. Basic type conversion examples

print()
print("=== Type conversion ===")

# str -> int
number_text = "25"
number = int(number_text)

print(number)
print(type(number))

# str -> float
price_text = "19.99"
price = float(price_text)

print(price)
print(type(price))

# int -> str
user_id = 100
user_id_text = str(user_id)

print(user_id_text)
print(type(user_id_text))

# float -> int: the fractional part is truncated, not rounded
decimal_number = 18.9
integer_number = int(decimal_number)

print(integer_number)  # 18


# 6. Boolean conversion with bool()

print()
print("=== Boolean conversion ===")

print(bool(""))        # False
print(bool("False"))   # True
print(bool("0"))       # True
print(bool(0))         # False
print(bool(1))         # True

# Note:
# Any non-empty string evaluates to True.
# Therefore, bool("False") does not return False.


# 7. Comparing print() and f-strings

print()
print("=== Comparing print() approaches ===")

student_name = "Ali"
student_age = 20

# Using commas
print("Name:", student_name, "Age:", student_age)

# String concatenation
print("Name: " + student_name + " Age: " + str(student_age))

# Using an f-string
print(f"Name: {student_name} Age: {student_age}")


# 8. Expressions inside f-strings

a = 10
b = 5

print()
print("=== F-string expressions ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")


# 9. Formatting numbers with f-strings

price = 19.9876

print()
print("=== Number formatting ===")
print(f"Default representation: {price}")
print(f"With two decimal places: {price:.2f}")


# 10. Exploring errors
#
# Uncomment and execute these statements one at a time.
# Do not run them all at once because execution stops
# when an error occurs.

# int("eighteen")   # ValueError
# int("18.5")       # ValueError
# int(None)         # TypeError
# "Age: " + 20      # TypeError
# 2026 - "20"       # TypeError

# However, this operation works:
print()
print("int(18.5) =", int(18.5))  # 18