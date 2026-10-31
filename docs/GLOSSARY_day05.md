

# Day 05 — Ma’lumotnoma

**Mavzu:** `input()`, type conversion va f-string  
**Sana:** 29.10.2026

Ushbu hujjat 05-darsda ishlatilgan asosiy tushunchalar, sintaksis va keng tarqalgan xatolarni tez takrorlash uchun mo‘ljallangan.

## `input()` qanday ishlaydi?

`input()` foydalanuvchidan bitta satr ma’lumot qabul qiladi. Foydalanuvchi Enter tugmasini bosmaguncha dastur kutib turadi.

```python
name = input("Ismingizni kiriting: ")
```

Bu yerda `input()` qaytargan qiymat `name` o‘zgaruvchisiga biriktiriladi.

**Muhim:** `input()` har doim `str` qaytaradi. Raqam kiritilishi ham bu qoidani o‘zgartirmaydi.

```python
age = input("Yoshingizni kiriting: ")

print(type(age))  # <class 'str'>
```

`input()` satr oxiridagi Enter belgisi (`newline`)ni natijaga qo‘shmaydi, ammo kiritilgan matnning boshidagi yoki oxiridagi probellarni avtomatik olib tashlamaydi.

## Type conversion — tur o‘zgartirish

Tur o‘zgartirish qiymatni bir ma’lumot turidan boshqasiga o‘tkazishdir. Buni Python'dagi ichki funksiyalar yordamida bajaramiz.

| Funksiya | Vazifasi | Misol | Natija |
|---|---|---|---|
| `int()` | Butun songa o‘tkazish | `int("25")` | `25` |
| `float()` | Haqiqiy songa o‘tkazish | `float("19.5")` | `19.5` |
| `str()` | Matnga o‘tkazish | `str(100)` | `"100"` |
| `bool()` | Mantiqiy qiymatga o‘tkazish | `bool(0)` | `False` |

### `int()`

```python
int("25")    # 25
int(18.9)    # 18
int(-3.9)    # -3
```

`int()` kasr sonni yaxlitlamaydi. Kasr qismini nol tomonga qarab kesib tashlaydi.

Quyidagi ifodalar bir xil emas:

```python
int(18.5)      # 18
int("18.5")    # ValueError
```

Birinchi holatda argument `float`, ikkinchisida esa `str`.

### `float()`

```python
float("19.99")   # 19.99
float("25")      # 25.0
float(10)        # 10.0
```

O‘nli kasr sonni matn ko‘rinishida kiritganda nuqta ishlatiladi: `"19.99"`. `"19,99"` odatiy `float()` konvertatsiyasi uchun to‘g‘ri format emas.

### `str()`

```python
str(100)       # "100"
str(19.5)      # "19.5"
str(True)      # "True"
```

Bu funksiya qiymatning matn ko‘rinishini qaytaradi. Masalan, sonni boshqa matn bilan birlashtirishdan oldin uning matn ko‘rinishiga o‘tish kerak bo‘lishi mumkin.

### `bool()`

Python'da quyidagi qiymatlar `False` hisoblanadi:

- `False`
- `None`
- `0`, `0.0` kabi nol qiymatlar
- `""` kabi bo‘sh satr
- `[]`, `()`, `{}` kabi bo‘sh kolleksiyalar

Boshqa ko‘pchilik qiymatlar `True` hisoblanadi.

```python
bool("")        # False
bool("False")   # True
bool("0")       # True
bool(0)         # False
bool(1)         # True
```

Bo‘sh bo‘lmagan matn `True` bo‘ladi. Demak, `bool("False")` natijasi `False` emas, `True`.

## Konvertatsiya va xatoliklar

Konvertatsiya jarayonida qiymat yoki obyekt mos kelmasa, Python xatolik chiqaradi.

| Xatolik | Sababi | Misol |
|---|---|---|
| `ValueError` | Qiymat so‘ralgan turga o‘tkazilmaydi | `int("hello")` |
| `TypeError` | Obyekt turi bajarilayotgan amal uchun mos emas | `int(None)` |

Boshqa keng tarqalgan misollar:

```python
int("18.5")          # ValueError
"Age: " + 20         # TypeError
2026 - "20"          # TypeError
```

`ValueError` va `TypeError` bir xil xatolik emas. Birinchisi qiymatning mos emasligi, ikkinchisi esa obyekt turi bilan bog‘liq.

## Foydalanuvchi ma’lumotini konvertatsiya qilish

Quyidagi yozuv:

```python
age = int(input("Yoshingizni kiriting: "))
```

ikki amalni ketma-ket bajaradi:

1. `input()` foydalanuvchidan matn oladi.
2. `int()` olingan matnni butun songa aylantiradi.

Bu ikki bosqichni alohida yozish ham mumkin:

```python
age_text = input("Yoshingizni kiriting: ")
age = int(age_text)
```

Har ikkala holatda ham foydalanuvchi butun son ko‘rinishidagi qiymat kiritishi kerak. Aks holda `ValueError` yuz berishi mumkin.

## `print()` va f-string

`print()` ichida verguldan foydalanib, bir nechta qiymatni chiqarish mumkin:

```python
name = "Ali"
age = 20

print("Ism:", name, "Yosh:", age)
```

`print()` argumentlar orasiga standart holatda bitta probel qo‘yadi. Buni `sep` parametri orqali o‘zgartirish mumkin:

```python
print("Ali", 20, sep=" | ")
```

`+` orqali matnlarni birlashtirishda esa ikkala operand ham mos turda bo‘lishi kerak:

```python
print("Yosh: " + str(age))
```

F-string bunday vaziyatlarda qulayroq:

```python
print(f"Yosh: {age}")
```

F-string Python 3.6 versiyasida taqdim etilgan.

Jingalak qavslar `{}` ichida o‘zgaruvchi yoki ifoda yozish mumkin:

```python
a = 10
b = 5

print(f"{a} + {b} = {a + b}")
```

Sonlarni formatlashda:

```python
price = 19.9876

print(f"{price:.2f}")  # 19.99
```

`:.2f` sonni ekranga ikki kasr xonasi bilan chiqaradi. Bu qiymatning o‘zini o‘zgartirmaydi, faqat uning ko‘rinishini formatlaydi.

## Yoshdan tug‘ilgan yilni aniqlash

Quyidagi formula taxminiy natija beradi:

```python
age = 20
birth_year = 2026 - age
```

Ammo 2026-yil 29-oktabr kuni 20 yoshda bo‘lgan inson 2005 yoki 2006-yilda tug‘ilgan bo‘lishi mumkin. Bu uning tug‘ilgan kuni joriy yilda o‘tgan-o‘tmaganiga bog‘liq.

Aniq hisoblash uchun yoshdan tashqari tug‘ilgan kun va oy ham kerak.

## Asosiy atamalar

| Atama | Ma’nosi |
|---|---|
| `input()` | Foydalanuvchidan ma’lumot olish funksiyasi |
| `type()` | Obyekt turini aniqlash funksiyasi |
| Type conversion | Ma’lumot turini o‘zgartirish |
| `int` | Butun son turi |
| `float` | Haqiqiy son turi |
| `str` | Matn turi |
| `bool` | Mantiqiy tur |
| `ValueError` | Qiymatni kerakli turga o‘tkazib bo‘lmaganda yuz beradigan xatolik |
| `TypeError` | Amal uchun mos bo‘lmagan turdagi obyekt berilganda yuz beradigan xatolik |
| f-string | O‘zgaruvchi va ifodalarni matn ichida formatlash usuli |
| Format specifier | Qiymat qanday ko‘rinishda chiqarilishini belgilovchi format qismi |





# Day 05 — Reference Notes

**Topic:** `input()`, type conversion, and f-strings  
**Date:** 29 October 2026

This document is a quick reference for the main concepts, syntax, and common errors covered in Lesson 05.

## How does `input()` work?

`input()` receives one line of data from the user. The program waits until the user presses Enter.

```python
name = input("Enter your name: ")
```

The value returned by `input()` is assigned to the `name` variable.

**Important:** `input()` always returns a `str`. Entering a number does not change this rule.

```python
age = input("Enter your age: ")

print(type(age))  # <class 'str'>
```

`input()` removes the trailing newline character from the entered line, but it does not automatically remove spaces at the beginning or end of the entered text.

## Type conversion

Type conversion means converting a value from one data type to another. In Python, we can do this with built-in functions.

| Function | Purpose | Example | Result |
|---|---|---|---|
| `int()` | Convert to an integer | `int("25")` | `25` |
| `float()` | Convert to a floating-point number | `float("19.5")` | `19.5` |
| `str()` | Convert to a string | `str(100)` | `"100"` |
| `bool()` | Convert to a Boolean value | `bool(0)` | `False` |

### `int()`

```python
int("25")    # 25
int(18.9)    # 18
int(-3.9)    # -3
```

`int()` does not round a floating-point number. It truncates the fractional part towards zero.

The following expressions are not equivalent:

```python
int(18.5)      # 18
int("18.5")    # ValueError
```

In the first case, the argument is a `float`. In the second case, it is a `str`.

### `float()`

```python
float("19.99")   # 19.99
float("25")      # 25.0
float(10)        # 10.0
```

When entering a decimal number as text, use a dot: `"19.99"`. The string `"19,99"` is not a valid format for ordinary `float()` conversion.

### `str()`

```python
str(100)       # "100"
str(19.5)      # "19.5"
str(True)      # "True"
```

This function returns the string representation of a value. For example, converting a number to a string may be necessary before concatenating it with other text.

### `bool()`

In Python, the following values are considered `False`:

- `False`
- `None`
- Zero values such as `0` and `0.0`
- Empty strings such as `""`
- Empty collections such as `[]`, `()`, and `{}`

Most other values are considered `True`.

```python
bool("")        # False
bool("False")   # True
bool("0")       # True
bool(0)         # False
bool(1)         # True
```

A non-empty string evaluates to `True`. Therefore, `bool("False")` returns `True`, not `False`.

## Conversion errors

Python raises an error when a value or object is not suitable for the requested conversion.

| Error | Cause | Example |
|---|---|---|
| `ValueError` | The value cannot be converted to the requested type | `int("hello")` |
| `TypeError` | The object's type is not suitable for the operation | `int(None)` |

Other common examples:

```python
int("18.5")          # ValueError
"Age: " + 20         # TypeError
2026 - "20"          # TypeError
```

`ValueError` and `TypeError` are not the same. The first concerns an unsuitable value; the second concerns an unsuitable object type for the operation.

## Converting user input

The following statement:

```python
age = int(input("Enter your age: "))
```

performs two operations in sequence:

1. `input()` receives text from the user.
2. `int()` converts the received text into an integer.

We can also write these steps separately:

```python
age_text = input("Enter your age: ")
age = int(age_text)
```

Both approaches require the user to enter a value that represents an integer. Otherwise, a `ValueError` may occur.

## `print()` and f-strings

We can use commas inside `print()` to display multiple values:

```python
name = "Ali"
age = 20

print("Name:", name, "Age:", age)
```

By default, `print()` inserts one space between its arguments. This can be changed using the `sep` parameter:

```python
print("Ali", 20, sep=" | ")
```

When concatenating strings with `+`, the operands must have compatible types:

```python
print("Age: " + str(age))
```

An f-string is more convenient in this situation:

```python
print(f"Age: {age}")
```

F-strings were introduced in Python 3.6.

Variables and expressions can be placed inside curly braces `{}`:

```python
a = 10
b = 5

print(f"{a} + {b} = {a + b}")
```

To format numbers:

```python
price = 19.9876

print(f"{price:.2f}")  # 19.99
```

`:.2f` displays the number with two digits after the decimal point. It changes the displayed representation, not the original value.

## Estimating a birth year from age

The following formula provides an estimate:

```python
age = 20
birth_year = 2026 - age
```

However, a person who is 20 years old on 29 October 2026 could have been born in either 2005 or 2006. It depends on whether their birthday has already occurred during the current year.

To calculate the exact birth date, we need the day and month of birth in addition to the age.

## Key terminology

| Term | Meaning |
|---|---|
| `input()` | A function that receives data from the user |
| `type()` | A function that identifies an object's type |
| Type conversion | Changing a value from one data type to another |
| `int` | Integer data type |
| `float` | Floating-point data type |
| `str` | String data type |
| `bool` | Boolean data type |
| `ValueError` | An error raised when a value cannot be converted as requested |
| `TypeError` | An error raised when an object has an unsuitable type for an operation |
| f-string | A way to format variables and expressions inside a string |
| Format specifier | A part of a format expression that controls how a value is displayed |






# Урок 05 — Справочный материал

**Тема:** `input()`, преобразование типов и f-строки  
**Дата:** 29.10.2026

Этот документ предназначен для быстрого повторения основных понятий, синтаксиса и распространённых ошибок, рассмотренных на пятом уроке.

## Как работает `input()`?

Функция `input()` получает от пользователя одну строку данных. Программа ожидает, пока пользователь нажмёт Enter.

```python
name = input("Введите ваше имя: ")
```

Значение, возвращаемое функцией `input()`, присваивается переменной `name`.

**Важно:** `input()` всегда возвращает значение типа `str`. Ввод числа не меняет этого правила.

```python
age = input("Введите ваш возраст: ")

print(type(age))  # <class 'str'>
```

Функция `input()` удаляет завершающий символ новой строки после ввода, но автоматически не удаляет пробелы в начале и конце введённого текста.

## Преобразование типов данных

Преобразование типов — это перевод значения из одного типа данных в другой. В Python для этого используются встроенные функции.

| Функция | Назначение | Пример | Результат |
|---|---|---|---|
| `int()` | Преобразование в целое число | `int("25")` | `25` |
| `float()` | Преобразование в число с плавающей точкой | `float("19.5")` | `19.5` |
| `str()` | Преобразование в строку | `str(100)` | `"100"` |
| `bool()` | Преобразование в логическое значение | `bool(0)` | `False` |

### `int()`

```python
int("25")    # 25
int(18.9)    # 18
int(-3.9)    # -3
```

Функция `int()` не округляет число с плавающей точкой. Она отбрасывает дробную часть в направлении нуля.

Следующие выражения не являются эквивалентными:

```python
int(18.5)      # 18
int("18.5")    # ValueError
```

В первом случае аргумент имеет тип `float`, а во втором — `str`.

### `float()`

```python
float("19.99")   # 19.99
float("25")      # 25.0
float(10)        # 10.0
```

При вводе десятичного числа в виде строки используется точка: `"19.99"`. Строка `"19,99"` не является корректным форматом для обычного преобразования через `float()`.

### `str()`

```python
str(100)       # "100"
str(19.5)      # "19.5"
str(True)      # "True"
```

Эта функция возвращает строковое представление значения. Например, преобразование числа в строку может понадобиться перед объединением его с другим текстом.

### `bool()`

В Python следующие значения считаются ложными (`False`):

- `False`
- `None`
- Нулевые значения, например `0` и `0.0`
- Пустые строки, например `""`
- Пустые коллекции, например `[]`, `()` и `{}`

Большинство остальных значений считаются истинными (`True`).

```python
bool("")        # False
bool("False")   # True
bool("0")       # True
bool(0)         # False
bool(1)         # True
```

Любая непустая строка преобразуется в `True`. Поэтому `bool("False")` возвращает `True`, а не `False`.

## Ошибки при преобразовании типов

Если значение или объект не подходит для запрошенного преобразования, Python вызывает ошибку.

| Ошибка | Причина | Пример |
|---|---|---|
| `ValueError` | Значение невозможно преобразовать в запрошенный тип | `int("hello")` |
| `TypeError` | Тип объекта не подходит для выполняемой операции | `int(None)` |

Другие распространённые примеры:

```python
int("18.5")          # ValueError
"Age: " + 20         # TypeError
2026 - "20"          # TypeError
```

`ValueError` и `TypeError` — разные ошибки. Первая связана с неподходящим значением, вторая — с неподходящим типом объекта для выполняемой операции.

## Преобразование пользовательского ввода

Следующая запись:

```python
age = int(input("Введите ваш возраст: "))
```

выполняет две операции последовательно:

1. `input()` получает текст от пользователя.
2. `int()` преобразует полученный текст в целое число.

Эти действия также можно записать отдельно:

```python
age_text = input("Введите ваш возраст: ")
age = int(age_text)
```

В обоих случаях пользователь должен ввести значение, которое можно интерпретировать как целое число. В противном случае может возникнуть `ValueError`.

## `print()` и f-строки

С помощью запятых внутри `print()` можно выводить несколько значений:

```python
name = "Ali"
age = 20

print("Имя:", name, "Возраст:", age)
```

По умолчанию `print()` добавляет один пробел между аргументами. Это поведение можно изменить с помощью параметра `sep`:

```python
print("Ali", 20, sep=" | ")
```

При объединении строк с помощью `+` операнды должны иметь совместимые типы:

```python
print("Возраст: " + str(age))
```

В такой ситуации f-строка обычно удобнее:

```python
print(f"Возраст: {age}")
```

F-строки были представлены в Python 3.6.

Внутри фигурных скобок `{}` можно указывать переменные и выражения:

```python
a = 10
b = 5

print(f"{a} + {b} = {a + b}")
```

Для форматирования чисел:

```python
price = 19.9876

print(f"{price:.2f}")  # 19.99
```

Формат `:.2f` выводит число с двумя знаками после десятичной точки. Он изменяет представление значения на экране, но не само исходное значение.

## Определение года рождения по возрасту

Следующая формула позволяет получить приблизительный результат:

```python
age = 20
birth_year = 2026 - age
```

Однако человек, которому исполнилось 20 лет на 29 октября 2026 года, мог родиться как в 2005, так и в 2006 году. Это зависит от того, наступил ли его день рождения в текущем году.

Для точного определения даты рождения, помимо возраста, необходимо знать день и месяц рождения.

## Основные термины

| Термин | Значение |
|---|---|
| `input()` | Функция получения данных от пользователя |
| `type()` | Функция определения типа объекта |
| Type conversion | Преобразование значения из одного типа данных в другой |
| `int` | Тип целого числа |
| `float` | Тип числа с плавающей точкой |
| `str` | Строковый тип данных |
| `bool` | Логический тип данных |
| `ValueError` | Ошибка, возникающая, когда значение невозможно преобразовать указанным способом |
| `TypeError` | Ошибка, возникающая, когда тип объекта не подходит для выполняемой операции |
| f-string | Способ форматирования переменных и выражений внутри строки |
| Format specifier | Часть выражения форматирования, определяющая способ отображения значения |

