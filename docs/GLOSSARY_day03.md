
# Glossary — Python Course

Ushbu lug'at kurs davomida kengayib boradi. Ta'riflar ataylab qisqa qilib berilgan; to'liqroq tushuntirishlar va misollar uchun dars fayllarini o'qing.


## Day 03 — Python and IDLE

### Python interpreter
Python manba kodini o'qiydigan va bajaradigan dastur.

### IDLE
Odatda Python o'rnatmalari bilan birga keladigan yengil dasturlash muhiti. U interaktiv Shell, Tahrirlovchi (Editor) va oddiy xatolarni to'g'rilash (debugging) vositalarini o'z ichiga oladi.

### Shell
Buyruq kiritilishi va uning natijasi darhol ko'rinishi mumkin bo'lgan interaktiv Python oynasi.

### Editor
Manba kodi fayllarini yozish va saqlash uchun ishlatiladigan matn tahrirlash oynasi.

### REPL
Read–Eval–Print Loop (O'qish-Baholash-Chop etish Sikli): tizim ifodani o'qiydigan, uni baholaydigan, natijani ko'rsatadigan va keyingi ifodani kutadigan interaktiv sikl.

### `.py` file
Odatda Python manba kodi uchun ishlatiladigan fayl kengaytmasi.

### `print()`
Obyektlarning matnli ifodasini matn oqimiga (odatda konsol yoki IDLE Shell'ga) yozadigan Python'ning ichki funksiyasi.

### Argument
Funksiya chaqiruviga taqdim etilgan qiymat. `print("A", "B")` da satrlar (stringlar) alohida argumentlardir.

### String concatenation
Satrlarni bitta satrga birlashtirish, ko'pincha `+` belgisi yordamida bajariladi.

### `sep`
Bir nechta argumentlar orasidagi ajratgichni tanlaydigan `print()` kalit so'z parametri. Uning standart qiymati bitta bo'sh joy (space).

### `end`
Chiqarishdan keyin nima yozilishini tanlaydigan `print()` kalit so'z parametri. Uning standart qiymati yangi qator (newline).

### Comment
Python'da kod ichida `#` bilan boshlanadigan eslatma. Tarjimon (interpreter) sharh matnini Python ko'rsatmasi sifatida hisobga olmaydi.

### Inline comment
Xuddi shu qatorda koddan keyin joylashtirilgan sharh.

### Docstring
Modul, funksiya yoki klassning birinchi bayonot pozitsiyasiga shu obyektni hujjatlashtirish uchun joylashtirilgan satr (string) literali. Docstring `#` bilan yoziladigan sharh bilan bir xil narsa emas.

### SyntaxError
Python manba kodi tilning sintaksis qoidalariga amal qilmaganda yuzaga keladigan xato.

### TypeError
Amal yaroqsiz turdagi qiymatga nisbatan qo'llanilganda (masalan, satr va butun sonni `+` bilan birlashtirishga urinish) yuzaga keladigan xato.

---

## Day 03 — Python and IDLE

### Python interpreter
The program that reads and executes Python source code.

### IDLE
A lightweight development environment commonly included with Python installations. It combines an interactive Shell, an Editor and basic debugging tools.

### Shell
An interactive Python window where a command can be entered and its result observed immediately.

### Editor
A text-editing window used to write and save source-code files.

### REPL
Read–Eval–Print Loop: an interactive cycle in which a system reads an expression, evaluates it, displays a result and waits for the next expression.

### `.py` file
A file extension commonly used for Python source code.

### `print()`
A built-in Python function that writes the text representation of objects to a text stream, usually the console or IDLE Shell.

### Argument
A value supplied to a function call. In `print("A", "B")`, the strings are separate arguments.

### String concatenation
Combining strings into one string, often using `+`.

### `sep`
The `print()` keyword parameter that chooses the separator between multiple arguments. Its default is one space.

### `end`
The `print()` keyword parameter that chooses what is written after the output. Its default is a newline.

### Comment
A note in source code beginning with `#` in Python. The interpreter ignores the comment text as a Python instruction.

### Inline comment
A comment placed after code on the same source line.

### Docstring
A string literal placed in a module, function or class's first statement position to document that object. A docstring is not the same as a `#` comment.

### SyntaxError
An error raised when Python source code does not follow the language's syntax rules.

### TypeError
An error raised when an operation is applied to a value of an unsuitable type, such as trying to concatenate a string and integer with `+`.

---


## Day 03 — Python and IDLE

### Python interpreter
Программа, которая читает и выполняет исходный код Python.

### IDLE
Легковесная среда разработки, обычно поставляемая вместе с Python. Объединяет в себе интерактивную оболочку (Shell), редактор (Editor) и базовые инструменты отладки.

### Shell
Интерактивное окно Python, в котором можно ввести команду и сразу увидеть ее результат.

### Editor
Окно редактирования текста, используемое для написания и сохранения файлов исходного кода.

### REPL
Read–Eval–Print Loop (Цикл Чтение-Вычисление-Вывод): интерактивный цикл, в котором система считывает выражение, вычисляет его, отображает результат и ждет следующего выражения.

### `.py` file
Расширение файла, обычно используемое для исходного кода Python.

### `print()`
Встроенная функция Python, которая записывает текстовое представление объектов в текстовый поток, обычно в консоль или IDLE Shell.

### Argument
Значение, переданное при вызове функции. В `print("A", "B")` строки являются отдельными аргументами.

### String concatenation
Объединение строк в одну строку, часто с использованием знака `+`.

### `sep`
Именованный параметр функции `print()`, который выбирает разделитель между несколькими аргументами. По умолчанию это один пробел.

### `end`
Именованный параметр функции `print()`, который выбирает, что записывается после вывода. По умолчанию это переход на новую строку (newline).

### Comment
Примечание в исходном коде, начинающееся с `#` в Python. Интерпретатор игнорирует текст комментария как инструкцию Python.

### Inline comment
Комментарий, размещенный после кода на той же строке.

### Docstring
Строковый литерал, помещенный в первую позицию модуля, функции или класса для документирования этого объекта. Docstring — это не то же самое, что комментарий `#`.

### SyntaxError
Ошибка, возникающая, когда исходный код Python не соответствует синтаксическим правилам языка.

### TypeError
Ошибка, возникающая, когда операция применяется к значению неподходящего типа, например, при попытке объединить строку и целое число с помощью `+`.