# 04-kun — Mustaqil topshiriqlar

Ushbu topshiriqlar o‘zgaruvchilar, ma’lumot turlari, `type()` va nomlash qoidalarini mustahkamlash uchun beriladi. Har bir javobni shunchaki taxmin qilish emas, sababini tushuntirishga harakat qiling.

## 1. Natijani oldindan ayting

Quyidagi kodni ishga tushirishdan oldin har bir `print()` nima chiqarishini yozing. Keyin kodni ishga tushirib, javobingizni tekshiring.

```python
value = 12
print(value, type(value))

value = "12"
print(value, type(value))

value = 12.0
print(value, type(value))

value = True
print(value, type(value))
```

Nima uchun qiymatlar ko‘rinish jihatidan o‘xshash bo‘lsa ham, turlari turlicha?

## 2. Nom qayta bog‘langanda

```python
number = 5
other = number
number = 8

print(number)
print(other)
```

Natijani yozing va `other` nima sababdan `8` bo‘lmasligini tushuntiring.

## 3. Yaroqli va yaroqsiz nomlar

Quyidagi nomlarni uch guruhga ajrating: **yaroqli**, **yaroqsiz**, **yaroqli, lekin uslub nuqtayi nazaridan unchalik yaxshi emas**.

- `user_name`
- `2user`
- `_count`
- `first name`
- `class`
- `total2`
- `FirstName`
- `list`
- `user-name`
- `AGE`

Yaroqsiz nomlarning sababini yozing. `list` nima uchun sintaktik jihatdan yaroqli bo‘lsa-da, o‘zgaruvchi nomi sifatida tavsiya etilmasligini tushuntiring.

## 4. Turini tekshiring

Quyidagi qiymatlar uchun `type()` ishlatadigan kod yozing:

- butun son;
- kasr son;
- matn;
- mantiqiy qiymat;
- `None`;
- ro‘yxat;
- lug‘at (`dict`).

Har biriga o‘zingiz misol tanlang.

## 5. Bir xil ko‘ringan qiymatlar

Quyidagi qiymatlar o‘rtasidagi farqni izohlang:

```python
a = 7
b = 7.0
c = "7"
```

Ularning turlarini tekshiring. Qaysi amallar natijasida xato yuzaga kelishi mumkinligini sinab ko‘ring.

## 6. Obyektga ikkita nom

```python
first = [1, 2]
second = first
second.append(3)

print(first)
print(second)
```

Natijani tushuntiring. Nima uchun bu holat `number = 5; other = number; number = 8` misolidan farq qiladi? Hozircha “mutable” va “immutable” atamalarini o‘z so‘zingiz bilan izohlash kifoya.

## 7. Nomlarni yaxshilang

Quyidagi nomlarni tushunarli Python uslubiga o‘zgartiring:

- `x` — foydalanuvchining yoshi;
- `tp` — buyurtmaning umumiy narxi;
- `a1` — foydalanuvchi tizimga kirgan-kirmaganini bildiruvchi qiymat;
- `n` — urinishlar soni.

## 8. Challenge

`student_profile.py` nomli fayl yarating. Unda quyidagi ma’lumotlarni alohida o‘zgaruvchilarda saqlang:

- o‘quvchining ismi;
- yoshi;
- kurs nomi;
- kursni davom ettirayotgani haqida mantiqiy qiymat;
- hozircha belgilanmagan yakuniy baho (`None`).

Har bir o‘zgaruvchini `print()` bilan chiqaring va `type()` orqali turini ham ko‘rsating. Nomlarni `snake_case` uslubida tanlang.

## Baholash mezonlari

- Natijalar to‘g‘ri taxmin qilingan va tekshirilgan.
- Yaroqsiz nomlarning sabablari to‘g‘ri tushuntirilgan.
- `type()` natijalari to‘g‘ri talqin qilingan.
- Bir nomni qayta bog‘lash va bir obyektga bir nechta nom bog‘lanishi farqlangan.
- Kod o‘qilishi oson nomlardan foydalanadi.
