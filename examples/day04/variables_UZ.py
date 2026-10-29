"""04-kun: o‘zgaruvchilar va ma’lumot turlari."""

student_name = "Ali"
age = 19
course_price = 125.50
is_enrolled = True
final_grade = None

print("O‘quvchi:", student_name)
print("Yoshi:", age)
print("Kurs narxi:", course_price)
print("Kursga yozilganmi:", is_enrolled)
print("Yakuniy baho:", final_grade)

print("\nQiymatlarning turlari:")
print(type(student_name))
print(type(age))
print(type(course_price))
print(type(is_enrolled))
print(type(final_grade))

print("\nDinamik tiplash:")
value = 42
print(value, type(value))
value = "qirq ikki"
print(value, type(value))
value = 42.0
print(value, type(value))

print("\nNomlarni qayta bog‘lash:")
first = 7
second = first
first = 9
print("first =", first)
print("second =", second)

print("\nBir obyektga ikki nom:")
items_a = [1, 2]
items_b = items_a
items_b.append(3)
print("items_a =", items_a)
print("items_b =", items_b)
