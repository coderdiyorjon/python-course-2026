# 04-kun — O‘zgaruvchilar, nomlash va asosiy ma’lumot turlari

- **Sana:** 27.10.2026
- **Modul:** Python asoslari
- **Daraja:** Beginner

## Darsning mazmuni

Dastur ma’lumotni qabul qiladi, uni qayta ishlaydi va natija chiqaradi. Bu ma’lumotlar bilan ishlash uchun ularni dastur ichida nomlar orqali murojaat qiladigan qilib saqlashimiz kerak. Shu yerda o‘zgaruvchi tushunchasi paydo bo‘ladi.

Python’da o‘zgaruvchini tushunish uchun uni shunchaki “ichiga qiymat solinadigan quti” deb tasavvur qilish boshlang‘ich bosqichda qulay. Lekin bu faqat soddalashtirilgan model. Aniqroq aytganda, Python’da o‘zgaruvchi nomi obyektga bog‘lanadi. Nom — obyektning o‘zi emas; u obyektga murojaat qilish uchun ishlatiladi.

```python
age = 20
name = "Ali"
height = 1.78

print(name)
print(age)
print(height)
```

Bu kodda `name`, `age` va `height` nomlari turli qiymatlarga bog‘langan. `=` belgisi bu yerda matematik tenglik emas, o‘ng tomondagi ifodaning qiymatini chap tomondagi nomga bog‘lash amalidir. Shuning uchun `age = age + 1` matematik tenglama emas: avval `age + 1` hisoblanadi, keyin hosil bo‘lgan qiymat yana `age` nomiga bog‘lanadi.

## O‘zgaruvchi va qiymat

O‘zgaruvchi — dastur ichida qiymatga nom orqali murojaat qilish usuli. Qiymat esa dastur ishlatayotgan ma’lumotning o‘zi.

```python
score = 100
score = 125
print(score)  # 125
```

Ikkinchi tayinlashdan keyin `score` nomi `125` qiymatiga bog‘langan. Avvalgi `100` qiymati boshqa nom orqali ishlatilmayotgan bo‘lsa, unga murojaat qilishning imkoni qolmaydi va Python uni xotiradan bo‘shatishi mumkin. Xotirani boshqarishning aniq ichki mexanizmi Python implementatsiyasiga bog‘liq.

Bir nechta nom bir obyektga murojaat qilishi ham mumkin:

```python
first = [1, 2, 3]
second = first
second.append(4)

print(first)   # [1, 2, 3, 4]
print(second)  # [1, 2, 3, 4]
```

Bu misolda ro‘yxat o‘zgartiriladigan obyekt. `second = first` ro‘yxatning yangi nusxasini yaratmaydi; ikkala nom ham o‘sha ro‘yxat obyektiga murojaat qiladi. Bu misol keyingi darslarda obyektlar va o‘zgaruvchan ma’lumotlar mavzusiga qaytish uchun tayyorgarlikdir.

## Ma’lumot turlari nima uchun kerak?

Dastur `25`, `25.0`, `"25"` va `True` qiymatlarini bir xil deb qabul qilmaydi. Ularning ko‘rinishi o‘xshash bo‘lishi mumkin, ammo turi va ular ustida bajarish mumkin bo‘lgan amallar farq qiladi.

```python
print(25, type(25))
print(25.0, type(25.0))
print("25", type("25"))
print(True, type(True))
```

Asosiy boshlang‘ich turlar:

- `int` — butun sonlar: `10`, `-4`, `0`.
- `float` — suzuvchi nuqtali sonlar: `3.14`, `-0.5`.
- `str` — matn: `"Python"`, `'salom'`.
- `bool` — mantiqiy qiymatlar: `True` va `False`.
- `NoneType` — qiymat yo‘qligini ifodalovchi `None`.
- `list` — tartiblangan, o‘zgartiriladigan elementlar ketma-ketligi.
- `tuple` — tartiblangan, odatda yaratilgandan keyin o‘zgartirilmaydigan ketma-ketlik.
- `dict` — kalit-qiymat juftliklari.
- `set` — takrorlanmaydigan elementlar to‘plami.

Bu ro‘yxat Python’dagi barcha turlarni qamrab olmaydi; hozircha asosiy tushunchalar uchun yetarli.

## Primitive va object tushunchalari

Turli dasturlash tillari ma’lumot turlarini turlicha tashkil qiladi. Masalan, Java’da `int` va `boolean` kabi primitive turlar obyekt turlaridan alohida ko‘riladi. JavaScript’da esa sonlar va mantiqiy qiymatlar kabi primitive qiymatlar obyektlardan farqlanadi, garchi ayrim amallarda ular vaqtincha obyektga o‘xshash imkoniyatlardan foydalanishi mumkin.

Python’da esa muhim qoida bor: **Python’da deyarli barcha qiymatlar obyekt sifatida ifodalanadi**. `int`, `float`, `bool`, `str`, `list`, `dict` va hatto funksiyalar ham obyektlardir. Shuning uchun boshqa tillardagi “primitive type” tushunchasini Python’ga to‘g‘ridan-to‘g‘ri ko‘chirish to‘g‘ri emas.

Python’da `int` oddiy ko‘rinsa ham, u obyekt. Buni `type()` orqali ko‘rish mumkin:

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
print(type([1, 2]))   # <class 'list'>
```

Dastlabki dars uchun obyektning barcha ichki tuzilishini o‘rganish shart emas. Hozir eslab qolish kerak bo‘lgan narsa: nom obyektga bog‘lanadi, obyektning turi esa qanday amallarni bajarish mumkinligiga ta’sir qiladi.

## O‘zgaruvchilar qanday “saqlanadi”?

Darsda xotira haqidagi sodda tasavvurdan foydalanish mumkin, lekin buni aniq fizik manzil haqidagi va’da deb qabul qilmaslik kerak. Python tili o‘zgaruvchi nomi va obyekt o‘rtasidagi bog‘lanishni belgilaydi; obyektlar xotirada aynan qanday joylashtirilishi esa interpreter implementatsiyasiga bog‘liq.

```python
x = 10
y = x
x = 20

print(x)  # 20
print(y)  # 10
```

`y = x` bajarilganda `y` nomi hozirgi `10` obyektiga bog‘lanadi. Keyin `x = 20` bajarilganda `x` boshqa obyektga bog‘lanadi, lekin `y` avvalgi qiymatga bog‘langanicha qoladi.

Bu holat `int` kabi o‘zgarmas (immutable) obyektlar bilan tushunarli. Ro‘yxat kabi o‘zgartiriladigan (mutable) obyektlarda esa nomlar orasidagi bog‘lanish sababli kutilmagan natijalar yuzaga kelishi mumkin; bu mavzu keyinroq chuqurroq o‘rganiladi.

## Python dinamik tiplanadi

Python’da o‘zgaruvchining turini oldindan qat’iy e’lon qilish talab qilinmaydi. O‘zgaruvchi nomi turli vaqtlarda turli turdagi obyektlarga bog‘lanishi mumkin.

```python
value = 10
print(value, type(value))

value = "ten"
print(value, type(value))

value = 10.5
print(value, type(value))
```

Natijada `value` avval `int`, keyin `str`, so‘ng `float` obyektiga bog‘lanadi. Bu Python’da dinamik tiplash deyiladi.

Muhim farq: obyektning turi o‘z-o‘zidan o‘zgarmaydi. `10` butun son obyektidir; keyinchalik `value = "ten"` bajarilganda o‘zgaruvchi nomi boshqa turdagi obyektga bog‘lanadi. Demak, “o‘zgaruvchining tipi o‘zgardi” deyish kundalik tushuntirish uchun qulay, lekin aniqroq ta’rif — “nom endi boshqa turdagi obyektga bog‘landi”.

## `type()` funksiyasi

`type(value)` berilgan qiymatning turini ko‘rsatadi. U ayniqsa yangi boshlovchilarga qiymatning matnmi, butun sonmi yoki boshqa turmi ekanini tekshirishga yordam beradi.

```python
age = 18
price = 12.5
title = "Python"
is_ready = False
nothing = None

print(type(age))
print(type(price))
print(type(title))
print(type(is_ready))
print(type(nothing))
```

`type()` bilan ishlashda natija odatda `<class 'int'>` kabi ko‘rinadi. Bu Python’da tur ham obyekt ekanini eslatadi. Oddiy dasturlarda tur tekshirish uchun ko‘pincha `isinstance()` ham ishlatiladi, lekin bu farqni keyingi darslarda batafsil o‘rganish mumkin.

## O‘zgaruvchi nomlash qoidalari

O‘zgaruvchi nomi ma’lumotning ma’nosini tushunarli qilishi kerak. Quyidagi nomlar Python’da yaroqli:

```python
name = "Ali"
age = 20
AGE = 21
AGE2 = 22
_name = "private convention"
first_name = "Ali"
firstName = "Ali"
user2 = "guest"
```

Asosiy sintaksis qoidalari:

1. Nom harf yoki pastki chiziq (`_`) bilan boshlanishi mumkin.
2. Nom raqam bilan boshlana olmaydi.
3. Keyingi belgilar orasida harflar, raqamlar va pastki chiziq ishlatilishi mumkin.
4. Bo‘sh joy nom ichida bo‘lishi mumkin emas.
5. Katta-kichik harflar farqlanadi: `name`, `Name` va `NAME` uchta alohida nom.
6. `if`, `for`, `class`, `return` kabi Python kalit so‘zlarini o‘zgaruvchi nomi sifatida ishlatib bo‘lmaydi.
7. `!age`, `(publicKey` yoki `private key` kabi nomlar yaroqsiz, chunki ular identifikator qoidalariga mos kelmaydi.

Misollar:

```python
# Yaroqli
public_key = "abc"
_name = "Ali"
age2 = 18
FirstName = "Ali"

# Yaroqsiz — quyidagilarni izohdan chiqarib ishga tushirmang:
# 5name = "Ali"       # raqamdan boshlanadi
# private key = "x"   # bo'sh joy bor
# !age = 18            # ! belgisi bilan boshlanadi
# class = "Python"     # kalit so'z
```

Python Unicode identifikatorlarni ham qo‘llab-quvvatlaydi, shuning uchun faqat ingliz harflari bilan cheklanmaydi. Lekin jamoaviy loyihalarda o‘qilishi va vositalar bilan mosligi uchun odatda inglizcha, ASCII belgilaridan iborat nomlar tavsiya etiladi.

## Sintaksis va yaxshi uslub bir xil narsa emas

`firstName` sintaktik jihatdan yaroqli. Lekin Python hamjamiyatidagi odatiy uslub — o‘zgaruvchilar uchun `snake_case`, ya’ni `first_name` yozuvidir. Bu sintaksis talabi emas, o‘qilishi va bir xillik uchun qo‘llanadigan konvensiya.

Yaxshi nomlar:

```python
student_name = "Ali"
total_price = 150
is_logged_in = True
number_of_attempts = 3
```

Yomonroq nomlar:

```python
x = "Ali"
tp = 150
a1 = True
n = 3
```

Qisqa nomlar `i`, `x` kabi juda маҳаллий kontekstlarda o‘rinli bo‘lishi mumkin, ammo odatda ma’noli nom tanlash kerak.

`_name` kabi bitta pastki chiziq bilan boshlanuvchi nom Python’da ko‘pincha “ichki foydalanish uchun” degan konvensiyani bildiradi. Bu avtomatik maxfiylik yoki qat’iy ruxsat cheklovi emas.

Shuningdek, `list`, `str`, `type` kabi ichki nomlarni o‘zgaruvchi nomi sifatida ishlatishdan saqlaning. Masalan, `list = [1, 2]` yozilsa, shu scope ichida `list()` funksiyasiga murojaat qilish qiyinlashadi.

## Amaliy tajriba

Quyidagi kodni IDLE’da yozing va natijalarni kuzating:

```python
value = 100
print(value, type(value))

value = "100"
print(value, type(value))

value = 100.0
print(value, type(value))

a = 7
b = a
a = 9
print(a, b)
```

O‘zingizga savol bering: nima uchun `100`, `"100"` va `100.0` bir xil tur emas? Nima uchun oxirgi qatorda `a` va `b` turli qiymatlarni ko‘rsatadi?

## Dars yakunida

O‘quvchi quyidagilarni tushuntira olishi kerak:

- o‘zgaruvchi nomi va qiymat orasidagi farq;
- `=` tayinlash operatorining vazifasi;
- `type()` yordamida tur ko‘rish;
- Python’da dinamik tiplash nimani anglatishi;
- Python qiymatlari obyekt sifatida qaralishi;
- sintaktik jihatdan yaroqli nom va yaxshi uslub orasidagi farq;
- kalit so‘zlar, raqamdan boshlanish, bo‘sh joy va case sensitivity qoidalari.

## O‘qituvchi uchun qayd

Quyidagilarni faqat darsda haqiqatan ko‘rib chiqqaningizdan keyin belgilang:

- [ ] O‘zgaruvchi tushunchasi tushuntirildi.
- [ ] Asosiy ma’lumot turlari ko‘rsatildi.
- [ ] Primitive va object tushunchalari tillararo taqqoslandi.
- [ ] Python’da qiymatlarning obyekt ekani izohlandi.
- [ ] Dinamik tiplash va `type()` amalda ko‘rsatildi.
- [ ] O‘zgaruvchi nomlash qoidalari misollar bilan ko‘rsatildi.
- [ ] Yaxshi nomlash uslubi muhokama qilindi.
