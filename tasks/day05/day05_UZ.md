

# 05-dars — Amaliy topshiriqlar

**Mavzu:** `input()`, type conversion va f-string

Ushbu topshiriqlar darsda o‘rganilgan bilimlarni mustahkamlash uchun tuzilgan. Maqsad — foydalanuvchidan qiymat qabul qilish, ularning turlarini to‘g‘ri boshqarish va natijalarni f-string yordamida chiqarish.

## 1. Tanishuv dasturi

Foydalanuvchidan ismi, familiyasi va yoshini so‘raydigan dastur yozing. Kiritilgan ma’lumotlarni quyidagi shaklda chiqaring:

```text
Salom, Ali Valiyev!
Siz 20 yoshdasiz.
```

Talablar:
- Ism va familiya `str` sifatida saqlansin.
- Yosh `int` ga aylantirilsin.
- Natija f-string yordamida chiqarilsin.

## 2. Keyingi yilgi yosh

Foydalanuvchidan yoshini so‘rang va kelasi yil nechchi yoshga kirishini hisoblang.

Masalan:

```text
Yoshingizni kiriting: 20
Kelasi yil siz 21 yoshda bo'lasiz.
```

Yoshni `int()` orqali konvertatsiya qilishni unutmang.

## 3. Tug‘ilgan yilni taxmin qilish

Foydalanuvchidan yoshini so‘rang va `2026 - age` formulasi orqali taxminiy tug‘ilgan yilini hisoblang.

Natijani quyidagiga o‘xshash shaklda chiqaring:

```text
Siz taxminan 2006-yilda tug'ilgansiz.
```

**O‘ylab ko‘ring:** nima uchun bu natija har doim ham aniq bo‘lmaydi? Tug‘ilgan kun va oy ma’lum bo‘lmasa, qanday noaniqlik qoladi?

## 4. Oddiy kalkulyator

Foydalanuvchidan ikkita son kiriting va ularning quyidagi natijalarini chiqaring:

- Yig‘indisi
- Ayirmasi
- Ko‘paytmasi
- Bo‘linmasi

Talablar:
- Qiymatlarni `float()` yordamida qabul qiling.
- Natijalarni f-string yordamida chiqaring.
- Bo‘lish uchun ikkinchi son nol bo‘lmasligi kerak. Hozircha buni shart operatorisiz ham tekshirib, qanday muammo yuzaga kelishini alohida kuzatib ko‘ring.

## 5. Do‘kon hisob-kitobi

Foydalanuvchidan mahsulot nomi, uning narxi va miqdorini so‘rang. Umumiy narxni hisoblang.

Masalan:

```text
Mahsulot nomi: Notebook
Narxi: 12.5
Miqdori: 3

Mahsulot: Notebook
Bir dona narxi: 12.50
Miqdori: 3
Jami: 37.50
```

Talablar:
- Narx `float` bo‘lsin.
- Miqdor `int` bo‘lsin.
- Jami narx `narx * miqdor` orqali hisoblansin.
- Pul qiymatlari f-string yordamida ikki kasr xonasi bilan chiqarilsin.

## 6. Konvertatsiya tajribasi

Quyidagi ifodalarni alohida-alohida bajarib, natijalarini va xatoliklarini kuzating:

```python
int("25")
int("25.5")
int(25.5)

float("25")
float("25.5")
float("hello")

str(25)
str(25.5)

bool("")
bool("False")
bool("0")
bool(0)
bool(1)
```

Har bir natija nima sababdan shunday bo‘lganini izohlashga harakat qiling. Xatolik yuz bergan ifodalarni ham alohida qayd eting.

## 7. Mini-loyiha: Shaxsiy ma’lumotlar kartasi

Foydalanuvchidan quyidagi ma’lumotlarni qabul qiladigan kichik dastur yarating:

- Ism va familiya
- Yosh
- Shahar
- Bo‘yi (metrda, masalan `1.75`)
- Sevimli dasturlash tili

Dastur ushbu ma’lumotlardan foydalanib, tartibli profil chiqarsin. Barcha qiymatlar mos turga o‘tkazilsin va natija f-string yordamida shakllantirilsin.

Masalan:

```text
========== PROFILE ==========
Name: Ali Valiyev
Age: 20
City: Tashkent
Height: 1.75 m
Favorite language: Python
=============================
```

## Qo‘shimcha savollar

1. `input()` nima uchun har doim `str` qaytaradi?
2. `int("12")` va `int("12.5")` orasidagi farq nima?
3. `int(12.9)` qanday natija qaytaradi? Nima uchun?
4. `ValueError` va `TypeError` o‘rtasidagi farq nima?
5. Nima uchun faqat yoshga qarab aniq tug‘ilgan sanani topib bo‘lmaydi?
6. `print("Age:", age)` va `print(f"Age: {age}")` o‘rtasida qanday farq bor?
7. F-string qaysi Python versiyasida taqdim etilgan?
8. `bool("False")` nima uchun `False` emas?

