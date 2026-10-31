

# 05-dars — Foydalanuvchi kiritgan ma’lumotlar, tur o‘zgartirish va f-string

**Sana:** 29.10.2026  
**Mavzu:** `input()`, type conversion va f-string

## Dastur faqat oldindan yozilgan ma’lumotlardan iborat bo‘la olmaydi

Dasturlashni endi boshlaganimizda, odatda, `print()` yordamida ekranga ma’lumot chiqaramiz:

```python
print("Salom, dunyo!")
print("Python dasturlash tilini o'rganamiz.")
```

Bu kodlar har safar ishga tushirilganda bir xil natijani beradi. Bunday dastur statik hisoblanadi: unda chop etiladigan ma’lumotlar oldindan belgilangan.

Lekin haqiqiy dasturlarda foydalanuvchining ismi, yoshi, elektron pochta manzili yoki boshqa ma’lumotlari kerak bo‘lishi mumkin. Har bir foydalanuvchi uchun kodni qayta yozish mantiqan to‘g‘ri emas. Dastur foydalanuvchining o‘zidan ma’lumot olishi kerak.

Python'da buning uchun `input()` funksiyasidan foydalanamiz.

## `input()` — foydalanuvchidan ma’lumot olish

`input()` dastur bajarilishini foydalanuvchi Enter tugmasini bosguniga qadar kutadi. Funksiyaga parametr sifatida matn berishimiz mumkin. Bu matn foydalanuvchiga nima kiritishi kerakligini ko‘rsatadi.

```python
name = input("Ismingizni kiriting: ")

print("Salom,", name)
```

Dastur foydalanuvchidan ism kiritishni so‘raydi. Kiritilgan qiymat `name` o‘zgaruvchisiga biriktiriladi.

Yana bir misol:

```python
age = input("Yoshingizni kiriting: ")

print("Sizning yoshingiz:", age)
```

Bu yerda dastur foydalanuvchidan yosh so‘raydi. Ammo muhim bir jihat bor: **`input()` qaytargan qiymat har doim `str` turida bo‘ladi.**

Foydalanuvchi `18` kiritsa ham, Python bu qiymatni son emas, `"18"` matni sifatida qabul qiladi.

Buni `type()` bilan tekshiramiz:

```python
age = input("Yoshingizni kiriting: ")

print(type(age))
```

Natija:

```text
<class 'str'>
```

Bu farq dastur matematik hisob-kitob bajarishi kerak bo‘lganida ayniqsa muhim.

## Nega ma’lumot turini o‘zgartirish kerak?

Tasavvur qiling, foydalanuvchidan yoshini oldik va uning tug‘ilgan yilini taxminan hisoblamoqchimiz:

```python
age = input("Yoshingizni kiriting: ")

birth_year = 2026 - age
```

Bu kod ishlamaydi. Sababi `2026` — `int`, `age` esa `str`. Python butun son bilan matnni ayirish amalini bajara olmaydi. Natijada `TypeError` yuz beradi.

Matnni matn bilan qo‘shish mumkin, ammo bu arifmetik qo‘shish emas:

```python
age = "18"

print(age + "1")
```

Natija:

```text
181
```

Python ikkita matnni birlashtirdi. Demak, matematik amal bajarishdan oldin ma’lumot turini moslashtirishimiz kerak.

## Type conversion — ma’lumot turini o‘zgartirish

Python'da qiymatlarni boshqa turlarga o‘tkazish uchun bir nechta ichki funksiyalar mavjud. Boshlang‘ich bosqichda eng ko‘p ishlatiladiganlari:

- `int()` — butun songa o‘tkazadi.
- `float()` — haqiqiy songa o‘tkazadi.
- `str()` — matnga o‘tkazadi.
- `bool()` — mantiqiy qiymatga o‘tkazadi.

Avval `input()` ishlatmasdan, oddiy o‘zgaruvchilar bilan ko‘rib chiqamiz:

```python
number = "25"

converted_number = int(number)

print(converted_number)
print(type(converted_number))
```

Natija:

```text
25
<class 'int'>
```

`int()` matn ko‘rinishidagi butun sonni haqiqiy `int` qiymatga aylantirdi.

Haqiqiy son bilan ishlash:

```python
price = "19.99"

converted_price = float(price)

print(converted_price)
print(type(converted_price))
```

Natija:

```text
19.99
<class 'float'>
```

Sonni matnga aylantirish ham mumkin:

```python
number = 100

text = str(number)

print(text)
print(type(text))
```

Natija:

```text
100
<class 'str'>
```

Bu usul turli ma’lumotlarni matn bilan birlashtirishda foydali bo‘ladi.

### Konvertatsiya har doim ham muvaffaqiyatli bo‘lavermaydi

Python qiymatni kerakli turga o‘tkaza olmasa, xatolik yuz beradi.

Masalan:

```python
age = int("eighteen")
```

`"eighteen"` matni raqam ko‘rinishida emas. Uni `int()` yordamida butun songa aylantirib bo‘lmaydi. Natijada `ValueError` yuz beradi.

Yana bir holat:

```python
number = int("18.5")
```

Bu ham `ValueError` beradi. Chunki `"18.5"` matnida kasr qismi mavjud va u butun son ko‘rinishida emas.

Ammo quyidagi ikkita holatni farqlash kerak:

```python
print(int(18.5))
print(int("18.5"))
```

Birinchi qatorda `18.5` qiymati `float` bo‘lgani uchun `int()` kasr qismini tashlab, `18` qaytaradi.

Ikkinchi qatorda esa `"18.5"` matnini `int()` bevosita butun songa o‘tkaza olmaydi va `ValueError` yuz beradi.

Eslab qoling: `int()` kasr sonni yaxlitlamaydi, kasr qismini kesib tashlaydi. Masalan, `int(-3.9)` natijasi `-3` bo‘ladi.

Noto‘g‘ri turdagi obyekt berilgan ayrim holatlarda `TypeError` yuz beradi. Masalan, `int(None)` bajarib bo‘lmaydigan konvertatsiyadir. Bu yerda `ValueError` va `TypeError` turli sabablar tufayli yuzaga keladi:

- `ValueError` — tur mos bo‘lishi mumkin, lekin qiymatni shu turga o‘tkazish mumkin emas.
- `TypeError` — bajarilayotgan amal uchun berilgan obyekt turi mos emas.

Yana bir muhim noziklik: `bool()` bilan matnni mantiqiy qiymatga o‘tkazganda, `"False"` matni `False` bo‘lmaydi. Bo‘sh bo‘lmagan matnlar, jumladan `"False"` va `"0"`, `True` qiymatiga o‘tadi. Shu sababli foydalanuvchidan `"True"` yoki `"False"` matnini qabul qilib, uni to‘g‘ridan-to‘g‘ri `bool()` ga berish to‘g‘ri usul emas.

## Konvertatsiyani `input()` bilan birga ishlatish

Endi o‘rganganlarimizni birlashtiramiz:

```python
name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))

print("Ism:", name)
print("Yosh:", age)
print("Keyingi yil yoshingiz:", age + 1)
```

Bu safar `input()` qaytargan matn darhol `int()` yordamida butun songa aylantirildi.

Quyidagi yozuv:

```python
age = int(input("Yoshingizni kiriting: "))
```

mantiqan ikki bosqichdan iborat:

1. `input()` foydalanuvchidan matn qabul qiladi.
2. `int()` olingan matnni butun songa aylantiradi.

Shuning uchun bu yozuv bilan quyidagi kod bir xil mazmunga ega:

```python
age_text = input("Yoshingizni kiriting: ")
age = int(age_text)
```

Agar foydalanuvchi butun son o‘rniga `"eighteen"` yoki `"18.5"` kiritsa, dastur `ValueError` bilan to‘xtaydi. Hozircha bu xatoliklarning sababini tushunish muhim. Keyingi mavzularda `try` va `except` yordamida bunday holatlarni boshqarishni o‘rganishimiz mumkin.

## Yoshdan tug‘ilgan yilni hisoblashdagi muammo

Masalan, foydalanuvchining yoshini bilamiz va tug‘ilgan yilini hisoblamoqchimiz:

```python
age = int(input("Yoshingizni kiriting: "))

birth_year = 2026 - age

print("Siz taxminan", birth_year, "yilda tug'ilgansiz.")
```

Bu oddiy hisoblash ko‘p vaziyatlarda foydali bo‘lishi mumkin. Ammo natija har doim aniq emas.

Nima uchun?

Chunki biz foydalanuvchining tug‘ilgan kuni joriy yilda allaqachon o‘tganmi yoki hali kelmaganmi, bilmaymiz. Masalan, 2026-yil 29-oktabr kuni 20 yoshda bo‘lgan inson 2005-yilda ham, 2006-yilda ham tug‘ilgan bo‘lishi mumkin.

Demak, faqat yoshga qarab tug‘ilgan sananing kunini, oyini va hatto tug‘ilgan yilini har doim aniq topib bo‘lmaydi. Aniq natija uchun tug‘ilgan kun va oy ham kerak bo‘ladi.

Bu misol bizga yana bir narsani ko‘rsatadi: dastur to‘g‘ri ishlashi faqat kodning to‘g‘riligiga emas, balki unga kiritilgan ma’lumotlarning yetarliligiga ham bog‘liq.

## `print()` va f-string

Avvalgi misollarda bir nechta qiymatni chiqarish uchun `print()` ichida verguldan foydalandik:

```python
name = "Ali"
age = 20

print("Ism:", name, "Yosh:", age)
```

Natija:

```text
Ism: Ali Yosh: 20
```

Bu usul qulay, chunki `print()` turli tipdagi qiymatlarni vergul orqali qabul qila oladi va odatda ularning orasiga probel qo‘yadi.

Ammo katta dasturlarda chiqariladigan matnni yanada tartibli va o‘qilishi oson shaklda yozish kerak bo‘ladi. Buning uchun f-string ishlatiladi.

F-string Python 3.6 versiyasida taqdim etilgan. Uning asosiy sintaksisi quyidagicha:

```python
name = "Ali"
age = 20

print(f"Mening ismim {name}, yoshim {age} da.")
```

Natija:

```text
Mening ismim Ali, yoshim 20 da.
```

Bu yerda satr boshidagi `f` Python'ga ushbu matn formatlanadigan satr ekanini bildiradi. Jingalak qavslar `{}` ichiga o‘zgaruvchi yoki ifodalarni yozish mumkin.

Masalan:

```python
a = 10
b = 5

print(f"{a} + {b} = {a + b}")
```

Natija:

```text
10 + 5 = 15
```

F-string ichida faqat o‘zgaruvchilar emas, balki Python ifodalaridan ham foydalanish mumkin.

### Sonlarni formatlash

F-string yordamida sonlarni ham chiroyli ko‘rinishda chiqarish mumkin:

```python
price = 19.9876

print(f"Narx: {price:.2f}")
```

Natija:

```text
Narx: 19.99
```

`:.2f` qiymatni kasr nuqtasidan keyin ikki xona bilan ko‘rsatishni anglatadi.

Yana bir misol:

```python
name = "Ali"
score = 95.5

print(f"{name} imtihondan {score:.1f} ball oldi.")
```

Natija:

```text
Ali imtihondan 95.5 ball oldi.
```

F-string matn va qiymatlarni bitta satr ichida birlashtirishning o‘qilishi oson usulidir.

## Uch xil usulni taqqoslaymiz

Quyidagi kodlarning barchasi bir xil maqsadga xizmat qiladi:

```python
name = "Ali"
age = 20

# Vergul orqali
print("Ism:", name, "Yosh:", age)

# Matnlarni qo'shish orqali
print("Ism: " + name + " Yosh: " + str(age))

# F-string orqali
print(f"Ism: {name} Yosh: {age}")
```

Ikkinchi usulda `age` ni `str()` yordamida matnga aylantirishimiz kerak. Chunki `str` va `int` qiymatlarni `+` orqali bevosita birlashtirib bo‘lmaydi.

F-string esa bunday holatlarda ancha qulay va tushunarli.

## Keng tarqalgan xatolar

Quyidagi holatlarni eslab qolish kerak:

```python
age = input("Yosh: ")
print(age + 1)  # TypeError: str va int ni qo'shib bo'lmaydi
```

```python
age = int(input("Yosh: "))
print(age + 1)  # Foydalanuvchi butun son kiritsa, ishlaydi
```

```python
price = float("19.99")  # To'g'ri
```

```python
price = int("19.99")  # ValueError
```

```python
print("Yosh: " + 20)  # TypeError
```

```python
print(f"Yosh: {20}")  # To'g'ri
```

## Dars yakuni

Bu dars orqali dasturga foydalanuvchidan ma’lumot kiritish imkonini berishni, `input()` qaytargan qiymatning turini tekshirishni, kerakli turga konvertatsiya qilishni va qiymatlarni f-string yordamida formatlashni o‘rgandik.

Eng muhim fikr: **foydalanuvchi kiritgan ma’lumotni ishlatishdan oldin uning turini va qiymati biz kutgan shaklda ekanini tekshirish kerak.**

Keyingi darslarda foydalanuvchi kiritgan ma’lumotlar asosida turli qarorlar qabul qilish, shartlar va mantiqiy ifodalar bilan ishlashga o‘tamiz.

