
# Glossary — Python Course

Ushbu hujjatda kurs davomida ishlatiladigan muhim texnik atamalar va ularning sodda izohlari jamlanadi. Lug'at yangi mavzular o'tilgani sari kengaytiriladi.


## Day 02 — Number Systems and Computer Representation

* **Number system (Sanoq sistemasi):** Sonlarni yozish va ular bilan ishlash qoidalari. Asos raqamlar to'plamini va pozitsiyalar og'irligini belgilaydi.
* **Base / Radix (Asos):** Pozitsion sanoq sistemasining asosi. Asosi `b` bo'lgan sistemada `0` dan `b-1` gacha bo'lgan raqamlar qo'llanadi.
* **Positional notation (Pozitsion yozuv):** Raqamning qiymati uning belgisiga ham, sondagi pozitsiyasiga ham bog'liq bo'lgan yozuv usuli.
* **Binary (Ikkilik sanoq sistemasi):** Asosi 2 bo'lgan sistema; faqat `0` va `1` raqamlaridan foydalanadi.
* **Octal (Sakkizlik sanoq sistemasi):** Asosi 8 bo'lgan sistema; `0` dan `7` gacha raqamlardan foydalanadi.
* **Decimal (O'nlik sanoq sistemasi):** Asosi 10 bo'lgan, kundalik hayotda keng ishlatiladigan sistema.
* **Hexadecimal / Hex (O'n oltilik):** Asosi 16 bo'lgan sistema; `0`–`9` va `A`–`F` raqamlaridan foydalanadi.
* **Bit:** Binary digit. Ikki mantiqiy qiymatdan birini ifodalovchi eng kichik axborot birligi.
* **Byte (Bayt):** Odatda 8 bitdan tashkil topgan ma'lumot birligi.
* **Logic level (Mantiqiy sath):** Elektron sxema signalining belgilangan fizik oraliq orqali mantiqiy `0` yoki `1` sifatida talqin qilinishi.
* **Voltage threshold (Kuchlanish chegarasi):** Kirish signali mantiqiy past yoki yuqori sifatida talqin qilinishiga ta'sir qiladigan kuchlanish chegarasi.
* **Noise margin (Shovqin zaxirasi):** Signalga qo'shilgan shovqin bo'lsa ham, mantiqiy holatni ishonchli qabul qilishga imkon beruvchi zaxira.
* **Transistor:** Elektr signaliga qarab tokni boshqaradigan yarimo'tkazgichli komponent; raqamli sxemalarda elektron kalit vazifasi.
* **SRAM (Static RAM):** Bitni tranzistorlardan tashkil topgan holat orqali saqlaydi; davriy refresh talab qilmaydi (juda tez va qimmat).
* **DRAM (Dynamic RAM):** Katakchada kondensator zaryadi orqali bitni ifodalaydi; zaryad yo'qolishi sababli davriy refresh talab etiladi.
* **Volatile memory:** Elektr ta'minoti uzilganda ma'lumotini yo'qotadigan (o'chib ketadigan) xotira turi.
* **Refresh:** DRAM katakchalaridagi ma'lumotni saqlab turish uchun zaryad holatini davriy yangilash amali.
* **Triad (Triada):** Ikkilik sonning uch bitli guruhi. 1 triada = 1 ta sakkizlik raqam.
* **Tetrad / Nibble (Tetriada):** To'rt bitli guruh. 1 tetriada = 1 ta hexadecimal raqam.
* **Floating-point:** Cheklangan sonli bitlar bilan juda katta va juda kichik haqiqiy sonlarni taxminan ifodalash formati.
* **IEEE 754:** Floating-point arifmetika uchun keng ishlatiladigan xalqaro standart.
* **Rounding error (Yaxlitlash xatosi):** Aniq matematik qiymatni to'liq ifodalab bo'lmaganda, uning xotiraga sig'adigan eng yaqin qiymatini tanlashdan kelib chiqadigan qoldiq farq.
* **`Decimal`:** Python'dagi o'nlik arifmetika uchun maxsus tip. Moliya kabi sohalarda aniqroq amallar kerak bo'lganda foydalaniladi.

---


# Glossary — Python Course

This document compiles essential technical terms used throughout the course along with their simplified explanations. The glossary will be expanded as new topics are covered.

## Day 02 — Number Systems and Computer Representation

* **Number system:** Rules for writing and calculating numbers. The base determines the available digit set and positional weights.
* **Base / Radix:** The foundation of a positional number system. A system with base `b` uses digits `0` to `b-1`.
* **Positional notation:** A numeral system in which the value of a digit depends on its position within the number.
* **Binary:** Base-2 system; uses only `0` and `1`.
* **Octal:** Base-8 system; uses digits `0` through `7`.
* **Decimal:** Base-10 system; standard system used in everyday life.
* **Hexadecimal / Hex:** Base-16 system; uses digits `0`–`9` and letters `A`–`F`.
* **Bit:** Binary digit. The smallest unit of data in a computer, representing a single logical state (`0` or `1`).
* **Byte:** A unit of digital data that typically consists of 8 bits.
* **Logic level:** The interpretation of a voltage range in a circuit as a logical `0` (low) or `1` (high).
* **Voltage threshold:** The specific voltage limit that determines how an input signal is interpreted.
* **Noise margin:** The amount of noise a signal can tolerate before it is incorrectly interpreted as the wrong logic state.
* **Transistor:** A semiconductor device used to switch electrical signals and power; the fundamental building block of modern electronics.
* **SRAM (Static RAM):** Retains memory bits in a flip-flop state as long as power is supplied; very fast but expensive.
* **DRAM (Dynamic RAM):** Stores bits as a charge in a capacitor; requires constant refreshing to prevent data loss.
* **Volatile memory:** Computer memory that requires power to maintain the stored information.
* **Refresh:** The operation of periodically reading and restoring the charge in DRAM cells.
* **Triad:** A group of three bits. Equates to a single octal digit.
* **Tetrad / Nibble:** A group of four bits. Equates to a single hexadecimal digit.
* **Floating-point:** A method of representing real numbers that can support a wide range of values by trading off precision.
* **IEEE 754:** The most widely used standard for floating-point arithmetic computation.
* **Rounding error:** The discrepancy that occurs when a precise mathematical value cannot be exactly represented in memory and is approximated.
* **`Decimal`:** A specific data type in Python used for exact decimal arithmetic, primarily to avoid floating-point errors in finance.

---


# Глоссарий — Курс Python

В этом документе собраны важные технические термины, используемые в ходе курса, и их простые объяснения. Словарь будет пополняться по мере прохождения новых тем.

## День 02 — Системы счисления и представление данных

* **Number system (Система счисления):** Правила записи чисел и работы с ними. Основание определяет набор цифр и вес каждой позиции.
* **Base / Radix (Основание):** Основание позиционной системы счисления. В системе с основанием `b` используются цифры от `0` до `b-1`.
* **Positional notation (Позиционная запись):** Способ записи, при котором значение цифры зависит как от её символа, так и от её позиции в числе.
* **Binary (Двоичная система):** Система с основанием 2; использует только `0` и `1`.
* **Octal (Восьмеричная система):** Система с основанием 8; использует цифры от `0` до `7`.
* **Decimal (Десятичная система):** Система с основанием 10; стандартная система для повседневной жизни.
* **Hexadecimal / Hex (Шестнадцатеричная система):** Система с основанием 16; использует цифры `0`–`9` и буквы `A`–`F`.
* **Bit (Бит):** Binary digit. Наименьшая единица информации, представляющая одно из двух логических значений.
* **Byte (Байт):** Единица измерения данных, обычно состоящая из 8 битов.
* **Logic level (Логический уровень):** Интерпретация уровня напряжения в электронной схеме как логического `0` (низкий) или `1` (высокий).
* **Voltage threshold (Пороговое напряжение):** Граница напряжения, влияющая на то, как будет интерпретирован входной сигнал (как высокий или низкий).
* **Noise margin (Запас помехоустойчивости):** Допустимый уровень шума в сигнале, при котором логическое состояние всё ещё надежно считывается.
* **Transistor (Транзистор):** Полупроводниковый компонент, управляющий током; в цифровых схемах выступает в роли электронного ключа.
* **SRAM (Static RAM):** Хранит биты с помощью состояния триггеров (транзисторов); не требует периодической регенерации (очень быстрая, но дорогая).
* **DRAM (Dynamic RAM):** Хранит бит в виде заряда на конденсаторе в ячейке; требует периодической регенерации из-за утечки заряда.
* **Volatile memory (Энергозависимая память):** Тип памяти, данные в которой теряются при отключении электропитания.
* **Refresh (Регенерация):** Процесс периодического обновления заряда в ячейках DRAM для сохранения информации.
* **Triad (Триада):** Группа из трех битов. Одна триада соответствует одной восьмеричной цифре.
* **Tetrad / Nibble (Тетрада / Ниббл):** Группа из четырех битов. Одна тетрада соответствует одной шестнадцатеричной цифре.
* **Floating-point (Плавающая точка):** Формат представления чисел, используемый для приближенного выражения очень больших или малых вещественных чисел ограниченным количеством битов.
* **IEEE 754:** Широко используемый международный стандарт для арифметики с плавающей точкой.
* **Rounding error (Ошибка округления):** Разница, возникающая, когда точное математическое значение не помещается в формат, и выбирается ближайшее представимое значение.
* **`Decimal`:** Специальный тип в Python для точной десятичной арифметики, часто применяемый в финансах для избежания проблем с плавающей точкой.