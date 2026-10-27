# Day 03 — Python, IDLE, print() va kommentariyalar

Bu topshiriqlarning maqsadi kodni nusxalash emas, balki o'rnatilgan muhit bilan ishonchli ishlash va birinchi buyruqlarning natijasini ongli ravishda taxmin qilishdir.

## 1. Python muhitini tekshirish

Kompyuteringizda quyidagilarni bajaring:

1. Start menyusidan IDLE'ni toping.
2. IDLE ichida Shell oynasi ochilishini aniqlang.
3. Windows Terminal yoki Command Prompt ochib, `python --version` yoki `py --version` buyruqlaridan birini sinang.
4. Qaysi Python versiyasi ko'rsatilganini yozib oling.
5. Bir jumlada Python, interpreter va IDLE orasidagi farqni tushuntiring.

Agar terminal buyruqlari ishlamasa, IDLE mavjud bo'lsa ham Python yo'q deb darhol xulosa qilmang. Xatolik matnini qayd eting va o'qituvchiga ko'rsating.

## 2. Birinchi Python fayli

IDLE'da `File → New File` orqali yangi Editor oynasini oching. Quyidagini yozing va `hello_world.py` nomi bilan saqlang:

```python
print("Hello World!")
```

`F5` yoki `Run → Run Module` orqali bajaring.

Tekshiring:
- Natija qaysi oynada paydo bo'ldi?
- Kod qaysi faylga saqlandi?
- Faylning kengaytmasi nima?
- Agar dasturni yana ishga tushirsangiz, kodni qayta yozish kerakmi?

## 3. print()ning turli ko'rinishlari

Quyidagi kodni alohida `print_basics.py` fayliga yozing va natijani ishga tushirishdan oldin taxmin qiling.

```python
print("Salom, dunyo!")
print("Python", "kursi")
print("Python" + " kursi")
print("Natija:", 10 + 5)
print("2026", "10", "24", sep="-")
print("Bir qator", end=" ")
print("davomi")
```

Har bir satr natijasini izohlang. Ayniqsa vergul bilan `+` orasidagi farqni tushuntiring.

## 4. O'zingizning salomlashuv dasturingiz

`my_introduction.py` nomli fayl yarating. Dastur kamida 5 qatordan iborat bo'lsin va quyidagilarni chiqarsin:

- salomlashuv;
- ismingiz yoki taxallusingiz;
- kurs nomi;
- o'rganmoqchi bo'lgan IT yo'nalishingiz;
- yakunlovchi jumla.

Talablar:
- kamida bir marta `print("A", "B")` ko'rinishidan foydalaning;
- kamida bir marta stringlarni `+` orqali birlashtiring;
- kamida bitta `sep` yoki `end` ishlating;
- faylni saqlang va qayta ishga tushirib ko'ring.

## 5. Kommentariyalar

`comments.py` faylida quyidagi uchala holatga misol yozing:

1. Alohida qatordagi `#` kommentariya.
2. Kod bilan bir qatordagi kommentariya.
3. Bir nechta izoh qatoridan iborat blok.

Keyin bitta yomon va bitta yaxshiroq kommentariya misolini yozing. Farqini tushuntiring: yaxshi kommentariya nima uchun kod shunday yozilganini tushuntiradi, yomon yoki ortiqcha kommentariya esa faqat kodning o'zini takrorlashi mumkin.

Uch qo'shtirnoqli matn haqida bitta jumla yozing: nega uni har doim kommentariya deb hisoblab bo'lmaydi?

## 6. IDLE menyulari bo'yicha amaliy tekshiruv

IDLE'da har bir amalni toping va sinab ko'ring:

- `File → New File` orqali Editor ochish.
- `File → Save As` orqali faylni yangi nom bilan saqlash.
- `Edit → Undo` va `Edit → Redo` bilan tahrirni qaytarish.
- `Run → Run Module` orqali faylni ishlatish.
- `Options → Configure IDLE` ichida shrift yoki rang sozlamasini topish. Hamma sozlamani o'zgartirish shart emas.
- `Window` menyusi orqali Shell va Editor orasida almashish.
- `Help` menyusidan IDLE Help yoki Python Docs'ni topish.

Shell oynasida Shell menyusi, Editor oynasida esa Run/Format menyusi ko'rinishi mumkin. Har ikki oynada bir xil menyular chiqishini kutmang.

## 7. Chiqarish natijasini oldindan aytish

Quyidagi kodni hozircha ishga tushirmasdan, har bir qator natijasini daftar yoki Markdown faylga yozing. So'ng ishga tushirib tekshiring.

```python
print("A", "B")
print("A" + "B")
print("A" + " " + "B")
print("X", "Y", sep="-")
print("Birinchi", end="...")
print("ikkinchi")
print()
print("Tugadi")
```

Nega birinchi qatorda bo'sh joy bor-u, ikkinchisida yo'q? `end` o'zgartirilmasa nima bo'ladi? `print()` argumentlarsiz chaqirilsa nima chiqaradi?

## 8. Challenge — kichik konsol tabrigi

`course_welcome.py` nomli kichik dastur yarating. U kursga yangi kelgan o'quvchini salomlab, kamida uchta ma'lumotni bir nechta `print()` usullari bilan chiqarishi kerak.

Qo'shimcha shartlar:
- Dastur boshiga nima qilishini tushuntiruvchi kommentariya yozing.
- Matnlarni `+` yordamida birlashtirish va vergul orqali bir nechta argument berishni taqqoslang.
- Natijani o'qishga qulay formatlang.
- Kodni `examples/day03/` ichida saqlang.

## Topshirish

Repositorydagi `examples/day03/` papkasida `hello_world.py`, `print_basics.py`, `comments.py` hamda o'zingiz yozgan dasturlardan kamida bittasi bo'lishi kerak. Topshiriqlarga yozma javoblar topshiruv usuliga qarab alohida fayl yoki daftar ko'rinishida berilishi mumkin.