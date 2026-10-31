"""
Урок 05 — input(), преобразование типов и f-строки
Дата: 29 октября 2026 года

В этом файле демонстрируются понятия, изученные на уроке.
"""

# 1. Получение данных от пользователя

print("=== Информация о пользователе ===")

name = input("Введите ваше имя: ")
age_text = input("Введите ваш возраст: ")

# input() всегда возвращает str
print("Введённый возраст:", age_text)
print("Тип данных:", type(age_text))


# 2. Преобразование типа данных

age = int(age_text)

print("Возраст после преобразования:", age)
print("Новый тип данных:", type(age))


# 3. Получение данных разных типов

height = float(input("Введите ваш рост в метрах (например, 1.75): "))
city = input("В каком городе вы живёте: ")

print()
print("=== Данные ===")
print("Имя:", name)
print("Возраст:", age)
print("Рост:", height)
print("Город:", city)


# 4. Вычисления на основе введённых данных

next_year_age = age + 1

# Это только приблизительный расчёт.
# Для определения точного года рождения нужны также день и месяц.
approximate_birth_year = 2026 - age

print()
print("=== Вычисления ===")
print(f"В следующем году вам будет {next_year_age} лет.")
print(f"Вы родились приблизительно в {approximate_birth_year} году.")


# 5. Простые примеры преобразования типов

print()
print("=== Преобразование типов ===")

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

# float -> int: дробная часть отбрасывается, а не округляется
decimal_number = 18.9
integer_number = int(decimal_number)

print(integer_number)  # 18


# 6. Преобразование в bool()

print()
print("=== Преобразование в Boolean ===")

print(bool(""))        # False
print(bool("False"))   # True
print(bool("0"))       # True
print(bool(0))         # False
print(bool(1))         # True

# Примечание:
# Любая непустая строка преобразуется в True.
# Поэтому bool("False") не возвращает False.


# 7. Сравнение print() и f-строк

print()
print("=== Сравнение способов вывода ===")

student_name = "Ali"
student_age = 20

# Использование запятых
print("Имя:", student_name, "Возраст:", student_age)

# Объединение строк
print("Имя: " + student_name + " Возраст: " + str(student_age))

# Использование f-строки
print(f"Имя: {student_name} Возраст: {student_age}")


# 8. Выражения внутри f-строк

a = 10
b = 5

print()
print("=== Выражения в f-строках ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")


# 9. Форматирование чисел с помощью f-строк

price = 19.9876

print()
print("=== Форматирование чисел ===")
print(f"Обычное представление: {price}")
print(f"С двумя знаками после запятой: {price:.2f}")


# 10. Изучение ошибок
#
# Раскомментируйте и выполните эти выражения по одному.
# Не запускайте их все одновременно, поскольку выполнение
# программы прекращается при возникновении ошибки.

# int("eighteen")   # ValueError
# int("18.5")       # ValueError
# int(None)         # TypeError
# "Age: " + 20      # TypeError
# 2026 - "20"       # TypeError

# Однако следующая операция работает:
print()
print("int(18.5) =", int(18.5))  # 18