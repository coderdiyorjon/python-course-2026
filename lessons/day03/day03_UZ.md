# Day 03 — Python o‘rnatish, IDLE bilan tanishish va birinchi dastur

**Sana:** 24.10.2026  
**Modul:** Python bilan tanishish  
**Daraja:** Beginner  
**Darsning markaziy g‘oyasi:** dasturlashni boshlash uchun muhitni tayyorlash, kod yoziladigan joyni natija ko‘rinadigan joydan farqlash va kompyuterga birinchi aniq ko‘rsatmalarni berish.

## Darsni nimadan boshlaymiz?

Oldingi darsda algoritm, ma’lumot va kompyuterda axborot qanday ifodalanishi haqida gaplashdik. Endi o‘sha nazariy tushunchalarni amaliyotga olib kiramiz. Dastur yozish uchun kompyuterda Python interpretatori, kod yozish uchun tahrirlovchi muhit va natijani ko‘rish imkoniyati kerak. Birinchi mashg‘ulotda bu qismlarni o‘rnatamiz, ularning vazifalarini ajratamiz va eng sodda ishlaydigan dasturni yaratamiz.

Dars yakunida o‘quvchi Python rasmiy saytidan o‘rnatish faylini topa olishi, o‘rnatilganini tekshirishi, IDLE Shell va Editor orasidagi farqni tushuntirishi, yangi `.py` fayl ochib saqlashi va uni ishga tushirishi kerak. Shuningdek, `print()` yordamida matn chiqarishni, vergul va `+` ishlatilishidagi farqni hamda kommentariyalar nima uchun kerakligini tushunishi lozim.

## 1. Python'ni qayerdan yuklab olamiz va nima uchun rasmiy manba kerak?

Dastur o‘rnatishda birinchi savol — uni qayerdan olish kerak? Python uchun rasmiy manzil [python.org](https://www.python.org/) hisoblanadi. Yuklab olish sahifasida operatsion tizimga mos o‘rnatish fayli yoki Python install manager taklif qilinadi. Boshqa saytlardan tasodifiy installer yuklab olish shart emas: rasmiy manba versiyani tekshirish, xavfsizlik va to‘g‘ri distributivni tanlashni osonlashtiradi.

Dars o‘tilgan 2026-yil 24-oktabr kuni Windows sahifasida Python 3.13.17 uchun an’anaviy installer mavjud edi. Python versiyalari vaqt o‘tishi bilan yangilanadi. 2026-yil 27-oktabr holatida rasmiy sahifada 3.15.2 eng yangi feature-release sifatida, 3.14.10 esa 3.14 qatorining yangilangan versiyasi sifatida ko‘rsatilgan; 3.13.18 xavfsizlik relizi bo‘lib, unga Windows installer berilmagan. Shuning uchun kurs guruhidagi kompyuterlarda qaysi versiya o‘rnatilganini tekshirish va hammani bir xil, kurs bilan mos versiyada ushlab turish muhim. Versiya raqamlari o‘zgarib boradi, shu sabab dars materialida raqamdan ko‘ra versiyani tekshirish usulini eslab qolish muhimroq.

Python'ning rasmiy Windows sahifasi: <https://www.python.org/downloads/windows/>  
Python'ning umumiy yuklab olish sahifasi: <https://www.python.org/downloads/>

### Windows'da o‘rnatish jarayoni

1. Brauzerda `python.org` saytini oching.
2. **Downloads** bo‘limidan **Windows** sahifasiga kiring.
3. Kurs uchun tanlangan Python versiyasini va kompyuterga mos variantni tanlang. Odatdagi zamonaviy Windows kompyuterlarining aksariyati 64-bit x86-64 bo‘ladi, ammo ARM qurilmalari uchun alohida paket kerak bo‘lishi mumkin.
4. Rasmiy sahifadagi o‘rnatish ko‘rsatmalariga amal qiling. Installer oynasidagi tanlovlar distributiv va versiyaga qarab farq qilishi mumkin.
5. Agar klassik installerda **Add python.exe to PATH** tanlovi ko‘rsatilsa va kurs komandalar satridan `python` buyrug‘i bilan ishga tushirishni nazarda tutsa, bu tanlovni belgilash qulay. Yangi Python install manager yoki boshqa o‘rnatish usulida jarayon farq qilishi mumkin.
6. O‘rnatish tugagach, Start menyusidan **IDLE (Python 3.x ...)** ni oching. Python asosiy komponentlari o‘rnatilgan bo‘lsa, IDLE odatda shu bilan birga keladi.
7. O‘rnatish muvaffaqiyatini tekshirish uchun Windows Terminal yoki Command Prompt'da `py --version` yoki `python --version` buyruqlaridan birini sinab ko‘ring. Kompyuterdagi o‘rnatish turiga qarab ulardan biri ishlamasligi mumkin; bu darhol Python yo‘q degani emas. Start menyusidagi IDLE orqali ham tekshirish mumkin.

Versiyani bilish nima uchun kerak? Chunki bir nechta Python versiyasi o‘rnatilgan bo‘lishi mumkin. Masalan, `python` bir versiyani, `py -3.13` esa aynan 3.13 qatorini ishga tushirishi mumkin. Keyinchalik paketlar, kutubxonalar va ayrim sintaksis xususiyatlari versiyaga bog‘liq bo‘lishi mumkin.

### O‘rnatish va konfiguratsiya bir xil narsa emas

**O‘rnatish** — kerakli dastur fayllarini kompyuterga joylashtirish. **Konfiguratsiya** — dastur qanday ishga tushishi, qaysi interpreter ishlatilishi va muhitingiz qanday sozlanishini belgilash. Boshlang‘ich darsda murakkab konfiguratsiya talab qilinmaydi; avvalo o‘rnatilgan Python'ni to‘g‘ri ishga tushirish, IDLE'ni ochish va faylni saqlashni o‘rganish kifoya.

O‘quvchilar kompyuterida bir nechta Python o‘rnatilgan bo‘lsa, `python --version`, `py --version` yoki `py -3.13 --version` natijalari farq qilishi mumkin. Muhim ko‘nikma — ko‘r-ko‘rona qayta-qayta o‘rnatish emas, qaysi interpreter ishlayotganini aniqlashdir.

## 2. Python, IDLE va kod yoziladigan oyna — bir xil narsa emas

Yangi boshlovchilar tez-tez uchta tushunchani bitta deb qabul qilishadi: Python tili, Python interpretatori va IDLE. Ular o‘zaro bog‘liq, ammo vazifalari boshqa-boshqa.

**Python** — dasturlash tili; unda dastur matni yoziladi.  
**Python interpreter** — Python kodini o‘qib bajaradigan dasturiy muhit.  
**IDLE** — Python bilan birga keladigan sodda integratsiyalashgan rivojlantirish muhiti. U kod yozish uchun Editor, buyruqlarni bevosita bajarish uchun Shell va ayrim tekshirish hamda debugging vositalarini birlashtiradi.

IDLE — Python yozishning yagona usuli emas. Keyinchalik o‘quvchilar VS Code, PyCharm yoki boshqa editorlardan foydalanishlari mumkin. Lekin IDLE yangi boshlovchilar uchun qulay: u odatda alohida murakkab sozlashni talab qilmaydi va Python bilan birga o‘rnatiladi.

IDLE ochilganda ko‘pincha qora yoki oq fonli **Python Shell** oynasi ko‘rinadi. Unda `>>>` belgisi bo‘ladi. Bu belgilar Python interaktiv buyruq kutayotganini bildiradi. Ularni o‘quvchi o‘zi yozmaydi. Kursor `>>>` dan keyin turganida bitta qisqa ifodani kiritish mumkin, masalan `2 + 3`, va Enter bosilganda natija darhol chiqadi.

Lekin bir nechta qatorlardan iborat saqlanadigan dastur yozmoqchi bo‘lsak, Shell ichiga kodni shunchaki kiritib ketish o‘rniga, **File → New File** orqali alohida **Editor** oynasini ochamiz. Bu ikki oynaning vazifasini boshidan ajratish foydali odatdir:

- **Shell:** qisqa buyruqlarni sinash, natijani tez ko‘rish, kichik tajribalar o‘tkazish.
- **Editor:** dastur matnini yozish, saqlash, o‘zgartirish va keyin qayta ishga tushirish.

Shell yomon yoki noto‘g‘ri joy emas. Aksincha, u juda foydali. Muhimi, o‘quvchi qachon vaqtinchalik tajriba qilayotganini, qachon esa saqlanishi kerak bo‘lgan `.py` dasturini yozayotganini farqlasin.

## 3. IDLE oynalari va ularning bir-biridan farqi

### Shell oynasi

Shell odatda Python ishga tushganda ochiladi. U foydalanuvchi kiritgan ifoda yoki buyruqni bajarib, natijani ko‘rsatadi. Masalan:

```pycon
>>> 2 + 3
5
>>> print("Salom")
Salom
```

Shell'da buyruq natijasi interaktiv tarzda ko‘rinadi. Biroq shell tarixidagi kodni `.py` fayl sifatida saqlagan bo‘laman deb o‘ylamaslik kerak. Shell'da yozilgan satrlar oddiy Editor fayli kabi boshqarilmaydi. Agar keyinroq qayta ishlatish kerak bo‘lsa, uni Editor fayliga ko‘chirish yoki boshidan Editor'da yozish ma’qul.

### Editor oynasi

Editor — Python faylini yozish va tahrirlash uchun mo‘ljallangan oyna. File → New File orqali ochiladi. Editor'da kod yoziladi, `File → Save` yoki `Ctrl+S` orqali saqlanadi, faylga masalan `hello_world.py` nomi beriladi. `.py` kengaytmasi faylda Python source code borligini bildiradi.

Saqlangan Editor faylini **Run → Run Module** orqali yoki odatda `F5` tugmasi bilan ishga tushirish mumkin. IDLE kerak bo‘lsa faylni saqlashni so‘raydi, so‘ng uni Shell oynasida bajaradi. Natijada Editor — kodning manbasi, Shell esa ishga tushirilgan dastur chiqishi ko‘rinadigan joy ekanini o‘quvchi ko‘radi.

### Nega boshidanoq faylni saqlash kerak?

Agar kod faqat vaqtinchalik Shell'da qolsa, keyin kompyuter yopilganda yoki Shell qayta ishga tushganda o‘sha amallarni aynan qayta tiklash qiyin bo‘lishi mumkin. `.py` fayl esa diskda saqlanadi. Uni qayta ochish, tahrirlash, boshqaga yuborish va GitHub repositoryga qo‘shish mumkin. Shuning uchun kurs davomida har bir darsning kod namunalarini `examples/dayXX/` papkasida saqlaymiz.

## 4. IDLE menyulari nimaga xizmat qiladi?

IDLE'da menyular faol oyna turiga qarab farqlanadi. Windows va Linux'da Shell va Editor oynalarining o‘z menyulari bor. Shu sabab bir oynada ko‘rgan bo‘limingiz ikkinchisida aynan o‘sha joyda turmasligi mumkin. Darsda o‘quvchilarni menyu nomlarini yodlashga emas, ularning vazifasini tushunishga o‘rgatish kerak. IDLE'ning rasmiy hujjatlari har bir menyuni batafsil tasvirlaydi: <https://docs.python.org/3/library/idle.html>.

### File

Bu menyu fayl va oyna bilan bog‘liq amallarni boshqaradi.

- **New File:** yangi, bo‘sh Editor oynasini ochadi. Birinchi dastur yozish uchun shu buyruqdan foydalanamiz.
- **Open:** diskda mavjud faylni ochadi.
- **Open Module:** Python qidirish yo‘llaridagi modulni topishga yordam beradi. Boshlang‘ich bosqichda har kuni ishlatish shart emas.
- **Recent Files:** yaqinda ochilgan fayllar ro‘yxati.
- **Save:** joriy faylni saqlaydi.
- **Save As:** faylni boshqa nom yoki joy bilan saqlaydi. Yangi dasturga nom berish kerak bo‘lganda foydali.
- **Close / Exit:** joriy oynani yoki IDLE dasturini yopadi. Saqlanmagan o‘zgarishlar bo‘lsa, saqlash taklifini e’tiborsiz qoldirmaslik kerak.

Menyu ichidagi buyruqlarning aniq joylashuvi IDLE versiyasiga qarab ozgina farq qilishi mumkin.

### Edit

Bu menyu matnni tahrirlashga xizmat qiladi.

- **Undo / Redo:** oxirgi tahrirni bekor qilish yoki qayta tiklash.
- **Cut / Copy / Paste:** matnni kesish, nusxalash va joylashtirish.
- **Select All:** oynadagi matnning barchasini belgilash.
- **Find / Find Again:** matn ichidan so‘z yoki belgini qidirish.
- **Replace:** topilgan matnni boshqa matn bilan almashtirish.
- **Go to Line:** faylning ma’lum qatoriga o‘tish.

Boshlang‘ich o‘quvchi uchun eng kerakli buyruqlar — Undo, Copy, Paste, Find va Select All.

### Shell — faqat Shell oynasida

Shell menyusi interaktiv muhitni boshqaradi.

- **View Last Restart:** Shell oxirgi marta qayta ishga tushgan joyni topishga yordam beradi.
- **Restart Shell:** interaktiv muhitni qayta ishga tushiradi; avvalgi Shell holati va o‘zgaruvchilar yo‘qolishi mumkin.
- **Previous History / Next History:** avval yozilgan buyruqlar bo‘ylab yurish.
- **Interrupt Execution:** juda uzoq ishlayotgan yoki javob bermayotgan buyruqni to‘xtatishga urinadi.

Restart Shell butun Python'ni kompyuterdan o‘chirib tashlamaydi; u faqat joriy interaktiv sessiyani yangilaydi.

### Debug — asosan xatolarni tekshirish uchun

Debug menyusidagi vositalar dasturning nima sababdan kutilgan natijani bermayotganini aniqlashga yordam beradi.

- **Debugger (toggle):** dasturni debugger orqali bajarish rejimini yoqadi yoki o‘chiradi.
- **Stack Viewer:** xatolik paytidagi chaqiruvlar ketma-ketligini ko‘rishga yordam beradi.
- **Auto-open Stack Viewer:** ayrim istisno holatlarida Stack Viewer'ning avtomatik ochilishini boshqaradi.
- **Go to File/Line:** xatolik xabarida ko‘rsatilgan fayl va qatorga o‘tishga yordam beradi.

Birinchi darsda bu vositalarning barchasidan foydalanish shart emas. Hozircha Debug — kodni shunchaki qayta yozishdan ko‘ra xatoni tekshirishga yordam beradigan vositalar borligini bilish uchun kerak. Debugger'ga keyinroq alohida qaytamiz.

### Options

Options menyusi IDLE'ning ko‘rinishi va ishlash afzalliklarini sozlashga xizmat qiladi. **Configure IDLE** ichida shrift o‘lchami, ranglar, klaviatura kombinatsiyalari, boshlanish oynasi, ba’zi tahrirlash sozlamalari va qo‘shimcha yordam manbalarini o‘zgartirish mumkin. Editor'da qator raqamlarini ko‘rsatish kabi ko‘rinish sozlamalari ham bo‘lishi mumkin.

Bu yerda har bir sozlamani o‘zgartirish kerak emas. O‘quvchi matn juda kichik bo‘lsa, shriftni kattalashtirish va kodni o‘qish qulay bo‘lishiga erishishni bilsa yetarli.

### Window

Bu menyu ochiq turgan Shell va Editor oynalari orasida almashishga yordam beradi. Bir nechta `.py` fayl ochiq bo‘lsa, kerakli oynaga tez qaytish mumkin. Bu menyu nima uchun kerakligini tushunish uchun Shell va Editor'ni bir paytda ochib ko‘rish kifoya.

### Help

Help menyusi yordam va hujjatlarga olib boradi.

- **About IDLE:** IDLE versiyasi va dastur haqida ma’lumot.
- **IDLE Help:** IDLE oynalari, menyulari va ishlatish usullari haqida hujjat.
- **Python Docs:** Python rasmiy hujjatlarini ochadi; sozlamaga qarab lokal nusxa yoki brauzerdagi hujjatlar ishlatilishi mumkin.
- **Turtle Demo:** Python'ning `turtle` moduli asosidagi namunalarni ochadi. Bu kursda keyinroq grafik misollar uchun qiziqarli bo‘lishi mumkin.

### Editor oynasida ko‘rinishi mumkin bo‘lgan Format va Run

O‘quvchilar Editor oynasida qo‘shimcha **Format** va **Run** menyularini ko‘rishlari mumkin. Bu normal holat.

**Format** kod bloklarining chekinishini tartibga solish, belgilangan qatorlarni izohga aylantirish yoki izohdan qaytarish va ayrim formatlash ishlariga yordam beradi. Keyinchalik Python'dagi indentatsiya muhim bo‘lganda bu menyu foydali bo‘ladi.

**Run** menyusi Editor'dagi faylni bajarish va tekshirish uchun ishlatiladi.

- **Run Module:** joriy dastur faylini tekshiradi, kerak bo‘lsa saqlatadi va Shell'da bajaradi.
- **Check Module:** fayldagi ayrim sintaksis muammolarini ishga tushirishdan oldin aniqlashga yordam beradi.
- **Python Shell:** Shell oynasini ochadi yoki oldinga olib chiqadi.

Birinchi darslarda asosiy odat: `File → New File`, kod yozish, `.py` sifatida saqlash, `Run → Run Module` yoki `F5` bilan ishga tushirish.

## 5. Birinchi dastur — Hello World!

Yangi Editor oynasini oching va quyidagini yozing:

```python
print("Hello World!")
```

Faylni `hello_world.py` nomi bilan saqlang va `F5` bosing. Natija Shell oynasida quyidagicha ko‘rinadi:

```text
Hello World!
```

Birinchi marta ishlatganingizda bu faqat bitta satr matn bo‘lib ko‘rinishi mumkin. Aslida dastur muvaffaqiyatli bajarilgani bir nechta narsani tekshiradi: Python ishga tushmoqda, kod sintaksisi to‘g‘ri, Editor faylni saqlay oladi, IDLE uni bajarishga uzatadi va natija Shell'da ko‘rinadi.

### Nega aynan “Hello World!”?

Bu — tarixan shakllangan dasturlash an’anasi. Brian Kernighan 1970-yillarning boshida B dasturlash tili haqidagi qo‘llanmada salomlashuv matnini chiqaruvchi juda sodda namuna ishlatgan. Bu misol keyinchalik Dennis Ritchie bilan yozilgan *The C Programming Language* kitobi orqali keng ommalashgan. Bugun ko‘plab kurslar shu an’anani davom ettiradi. Har bir tilda yozilgan Hello World sintaksisi turlicha bo‘lishi mumkin, ammo maqsadi o‘xshash: o‘rnatilgan muhitda eng sodda ishlaydigan dasturni yozib, natija chiqarishni ko‘rsatish.

Bu matnda aynan `Hello World!` yozish majburiy emas. `Salom, dunyo!` ham ishlaydi. Muhimi, o‘quvchi dastur yozish, uni ishga tushirish va natijani ko‘rish o‘rtasidagi bog‘lanishni tushunsin.

### `print` nima?

`print()` — Python'ning built-in funksiyasi. U berilgan obyektlarning matn ko‘rinishini odatda standart chiqish oqimiga, ko‘pincha Shell oynasiga chiqaradi. Qavslar ichida nimani chiqarishni yozamiz. Matn qiymati string deyiladi; string odatda bir juft qo‘shtirnoq (`"..."`) yoki bir juft yakka tirnoq (`'...'`) bilan o‘raladi.

```python
print("Hello World!")
print('Salom, dunyo!')
print("Python dasturlash tilini o‘rganamiz.")
```

Qo‘shtirnoqning o‘zi odatda natijaga chiqmaydi; u Python'ga matn literalining qayerda boshlanishi va tugashini bildiradi. Agar matn ichida qo‘shtirnoq kerak bo‘lsa, boshqa turdagi tashqi tirnoqdan yoki keyinroq o‘rganiladigan escape belgilaridan foydalanish mumkin.

### `print()` bilan vergul va `+` ishlatish

Ikkalasi ham ko‘rinishda bir nechta qismlardan matn chiqarish uchun ishlatilishi mumkin, lekin ular bir xil ish qilmaydi.

**Vergul bilan bir nechta argument berish:**

```python
print("Hello", "World!")
print("Yosh:", 18)
print("Natija:", 2 + 3)
```

Har bir argument alohida qiymat bo‘lib `print()` funksiyasiga uzatiladi. Standart holatda argumentlar orasiga bitta bo‘sh joy qo‘yiladi. Yuqoridagi kodning natijasi:

```text
Hello World!
Yosh: 18
Natija: 5
```

Bu usulda sonni stringga qo‘lda aylantirmasdan ham matn bilan birga chiqarish mumkin, chunki `print()` berilgan har bir argumentni matn sifatida ko‘rsatadi.

**`+` bilan stringlarni birlashtirish:**

```python
print("Hello" + "World!")
print("Hello" + " " + "World!")
print("Python " + "kursi")
```

Bu yerda `+` stringlarni birlashtiradi. Birinchi natija `HelloWorld!` bo‘ladi, chunki o‘zimiz bo‘sh joy qo‘shmadik. Ikkinchi natija `Hello World!` bo‘ladi.

Eng muhim farq — vergul `print()` ga bir nechta alohida argument beradi, `+` esa mos qiymatlarni bitta yangi qiymatga birlashtiradi. Shuning uchun:

```python
print("Yosh:", 18)       # ishlaydi
# print("Yosh: " + 18)   # TypeError beradi: str va int mos emas
```

Agar `+` bilan ishlatish kerak bo‘lsa, butun sonni matnga aylantirish mumkin:

```python
print("Yosh: " + str(18))
```

`str()` hozircha faqat tanishuv sifatida ko‘rsatiladi; uni keyingi mavzularda batafsil o‘rganamiz.

### `sep` va `end` — `print()`ni boshqarish

`print()`ning odatiy xatti-harakatida argumentlar orasidagi ajratgich bitta bo‘sh joy, har bir chaqiriq oxiridagi belgi esa yangi qatordir. Bu ikkisini mos ravishda `sep` va `end` orqali o‘zgartirish mumkin.

```python
print("2026", "10", "24", sep="-")
print("Ali", "Vali", "Hasan", sep=" | ")

print("Salom", end=" ")
print("dunyo!")
```

Natija:

```text
2026-10-24
Ali | Vali | Hasan
Salom dunyo!
```

`sep` bir nechta argument orasiga nima qo‘yilishini belgilaydi. `end` esa chiqarish tugagach nima qo‘yilishini belgilaydi. Bu parametrlar majburiy emas; ular ko‘rsatilmasa, odatiy qiymatlar ishlaydi. Hozircha ularni tajriba qilib ko‘rish yetarli.

### `print()`ning oddiy va foydali ko‘rinishlari

```python
print("Birinchi qator")
print("Ikkinchi qator")

print()  # bo‘sh qator chiqaradi

print("2 + 3 =", 2 + 3)
print("A", "B", "C", sep=",")
```

Python'dagi `print()` haqida to‘liq ma’lumot: <https://docs.python.org/3/library/functions.html#print>.

## 6. Kommentariyalar — kod ichidagi izohlar

Dastur kodi birinchi qarashda tushunarli bo‘lishi mumkin, lekin vaqt o‘tib, dastur kattalashgan sari muayyan qaror nima sababdan qabul qilinganini esdan chiqarish oson. Kommentariya — kod ichida dasturchiga yordam berish uchun yoziladigan, Python bajaradigan buyruq sifatida talqin qilinmaydigan izoh.

Python'da oddiy kommentariya `#` belgisi bilan boshlanadi. Belgidan keyin, shu qator oxirigacha bo‘lgan matn kommentariya hisoblanadi.

### Alohida qatordagi kommentariya

```python
# Bu dastur foydalanuvchiga salom beradi.
print("Salom!")
```

Bu ko‘rinish yangi mavzu, murakkab fikr yoki kodning maqsadini izohlash uchun qulay. Kommentariya Python'ga yangi amal bajartirmaydi.

### Kod bilan bir qatordagi kommentariya

```python
answer = 2 + 3  # oddiy misolda yig'indini hisoblaymiz
print(answer)
```

Koddan keyingi kommentariya texnik jihatdan ishlaydi, ammo uni ortiqcha ishlatish kodni zich va o‘qishni qiyin qilib qo‘yishi mumkin. Izoh juda uzun bo‘lsa, alohida qatorga yozish yaxshiroq.

### Bir necha qatorli izoh

Python'da ko‘p qatorni izohga aylantirishning odatiy usuli — har bir qator boshiga `#` yozish.

```python
# Dastur natijani chiqarishdan oldin
# o'zgaruvchini hisoblab olishi mumkin.
# Hozircha o'zgaruvchilarni keyingi darsda o'rganamiz.
```

Bu ko‘rinish ba’zan “block comment” deb ataladi, lekin u alohida maxsus ko‘p qatorli kommentariya sintaksisi emas: bu — ketma-ket yozilgan oddiy qator kommentariyalar.

### Uch qo‘shtirnoq har doim kommentariya emas

Ba’zan quyidagini ko‘ramiz:

```python
"""
Ushbu modulning vazifasi — print() misollarini ko'rsatish.
Bu matn modulning docstring'i bo'lib xizmat qiladi.
"""
```

Uch qo‘shtirnoqli matn Python'da oddiy kommentariyaning maxsus shakli emas. Bu — ko‘p qatorli string literal. Agar modul, funksiya yoki class boshida kerakli joyga qo‘yilsa, u hujjatlashtirish uchun ishlatiladigan **docstring** bo‘ladi. Docstring keyinchalik `help()` kabi vositalar orqali ko‘rinishi mumkin. Agar matn faqat `#` izohlarini almashtirish uchun tasodifan yozilsa, u ba’zi holatlarda bajariladigan string literal sifatida qoladi.

Shuning uchun boshlang‘ich qoida quyidagicha:

- Oddiy tushuntirish yoki vaqtinchalik eslatma uchun `#` ishlating.
- Modul, funksiya yoki class nima qilishini hujjatlashtirish kerak bo‘lsa, tegishli joyda docstring ishlating.
- Uch qo‘shtirnoqni “Python'dagi ko‘p qatorli kommentariya” deb tushuntirmang; bu texnik jihatdan aniq emas.

### Yaxshi kommentariya qanday bo‘ladi?

Kommentariya kodni takrorlab bermasligi, aksincha zarur kontekstni tushuntirishi kerak.

```python
# Yaxshi: sababini tushuntiradi.
# Natija foydalanuvchiga alohida qatorda ko'rinishi kerak.
print("Hisoblash tugadi")
```

Quyidagi kabi izoh ko‘pincha ortiqcha:

```python
# print funksiyasini chaqiramiz
print("Salom")
```

Yangi o‘quvchi uchun bu izoh yomon deb qat’iy aytish shart emas, lekin tajriba ortgan sayin kodning o‘zi ko‘rsatib turgan narsani izohlash o‘rniga, nima uchun shunday qilinganini tushuntirishga intilish kerak.

## 7. Eng ko‘p uchraydigan xatolar

**Kod Shell va Editor orasida adashib yozildi.** Shell interaktiv buyruqlar uchun, Editor esa saqlanadigan fayl uchun ekanini tekshiring. Agar kodni `.py` fayl sifatida topshirish kerak bo‘lsa, uni Editor'da saqlang.

**`>>>` belgisi kodga qo‘shib yozildi.** Shell promptini ko‘chirib Editor'ga joylashtirmang. Editor'da `print("Hello World!")` deb yoziladi, `>>> print(...)` emas.

**Fayl `.py` emas, `.py.txt` bo‘lib saqlandi.** Windows kengaytmalarni yashirishi mumkin. Fayl nomi va saqlangan joyni tekshiring. File Explorer'da fayl kengaytmalarini ko‘rsatishni yoqish foydali.

**O‘zgarishlar saqlanmadi.** Kodni o‘zgartirgandan keyin `Ctrl+S` tugmasini bosing. IDLE saqlashni eslatishi mumkin, lekin saqlash holatini o‘zingiz nazorat qiling.

**`print` va `+`ni bir xil deb o‘ylash.** `print("A", "B")` argumentlar orasiga bo‘sh joy qo‘yadi; `"A" + "B"` esa stringlarni birlashtirib `AB` hosil qiladi.

**Son bilan string `+` orqali birlashtirildi.** `"Age: " + 18` TypeError beradi, chunki biri string, biri integer. `print("Age:", 18)` yoki `print("Age: " + str(18))` ishlaydi.

**Kommentariya sintaksisi noto‘g‘ri yozildi.** Python'da oddiy kommentariya `#` bilan boshlanadi. Boshqa tillarda uchraydigan `//` Python'ning oddiy kommentariya belgisi emas.

**Natijada qo‘shtirnoqlar chiqishi kutilmoqda.** `print("Salom")` natijada `Salom` chiqaradi, qo‘shtirnoqni emas. Qo‘shtirnoqlar Python kodidagi string chegarasini belgilaydi.

**Python bir necha marta o‘rnatildi.** Qayta o‘rnatishdan avval `python --version` yoki `py --version` orqali qaysi interpreter ishlayotganini tekshiring. Bir nechta o‘rnatish bo‘lishi mumkin, ammo muammoni tushunmasdan ularni o‘chirish shart emas.

## 8. Dars yakunida tekshiruv

O‘quvchi quyidagi savollarga o‘z so‘zlari bilan javob bera olishi kerak:

1. Python dasturlash tili, interpreter va IDLE orasidagi farq nima?
2. IDLE ochilganda ko‘rinadigan `>>>` nimani anglatadi?
3. Nima uchun saqlanadigan dastur uchun `File → New File` ishlatamiz?
4. Editor oynasida yozilgan `.py` fayl qanday ishga tushiriladi?
5. “Hello World!” dasturi nimani tekshiradi va nega odatda birinchi misol sifatida tanlanadi?
6. `print("A", "B")` va `print("A" + "B")` orasida qanday farq bor?
7. `sep` va `end` vazifasi nima?
8. Kommentariya nima uchun kerak va u qaysi belgi bilan boshlanadi?
9. Nega uch qo‘shtirnoqli matnni oddiy kommentariya deb atash to‘liq to‘g‘ri emas?
10. Python o‘rnatilganini qanday tekshirish mumkin?

## O‘qituvchi uchun qayd

Darsdan keyin haqiqatan o‘tilgan qismlarni belgilang. Rejadagi qo‘shimcha tushuntirishlar darsda ulgurilmagan bo‘lsa, ularni avtomatik ravishda “o‘tilgan” deb hisoblamang.

- [ ] Python.org saytidan o‘rnatish faylini topish va yuklab olish ko‘rsatildi.
- [ ] O‘rnatish va konfiguratsiya farqi tushuntirildi.
- [ ] Python, interpreter va IDLE farqi tushuntirildi.
- [ ] Shell va Editor farqi ko‘rsatildi.
- [ ] IDLE menyularining vazifalari tushuntirildi.
- [ ] `Hello World!` dasturi yozildi va ishga tushirildi.
- [ ] Vergul orqali bir nechta `print()` argumenti ko‘rsatildi.
- [ ] Stringlarni `+` yordamida birlashtirish ko‘rsatildi.
- [ ] Kommentariyalar misollar bilan tushuntirildi.
- [ ] Uy vazifasi tushuntirildi.
