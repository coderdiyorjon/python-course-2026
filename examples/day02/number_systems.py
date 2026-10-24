"""Day 02: Python built-ins for common number-system conversions."""

# Python'da sonlar odatda integer qiymat sifatida saqlanadi,
# bin(), oct() va hex() esa ularning boshqa asosdagi yozuvini qaytaradi.
number = 45

print("Decimal:", number)
print("Binary: ", bin(number))
print("Octal:  ", oct(number))
print("Hex:    ", hex(number))

# Stringni ma'lum asosda integerga aylantirish.
print('"101101" base 2 ->', int("101101", 2))
print('"55" base 8 ->', int("55", 8))
print('"2D" base 16 ->', int("2D", 16))

# format() prefikssiz ko'rinish qaytaradi.
print("Binary without prefix:", format(number, "b"))
print("Octal without prefix: ", format(number, "o"))
print("Hex without prefix:   ", format(number, "X"))

# 8 bit sifatida ko'rsatish uchun chap tomonga nol to'ldirish.
print("8-bit binary:", format(number, "08b"))

# Eslatma: matn ichidagi raqamlarning o'zi shu asosda ruxsat etilgan
# bo'lishi kerak. Masalan, '2' belgisi binary raqam emas.
try:
    print(int("102", 2))
except ValueError as error:
    print("Kutilgan xato:", error)
