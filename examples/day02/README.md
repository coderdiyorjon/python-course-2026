# Day 02 — Code Examples

Bu papkada darsda ishlatiladigan uchta mustaqil namuna bor.

## `number_systems.py`

Python'ning `bin()`, `oct()`, `hex()`, `int()` va `format()` funksiyalarini ko'rsatadi.

```bat
python examples/day02/number_systems.py
```

## `base_conversion.py`

Butun sonlarni 2 dan 36 gacha bo'lgan asoslar orasida qo'lda o'rganilgan bo'lish-qoldiq algoritmi bilan o'giradi. Manfiy qiymatlar va xato kiritishlar ham tekshiriladi.

```bat
python examples/day02/base_conversion.py
```

Interaktiv qismda son, manba asosi va maqsad asosini kiriting. `q` bilan dasturdan chiqish mumkin.

## `floating_point.py`

Binary floating-point cheklovlarini, `as_integer_ratio()`, `math.isclose()` va `Decimal` turini ko'rsatadi.

```bat
python examples/day02/floating_point.py
```

## Muhim eslatma

`bin()`, `oct()` va `hex()` natijani prefiks bilan qaytaradi (`0b`, `0o`, `0x`). `int(text, base)` esa matnni ko'rsatilgan asosda o'qib, butun son qiymatiga aylantiradi. `float` ning ko'rinadigan natijasi ichkaridagi qiymatni o'nlikda to'liq aks ettirishi shart emas.
