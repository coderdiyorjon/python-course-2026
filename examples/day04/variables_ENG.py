"""Day 04: variables and data types."""

student_name = "Ali"
age = 19
course_price = 125.50
is_enrolled = True
final_grade = None

print("Student:", student_name)
print("Age:", age)
print("Course price:", course_price)
print("Enrolled:", is_enrolled)
print("Final grade:", final_grade)

print("\nValue types:")
print(type(student_name))
print(type(age))
print(type(course_price))
print(type(is_enrolled))
print(type(final_grade))

print("\nDynamic typing:")
value = 42
print(value, type(value))
value = "forty-two"
print(value, type(value))
value = 42.0
print(value, type(value))

print("\nRebinding names:")
first = 7
second = first
first = 9
print("first =", first)
print("second =", second)

print("\nTwo names referring to one object:")
items_a = [1, 2]
items_b = items_a
items_b.append(3)
print("items_a =", items_a)
print("items_b =", items_b)
