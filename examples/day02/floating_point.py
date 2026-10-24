"""Day 02: binary floating-point and decimal arithmetic examples."""

from decimal import Decimal
from math import isclose

print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("0.1 with 20 digits after decimal point:", format(0.1, ".20f"))

# Aslida saqlanayotgan binary float qiymati aniq kasr ko'rinishida.
print("0.1 as a ratio:", (0.1).as_integer_ratio())

# Sonli natijalarni tolerans bilan taqqoslash.
print("isclose(0.1 + 0.2, 0.3):", isclose(0.1 + 0.2, 0.3))

# Decimal bilan stringdan boshlash o'nlik qiymatni aniq yaratadi.
decimal_sum = Decimal("0.1") + Decimal("0.2")
print("Decimal sum:", decimal_sum)
print("Decimal equality:", decimal_sum == Decimal("0.3"))

# Decimal(float) float ichidagi taxminiy qiymatni ham olib kiradi.
print("Decimal(0.1):", Decimal(0.1))
print('Decimal("0.1"):', Decimal("0.1"))
