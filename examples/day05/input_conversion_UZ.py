"""
Day 05 — input(), type conversion va f-string
Sana: 29.10.2026

Ushbu fayl darsda o'rganilgan tushunchalarni amalda ko'rsatadi.
"""

# 1. Foydalanuvchidan ma'lumot olish

print("=== Foydalanuvchi ma'lumotlari ===")

name = input("Ismingizni kiriting: ")
age_text = input("Yoshingizni kiriting: ")

# input() har doim str qaytaradi
print("Kiritilgan yosh:", age_text)
print("Ma'lumot turi:", type(age_text))


# 2. Ma'lumot turini o'zgartirish

age = int(age_text)

print("Konvertatsiyadan keyingi yosh:", age)
print("Yangi ma'lumot turi:", type(age))


# 3. Bir nechta turdagi ma'lumotlarni qabul qilish

height = float(input("Bo'yingizni metrda kiriting (masalan, 1.75): "))
city = input("Qaysi shaharda yashaysiz: ")

print()
print("=== Ma'lumotlar ===")
print("Ism:", name)
print("Yosh:", age)
print("Bo'y:", height)
print("Shahar:", city)


# 4. Kiritilgan ma'lumotlar asosida hisoblash

next_year_age = age + 1

# Bu faqat taxminiy hisoblash.
# Aniq tug'ilgan yilni topish uchun kun va oy ham kerak.
approximate_birth_year = 2026 - age

print()
print("=== Hisob-kitob ===")
print(f"Kelasi yil siz {next_year_age} yoshda bo'lasiz.")
print(f"Siz taxminan {approximate_birth_year}-yilda tug'ilgansiz.")


# 5. Oddiy type conversion misollari

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

# float -> int: kasr qismi kesib tashlanadi, yaxlitlanmaydi
decimal_number = 18.9
integer_number = int(decimal_number)

print(integer_number)  # 18


# 6. bool() bilan konvertatsiya

print()
print("=== Boolean conversion ===")

print(bool(""))        # False
print(bool("False"))   # True
print(bool("0"))       # True
print(bool(0))         # False
print(bool(1))         # True

# Eslatma:
# Bo'sh bo'lmagan har qanday matn True bo'ladi.
# Shuning uchun bool("False") False qiymatini bermaydi.


# 7. print() va f-string

print()
print("=== print() usullarini taqqoslash ===")

student_name = "Ali"
student_age = 20

# Vergul orqali
print("Ism:", student_name, "Yosh:", student_age)

# String concatenation
print("Ism: " + student_name + " Yosh: " + str(student_age))

# f-string orqali
print(f"Ism: {student_name} Yosh: {student_age}")


# 8. F-string ichida ifodalar

a = 10
b = 5

print()
print("=== F-string expressions ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")


# 9. F-string yordamida sonlarni formatlash

price = 19.9876

print()
print("=== Number formatting ===")
print(f"Oddiy ko'rinish: {price}")
print(f"Ikki kasr xonasi bilan: {price:.2f}")


# 10. Xatoliklarni kuzatish
#
# Quyidagi kodlarni bittadan ochib, alohida sinab ko'ring.
# Ularning barchasini bir vaqtda ishga tushirmang,
# chunki xatolik yuz berganda dastur bajarilishi to'xtaydi.

# int("eighteen")   # ValueError
# int("18.5")       # ValueError
# int(None)         # TypeError
# "Age: " + 20      # TypeError
# 2026 - "20"       # TypeError

# Biroq quyidagi amal ishlaydi:
print()
print("int(18.5) =", int(18.5))  # 18