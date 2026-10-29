"""День 04: переменные и типы данных."""

student_name = "Ali"
age = 19
course_price = 125.50
is_enrolled = True
final_grade = None

print("Ученик:", student_name)
print("Возраст:", age)
print("Стоимость курса:", course_price)
print("Записан на курс:", is_enrolled)
print("Итоговая оценка:", final_grade)

print("\nТипы значений:")
print(type(student_name))
print(type(age))
print(type(course_price))
print(type(is_enrolled))
print(type(final_grade))

print("\nДинамическая типизация:")
value = 42
print(value, type(value))
value = "сорок два"
print(value, type(value))
value = 42.0
print(value, type(value))

print("\nПовторное связывание имён:")
first = 7
second = first
first = 9
print("first =", first)
print("second =", second)

print("\nДва имени ссылаются на один объект:")
items_a = [1, 2]
items_b = items_a
items_b.append(3)
print("items_a =", items_a)
print("items_b =", items_b)
