
# Day 02 — Sanoq sistemalari va kompyuterda sonlarni ifodalash

Bugungi topshiriqlarning maqsadi formulalarni shunchaki yodlash emas. Har bir o'tishni qog'ozda qadamma-qadam ko'rsating va javobingizni boshqa usul bilan tekshirishga harakat qiling. O'nlikka o'tkazishda razryadlar qiymatini yozing; o'nlikdan boshqa asosga o'tkazishda bo'lish va qoldiqlarning har birini ko'rsating.

### 1-topshiriq — Sanoq sistemasi asosini aniqlang

Quyidagi yozuvlarning qaysilari ko'rsatilgan asosda to'g'ri yozilganini belgilang. Noto'g'ri bo'lsa, sababini tushuntiring.

1. $101101_2$
2. $10201_2$
3. $728_8$
4. $7A_{16}$
5. $2G_{16}$
6. $1203_4$
7. $999_{10}$

### 2-topshiriq — Boshqa asosdan o'nlikka

Har bir sonni o'nlikka o'tkazing. Pozitsion formulani yozing va oraliq hisob-kitoblarni ko'rsating.

1. $101011_2$
2. $1110101_2$
3. $347_8$
4. $625_8$
5. $3A_{16}$
6. $2F4_{16}$
7. $132_4$
8. $243_5$

### 3-topshiriq — O'nlikdan boshqa asosga

Quyidagi sonlarni ko'rsatilgan asosga o'tkazing. Qoldiqlar jadvalini yozing va qoldiqlar nega teskari tartibda olinishi haqida bir-ikki gap bilan izoh bering.

1. $37_{10} \rightarrow ?_2$
2. $156_{10} \rightarrow ?_7$
3. $255_{10} \rightarrow ?_{16}$
4. $100_{10} \rightarrow ?_8$
5. $73_{10} \rightarrow ?_3$
6. $202_{10} \rightarrow ?_5$

### 4-topshiriq — Bir asosdan boshqa asosga

Har bir misolda avval manba asosini o'nlikka o'tkazing, keyin o'nlikdan maqsad asosiga o'ting. Yakunda teskari tekshiruv qiling.

1. $243_5 \rightarrow ?_3$
2. $352_7 \rightarrow ?_4$
3. $7B_{16} \rightarrow ?_8$
4. $1101101_2 \rightarrow ?_5$

### 5-topshiriq — Triada va tetrada

Quyidagi o'tishlarni bo'lish usulisiz, guruhlash orqali bajaring.

1. $110101101_2 \rightarrow ?_8$
2. $1011110011_2 \rightarrow ?_{16}$
3. $724_8 \rightarrow ?_2$
4. $B3A_{16} \rightarrow ?_2$
5. $111010111101_2 \rightarrow ?_8$ va $?_{16}$

Har bir savolda guruhlarni alohida ko'rsating. Kerak bo'lsa butun sonning eng chap tomoniga nol qo'shing va nega bu qiymatni o'zgartirmasligini tushuntiring.

### 6-topshiriq — Kasr sonlar

1. $101.101_2$ ni o'nlikka o'tkazing.
2. $110.011_2$ ni o'nlikka o'tkazing.
3. $0.625_{10}$ ni ikkilikka o'tkazing va har bir ko'paytirish bosqichini ko'rsating.
4. $13.625_{10}$ ni ikkilikka o'tkazing.
5. $0.1_{10}$ ni ikkilikka o'tkazishning dastlabki kamida 8 bitini toping. Qaysi kasr qismi qayta paydo bo'layotganini aniqlang.
6. Nima sababdan $1/10$ ning ikkilik yozuvi tugamasligini kasrning qisqartirilgan maxraji orqali tushuntiring.

### 7-topshiriq — Fizika va raqamli mantiq

Quyidagi savollarga o'z so'zlaringiz bilan javob yozing.

1. Kuchlanish ko'p qiymatli bo'lishi mumkin bo'lsa, nima uchun raqamli sxema uni ikki mantiqiy holat sifatida talqin qiladi?
2. Nega $0$ har doim aynan $0$ V, $1$ esa aynan $5$ V degani emas?
3. Noise margin qanday muammoni kamaytirishga yordam beradi?
4. SRAM katakchasi va DRAM katakchasining asosiy fizik farqi nima?
5. DRAM refresh nima uchun kerak?
6. $0$ va $1$ ma'lumotning o'zi emas, balki kodlash qiymatlari, deganda nimani tushunasiz?

### 8-topshiriq — Python bilan tekshirish

Python'da `examples/day02/number_systems.py` va `examples/day02/base_conversion.py` fayllarini ishga tushiring. Keyin mustaqil ravishda quyidagilarni sinab ko'ring:

```python
print(bin(45))
print(oct(45))
print(hex(45))
print(int("101101", 2))
print(int("55", 8))
print(int("2D", 16))
```

Savollar:
1. `bin()`, `oct()` va `hex()` qanday maqsadga xizmat qiladi?
2. `int("101101", 2)` dagi ikkinchi argument nimani bildiradi?
3. Python nima uchun `int("102", 2)` uchun xato beradi?
4. O'zingiz tanlagan 3 ta sonni ikki xil asosda ifodalang va qiymat bir xil ekanini tekshiring.

### 9-topshiriq — Floating-point tajribasi

Quyidagi kodni mustaqil ishga tushiring:

```python
from decimal import Decimal
from math import isclose

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(format(0.1, ".20f"))
print((0.1).as_integer_ratio())
print(isclose(0.1 + 0.2, 0.3))
print(Decimal("0.1") + Decimal("0.2"))
```

Natijalarni izohlang:
1. Qaysi natija siz kutgandan farq qildi?
2. `as_integer_ratio()` nimani ko'rsatadi?
3. `math.isclose()` tekshiruvi nega `==` dan farq qiladi?
4. `Decimal("0.1")` va `Decimal(0.1)` o'rtasida qanday farq bor?
5. Nima uchun `float` ni "noto'g'ri" deb emas, cheklangan aniqlikka ega format deb ta'riflash to'g'riroq?

### Challenge — O'zingizning konvertoringiz

`examples/day02/base_conversion.py` dagi kodni o'qing. Keyin yangi dastur yozing yoki mavjud funksiyalarni kengaytiring:
- foydalanuvchi sonni matn shaklida kiritadi;
- manba asosini va maqsad asosini kiritadi;
- dastur natijani hisoblaydi;
- noto'g'ri asos yoki noto'g'ri raqam kiritilganda tushunarli xabar beradi;
- manfiy butun sonlarni ham qo'llab-quvvatlaydi.

**Qo'shimcha talab:** $2$ dan $36$ gacha bo'lgan asoslarni qo'llashga harakat qiling. Bu diapazonda $A$ dan $Z$ gacha harflar $10$ dan $35$ gacha qiymatlarni ifodalashi mumkin.

### 📋 Topshirish mezonlari
- Har bir qo'lda yechilgan o'tishning oraliq qadamlari ko'rsatilgan.
- Natijalar kamida bitta mustaqil usul bilan tekshirilgan.
- Kasr konvertatsiyasida raqamlar qaysi tartibda o'qilishi izohlangan.
- SRAM/DRAM va raqamli mantiq savollariga sababni tushuntiruvchi javob berilgan.
- Python tajribasida natijalarni ko'chirib qo'yish bilan cheklanmay, ularning sababi izohlangan.

---

