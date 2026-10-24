# Day 02 — Sanoq sistemalari, raqamli mantiq va kompyuter xotirasi

**Daraja:** Beginner, chuqur tushuntirish bilan  
**Asosiy mavzular:** bit va bayt, ikkilik mantiq, tranzistor, SRAM/DRAM, sanoq sistemalari, konvertatsiya, floating-point sonlar.

Bu darsda biz kundalik hayotda ko'rinmaydigan, lekin dasturlashni chuqurroq tushunish uchun muhim bo'lgan savollardan boshlaymiz: nega kompyuterlar odatda ikkilik tizimdan foydalanadi? Elektr toki va kuchlanishning o'zi qanday qilib `0` yoki `1` deb talqin qilinadi? Xotirada bit qanday saqlanadi? Nima uchun $1010_2$, $12_8$, $A_{16}$ va $10_{10}$ turli yozuvlar bo'lsa ham bir xil miqdorni ifodalashi mumkin? Va nihoyat, nega $0.1 + 0.2$ ayrim dasturlash tillarida kutilgan $0.3$ ga aynan teng bo'lmaydi?

Darsning asosiy g'oyasi shuki: **sanoq sistemasi — qiymatni yozish usuli; raqamli elektronika esa fizik holatlarni ishonchli tarzda mantiqiy qiymatlar sifatida kodlash usulidir.** Bu ikki tushuncha bir-biriga bog'langan, lekin aynan bir narsa emas.

## 1. Nima uchun sanoq sistemalari kerak?

Tasavvur qiling, sizda 27 ta kitob bor. Siz bu miqdorni $27$ deb yozishingiz mumkin. Boshqa sanoq sistemasida ayni miqdor boshqacha yoziladi: ikkilikda $11011_2$, sakkizlikda $33_8$, o'n oltilikda $1B_{16}$. Yozuvlar har xil, ammo kitoblar soni o'zgarmaydi.

Demak, sonning **qiymati** bilan uning **yozilishi**ni farqlash zarur. Sanoq sistemasi — sonlarni belgilash va yozish qoidalari to'plami. U miqdorlarni ifodalashga, taqqoslashga, hisoblashga va ma'lumotlarni ixcham yozishga yordam beradi.

Odamlar kundalik hayotda ko'pincha o'nlik sanoq sistemasidan foydalanadi. Buning tarixiy sabablari turlicha bo'lishi mumkin; inson qo'llaridagi o'nta barmoq bunga qulay asos bo'lgan, degan keng tarqalgan izoh mavjud. Ammo o'nlik yagona mumkin bo'lgan sistema emas. Soat va vaqt o'lchashda 60 likka, eski burchak o'lchovlarida 360 likka, kompyuterlar bilan ishlashda esa ikkilik va o'n oltilik yozuvlarga duch kelamiz.

Sanoq sistemasining asosi nechta turli raqam belgisi ishlatishimizni va pozitsiyalar qiymati qanday ortishini belgilaydi. O'nlik sistemada asos $10$; raqamlar $0$ dan $9$ gacha. Ikkilikda asos $2$; raqamlar faqat $0$ va $1$. Sakkizlikda $0$–$7$, o'n oltilikda esa $0$–$9$ va $A$–$F$ ishlatiladi.

Umumiy qoida: **asosi $b$ bo'lgan pozitsion sistemada har bir raqam $0$ dan $b - 1$ gacha bo'lishi kerak.** Masalan, $102_2$ noto'g'ri yozuv, chunki ikkilikda $2$ raqami yo'q. Xuddi shunday, $8_8$ ham noto'g'ri, chunki sakkizlikda $8$ ishlatilmaydi.

## 2. Pozitsion yozuv: raqamning o'rni nega muhim?

O'nlikdagi $583$ sonini ko'raylik. Bu shunchaki uchta belgi emas. Uning qiymati quyidagicha tuziladi:

$$583 = 5 \times 10^2 + 8 \times 10^1 + 3 \times 10^0$$

Ya'ni:
- chapdagi $5$ — beshta yuzlik;
- o'rtadagi $8$ — sakkizta o'nlik;
- o'ngdagi $3$ — uchta birlik.

Raqamning qiymati uning o'rni bilan birga aniqlanadi. Bu **pozitsion sanoq sistemasi**ning asosiy xususiyati. Eng o'ngdagi butun qism raqami $b^0$ ga, undan chapdagisi $b^1$ ga, keyingisi $b^2$ ga ko'paytiriladi.

Xuddi shu usul ikkilikda ham ishlaydi:

$$101101_2 = 1 \times 2^5 + 0 \times 2^4 + 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$$
$$= 32 + 0 + 8 + 4 + 0 + 1 = 45_{10}$$

Bu yerda $_2$ sonning ikkilikda, $_{10}$ esa o'nlikda yozilganini bildiradi. Pastki indeksni ishlatishning sababi — bir xil $101$ yozuvi turli asoslarda turli qiymatga ega bo'lishi mumkin. Masalan, $101_2 = 5_{10}$, ammo $101_3 = 10_{10}$.

Umumiy formula:

$$(d_n d_{n-1} \dots d_2 d_1 d_0)_b = d_n \times b^n + d_{n-1} \times b^{n-1} + \dots + d_1 \times b^1 + d_0 \times b^0$$

Bu yerda $b$ — sanoq sistemasining asosi, $d$ lar esa shu sistemada ruxsat etilgan raqamlardir. Formula sanoq sistemasining eng muhim qoidasini beradi: har bir raqam o'z pozitsiyasining asosi darajasiga ko'paytiriladi va natijalar qo'shiladi.

## 3. Nega aynan 0 va 1? Kompyuter ichida rostdan ham 0 va 1 bormi?

Bu savolga aniq javob berish uchun ikki qatlamni ajratamiz: **fizik qurilma** va **mantiqiy model**.

Tabiatdagi elektr kuchlanishi faqat ikki qiymatga ega emas. Kuchlanish ko'plab oraliq qiymatlarni olishi mumkin. Masalan, bir nuqtadagi kuchlanish $0.7$ V, $1.2$ V yoki $2.8$ V bo'lishi mumkin. Bunday uzluksiz yoki juda ko'p qiymatli fizik kattalik analog miqdor sifatida qaraladi. Tranzistorning fizik xatti-harakati ham ideal, sehrli "yoqilgan/o'chirilgan" tugmadan murakkabroq: u kuchlanishga qarab tok oqimini boshqaradi.

Lekin raqamli elektronika bu fizik xatti-harakatdan foydalanib, ko'p holatlarni ikkita mantiqiy sinfga ajratadi. Elektron sxema ishlab chiqilganda, past kuchlanish oralig'i mantiqiy $0$, yuqori kuchlanish oralig'i esa mantiqiy $1$ deb talqin qilinishi kelishib olinadi. Muhim jihat: **$0$ va $1$ — kuchlanishning o'zi emas, balki kuchlanish yoki boshqa fizik holatga berilgan mantiqiy ma'nodir.**

Masalan, ma'lum bir sxema uchun $0$ juda past kuchlanishlar, $1$ esa yetarlicha yuqori kuchlanishlar bilan ifodalanishi mumkin. Ammo $0$ har doim aynan $0.000$ V, $1$ esa har doim aynan $5.000$ V degani emas. Zamonaviy sxemalarda ta'minot kuchlanishi $5$ V bo'lishi shart emas; $3.3$ V yoki bundan past qiymatlar ham uchraydi. To'g'ri chegaralar qurilma va mantiq oilasining elektr spetsifikatsiyasiga bog'liq.

### Nega har qanday kuchlanishni alohida raqam qilib ishlatmaymiz?

Nazariy jihatdan bir nechta kuchlanish darajasidan foydalanadigan ko'p qiymatli tizimni qurish mumkin. Hatto uch holatli yoki boshqa ko'p qiymatli mantiq bo'yicha tadqiqotlar ham bor. Demak, ikkilik — tabiatning yagona yo'li emas.

Ammo real elektron sxemada shovqin, harorat, ishlab chiqarishdagi farqlar, simlardagi qarshilik, boshqa sxemalarning ta'siri va elektr signallarining vaqt bo'yicha o'zgarishi mavjud. Agar biz har bir kichik kuchlanish farqiga alohida ma'no yuklasak, shovqin signaldagi ma'noni o'zgartirib yuborishi ehtimoli ortadi. Ikki keng ajratilgan holatni farqlash esa odatda ancha ishonchliroq.

Raqamli sxemada faqat bitta keskin chegara bo'lishi ham yetarli emas. Ishonchli ishlash uchun $0$ deb qabul qilinishi kafolatlangan past diapazon va $1$ deb qabul qilinishi kafolatlangan yuqori diapazon belgilanadi. Ularning orasidagi soha ayrim sxemalarda noaniq bo'lishi mumkin; normal ishlashda sxemalar ushbu noaniq oraliqqa tushmasligi kerak. Chiqish va kirish chegaralari orasidagi zaxira **noise margin**, ya'ni shovqin zaxirasi deb ataladi.

Buni oddiy tasavvur bilan tushuntiring: termometrdagi $36.6$ °C kabi uzluksiz qiymatni o'lchash bilan ikki holatli tugmani bosilgan yoki bosilmagan deb aniqlash bir xil vazifa emas. Ikkinchi holatda ikkita aniq ajratiladigan holatni loyihalash osonroq. Raqamli elektronika ana shu farqdan foydalanadi.

### "Barcha ma'lumot elektr toki qiymatimi?"

Bu fikrning bir qismi to'g'ri, lekin uni aniqroq aytish kerak. Elektron kompyuter ichida ma'lumot fizik qurilmalar holati orqali ifodalanadi. Ko'plab raqamli zanjirlarda signalni ifodalash uchun kuchlanishlardan, xotira elementlarida esa kuchlanish va elektr zaryadidan foydalaniladi. Boshqa saqlash qurilmalari ma'lumotni magnit holatlar, flash xotirada zaryad tuzoqlari yoki boshqa fizik xususiyatlar orqali saqlashi mumkin.

Shuning uchun barcha xotira "faqat elektr tokining qiymatlaridan iborat" deyish haddan tashqari soddalashtirish bo'ladi. To'g'riroq fikr: **ma'lumotning o'zi mavhum; apparat esa uni saqlash va qayta ishlash mumkin bo'lgan fizik holatlar yordamida kodlaydi.** Dasturdagi `True`, `False`, `45` yoki `"Salom"` kabi tushunchalar apparatda bitlar va boshqa kodlashlar orqali ifodalanadi.

## 4. Tranzistor va raqamli kalit g'oyasi

Tranzistor — zamonaviy elektronikaning asosiy komponentlaridan biri. Uning vazifalaridan biri boshqaruvchi elektr signali yordamida tok oqimini boshqarishdir. Raqamli sxemada tranzistorlar ko'pincha elektron kalit singari ishlatiladi: muayyan sharoitda tok yo'liga ruxsat beriladi, boshqa sharoitda esa tok yo'li to'siladi.

Buni devordagi chiroq kaliti bilan o'xshatish mumkin, lekin o'xshatishning chegarasi bor. Mexanik kalit qo'l bilan boshqariladi; tranzistor esa juda kichik elektr signali yordamida boshqarilishi va mikrosxema ichida nihoyatda ko'p miqdorda joylashtirilishi mumkin.

Tranzistorlar mantiqiy eshiklarni — masalan, NOT, AND, OR — yaratishga imkon beradi. Mantiqiy eshiklar bitlar ustida amallar bajaradi. Ko'plab eshiklarni birlashtirib, qo'shish, solishtirish, qiymat tanlash, xotira boshqarish va protsessor hisob-kitoblari kabi vazifalarni bajaruvchi murakkab sxemalar quriladi.

$0$ va $1$ ni ishlatishning afzalligi shundaki, mantiqiy qoidalar oddiy va elektron sxemalar ularni ko'p marta qayta tiklab, shovqin ta'sirini cheklashi mumkin. Bu kompyuterning barcha ichki jarayoni oddiygina ikkita ideal kuchlanishdan iborat degani emas; bu — murakkab fizik qurilmani ishonchli mantiqiy model yordamida loyihalash usuli.

## 5. Bit, bayt va ma'lumotni kodlash

**Bit** — binary digit so'zlaridan qisqartma. U ikkita mantiqiy qiymatdan birini ifodalaydi: $0$ yoki $1$.

Bitta bit ikki xil holatni ifodalay oladi. Ikki bit $00$, $01$, $10$, $11$ ko'rinishidagi to'rtta kombinatsiyaga ega. Uch bit $2^3 = 8$ xil kombinatsiyani, sakkiz bit esa $2^8 = 256$ xil kombinatsiyani ifodalay oladi.

Umuman, $n$ ta bitdan $2^n$ xil kombinatsiya tuzish mumkin. Shu sababli 8 bit bir qiymatni kodlash uchun 256 ta mumkin bo'lgan naqsh beradi. Ammo bu 256 ta naqshning qanday ma'no anglatishi ishlatilayotgan kodlashga bog'liq. Masalan, ular 0–255 oralig'idagi butun sonlar, belgilar kodlari yoki boshqa ma'lumotlar bo'lishi mumkin.

**Bayt (byte)** odatda 8 bitdan iborat. Shuning uchun:
- 1 bit — ikkita holatdan biri;
- 1 bayt — 8 bit;
- 1 bayt 256 xil bit naqshini ifodalashi mumkin.

Bu yerda muhim farq bor: sakkiz bitli naqshning o'zi avtomatik ravishda "son" yoki "harf" emas. Uning ma'nosi qanday talqin qilinishiga bog'liq. Masalan, $01000001_2$ ikkilik son sifatida $65_{10}$ ga teng; ASCII kodlashida esa `A` harfiga mos keladi.

## 6. SRAM va DRAM: xotirada bit qanday saqlanadi?

Kompyuter xotirasining barcha turlari bir xil tuzilishga ega emas. Operativ xotiraning keng tarqalgan ikki turi — **SRAM (Static RAM)** va **DRAM (Dynamic RAM)**. Ularning asosiy farqi bitning fizik jihatdan qanday saqlanishidadir.

### SRAM — holatni qayta ushlab turuvchi sxema

SRAM katakchasi odatda o'zaro ulangan tranzistorlardan qurilgan bistabil sxema — latch — yordamida bit holatini saqlaydi. Keng tarqalgan 6T SRAM katakchasida olti tranzistor ishlatiladi. Sxemaning teskari aloqa xususiyati holatlardan birini elektr ta'minoti mavjud ekan saqlab turishga yordam beradi.

SRAM katakchasi DRAM katakchasiga qaraganda ko'proq tranzistor talab qiladi, shuning uchun bir xil chip maydoniga kamroq bit joylashtirish mumkin. Biroq SRAM odatda tez ishlaydi va shu sababli protsessor keshlarida hamda tezkor kichik xotiralarda keng qo'llanadi.

"Static" so'zi ma'lumot kompyuter o'chirilganidan keyin ham saqlanadi degani emas. SRAM ham **volatile**, ya'ni elektr ta'minoti uzilganda ma'lumotini yo'qotadigan xotira turidir. "Static" uning quvvat bor paytda bitni saqlash usuliga taalluqli.

### DRAM — zaryad yordamida saqlash

Oddiy DRAM katakchasi odatda bitta tranzistor va bitta kondensatordan tashkil topadi. Kondensator elektr zaryadini saqlaydi; zaryad holati bit qiymatini ifodalash uchun ishlatiladi. Amaliy sxemalarda bu ideal "zaryad bor yoki yo'q" holati emas: zaryad miqdori, o'qish zanjirlari va sezgir kuchaytirgichlar orqali fizik signaldan mantiqiy qiymat aniqlanadi.

Kondensatordagi zaryad vaqt o'tishi bilan sizib chiqishi mumkin. Shu sababli DRAM hujayralaridagi ma'lumot davriy ravishda yangilanadi — **refresh** qilinadi. DRAM zichligi yuqori va bir bitni saqlash uchun nisbatan kam element talab qiladi; asosiy operativ xotira sifatida keng ishlatilishining muhim sababi shu. Lekin refresh boshqaruvi zarur va DRAM odatda SRAMga qaraganda sekinroq.

### SRAM va DRAM qisqacha taqqoslanishi

| Xususiyat | SRAM | DRAM |
|---|---|---|
| Bitni saqlash usuli | Tranzistorlar yordamida tuzilgan latch | Kondensator zaryadi va kirish tranzistori |
| Refresh | Oddiy ishlashda davriy DRAM refresh’i talab qilinmaydi | Davriy refresh talab qilinadi |
| Tezlik | Odatda tezroq | Odatda sekinroq |
| Zichlik | Katakcha kattaroq, zichligi pastroq | Katakcha kichikroq, zichligi yuqoriroq |
| Odatdagi qo'llanish | CPU kesh va kichik tezkor xotiralar | Asosiy operativ xotira (RAM) |
| Quvvat uzilganda | Ma'lumot yo'qoladi | Ma'lumot yo'qoladi |

Bu jadval umumiy tamoyilni ko'rsatadi; haqiqiy tezlik, quvvat sarfi va dizayn xususiyatlari qurilmaga bog'liq.

## 7. Nega ikkilik sanoq sistemasi kompyuterlar uchun qulay?

Agar xotira va mantiqiy sxemalar ikkita holatni ishonchli ajrata olsa, ikkilik sanoq sistemasi ularni tasvirlash uchun tabiiy tanlov bo'ladi. Bitta bit $0$ yoki $1$ holatini bildiradi. Bir nechta bit birgalikda kattaroq sonlarni, belgilarni, buyruqlarni yoki ma'lumotlar tuzilishini kodlashi mumkin.

Bu yerda ehtiyot bo'lish kerak: kompyuter faqat sonlarni saqlamaydi. Matn, rasm, tovush, video va dastur buyruqlari ham turli kodlashlar orqali bitlar ketma-ketligiga aylantiriladi. Bitlar fizik xotira yoki signallarda saqlanadi va qurilma ularni kelishilgan qoidalarga muvofiq talqin qiladi.

Nima uchun aynan ikkilik qulay? Chunki ikkita mantiqiy holatni fizik jihatdan farqlash, ularni sxemalar orqali qayta tiklash va shovqinga bardoshli qilish odatda ko'p darajali holatlarni ajratishdan oson. Bu yagona nazariy imkoniyat emas, ammo zamonaviy raqamli kompyuterlarda juda samarali muhandislik tanlovidir.

## 8. Ikkilik, sakkizlik, o'nlik va o'n oltilik sistemalar

Endi fizik asosdan sonlarni yozish usuliga o'tamiz.

| Sanoq sistemasi | Asos | Ishlatiladigan raqamlar | Misol |
|---|---:|---|---|
| Ikkilik (binary) | 2 | $0, 1$ | $101101_2$ |
| Sakkizlik (octal) | 8 | $0$–$7$ | $55_8$ |
| O'nlik (decimal) | 10 | $0$–$9$ | $45_{10}$ |
| O'n oltilik (hexadecimal) | 16 | $0$–$9, A$–$F$ | $2D_{16}$ |

O'n oltilik sistemada harflar qo'shimcha raqamlar o'rnida ishlatiladi:

| O'nlik qiymat | Hex raqam | Ikkilik ekvivalenti |
|---:|---|---|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| 2 | 2 | 0010 |
| 3 | 3 | 0011 |
| 4 | 4 | 0100 |
| 5 | 5 | 0101 |
| 6 | 6 | 0110 |
| 7 | 7 | 0111 |
| 8 | 8 | 1000 |
| 9 | 9 | 1001 |
| 10 | A | 1010 |
| 11 | B | 1011 |
| 12 | C | 1100 |
| 13 | D | 1101 |
| 14 | E | 1110 |
| 15 | F | 1111 |

Bu yerda $A$ harfi o'n oltilik sistemadagi o'nlik qiymati 10 bo'lgan raqam, $F$ esa 15 qiymatini bildiradi.

## 9. Har qanday sanoq sistemasidan o'nlikka o'tish

Eng umumiy usullardan biri — pozitsion formuladan foydalanish. Har bir raqamni o'z o'rniga mos asos darajasiga ko'paytiramiz va barcha natijalarni qo'shamiz.

### Misol 1: $110101_2$ ni o'nlikka aylantirish

Yozamiz:
$$110101_2 = 1 \times 2^5 + 1 \times 2^4 + 0 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$$

Darajalarni hisoblaymiz:
$$= 1 \times 32 + 1 \times 16 + 0 \times 8 + 1 \times 4 + 0 \times 2 + 1 \times 1$$
$$= 32 + 16 + 4 + 1 = 53_{10}$$

Demak, $110101_2 = 53_{10}$.

### Misol 2: $243_5$ ni o'nlikka aylantirish

Besh asosli sistemada $0, 1, 2, 3, 4$ raqamlari ruxsat etilgan. Shuning uchun $243_5$ to'g'ri yozuv:

$$243_5 = 2 \times 5^2 + 4 \times 5^1 + 3 \times 5^0$$
$$= 2 \times 25 + 4 \times 5 + 3 \times 1$$
$$= 50 + 20 + 3 = 73_{10}$$

Demak, $243_5 = 73_{10}$.

### Misol 3: $2D7_{16}$ ni o'nlikka aylantirish

Hex sistemada $D = 13$:

$$2D7_{16} = 2 \times 16^2 + 13 \times 16^1 + 7 \times 16^0$$
$$= 2 \times 256 + 13 \times 16 + 7$$
$$= 512 + 208 + 7 = 727_{10}$$

**Yodingizda bo'lsin:** asosni ko'paytiruvchi sifatida ishlatamiz; raqamning o'zi esa o'sha sistemadagi haqiqiy qiymatidir.

## 10. O'nlik butun sonni boshqa asosga o'tkazish: bo'lish va qoldiq

O'nlikdagi butun sonni boshqa asosga aylantirish uchun sonni yangi asosga ketma-ket bo'lamiz. Har safar bo'lishdagi **qoldiqni yozib olamiz**. Jarayon bo'linma 0 bo'lguncha davom etadi. Javob qoldiqlarni **oxiridan boshiga qarab** o'qish orqali hosil bo'ladi.

### Misol: $156_{10}$ ni yettilik sistemaga o'tkazish

| Amal | Bo'linma | Qoldiq |
|---|---:|---:|
| $156 \div 7$ | 22 | 2 |
| $22 \div 7$ | 3 | 1 |
| $3 \div 7$ | 0 | 3 |

Qoldiqlar yuqoridan pastga $2, 1, 3$ bo'lib chiqdi, lekin javobni teskari o'qiymiz: $312_7$.

Tekshirish:
$$312_7 = 3 \times 7^2 + 1 \times 7^1 + 2 = 147 + 7 + 2 = 156_{10}$$

Demak, $156_{10} = 312_7$.

### Nega qoldiqlarni teskari o'qiymiz?

Birinchi qoldiq sonning eng kichik razryadini — $b^0$ koeffitsiyentini beradi. Keyingi qoldiq $b^1$, undan keyingisi $b^2$ razryadiga tegishli bo'ladi. Biz hisoblashni kichik razryaddan boshlaganimiz uchun, raqamlarni javob sifatida yozishda ularni teskari tartibda olamiz.

## 11. Istalgan bir asosdan istalgan boshqa asosga o'tish

Masalan, $243_5$ ni $3$ asosli sistemaga o'tkazish kerak bo'lsin. Manba asosidan to'g'ridan-to'g'ri o'tish qiyin ko'rinsa, ikkita bosqichdan foydalanamiz:

1. Manba sistemasidan o'nlikka o'tamiz.
2. O'nlikdan maqsad sistemasiga o'tamiz.

Birinchi qismni yuqorida hisobladik: $243_5 = 73_{10}$.

Endi $73_{10}$ ni uch asosli sistemaga o'tkazamiz:

| Amal | Bo'linma | Qoldiq |
|---|---:|---:|
| $73 \div 3$ | 24 | 1 |
| $24 \div 3$ | 8 | 0 |
| $8 \div 3$ | 2 | 2 |
| $2 \div 3$ | 0 | 2 |

Qoldiqlarni teskari o'qisak $2201_3$ hosil bo'ladi.

Tekshirish:
$$2201_3 = 2 \times 3^3 + 2 \times 3^2 + 0 \times 3^1 + 1 = 54 + 18 + 1 = 73_{10}$$

Shunday qilib, **$243_5 = 2201_3$**.

## 12. Nega ikkilikdan sakkizlikka triadalar orqali o'tamiz?

Sakkizlikning asosi $8$, ikkilikning asosi $2$. Ularning orasidagi muhim matematik bog'lanish:
$$8 = 2^3$$

Demak, uch bit yordamida aynan sakkizta kombinatsiya ifodalanadi. Shuning uchun ikkilik sonni o'ngdan boshlab uch bitdan guruhlash va har bir guruhni bitta sakkizlik raqamiga almashtirish mumkin. Bunday uch bitli guruh **triada** deb ataladi.

### Ikkilikdan sakkizlikka misol

$1101011_2$ ni sakkizlikka aylantiramiz.

O'ngdan boshlab uch bitdan ajratamiz:
`1 101 011`

Eng chap guruhda bitta bit qolgan. Guruh to'liq uch bit bo'lishi uchun uning chap tomoniga ikkita nol qo'shamiz:
`001 101 011`

Endi guruhlarni alohida o'qiymiz:
- $001_2 = 1_8$
- $101_2 = 5_8$
- $011_2 = 3_8$

Natija: $1101011_2 = 153_8$.

### Sakkizlikdan ikkilikka

Teskari yo'nalishda har bir sakkizlik raqamni aynan uch bit bilan almashtiramiz:
$572_8 \rightarrow 101\ 111\ 010_2$

## 13. Nega ikkilikdan o'n oltilikka tetradalar orqali o'tamiz?

O'n oltilikning asosi $16$, ikkilikning asosi $2$:
$$16 = 2^4$$

To'rt bitda $2^4 = 16$ xil kombinatsiya bor. Bu $0$ dan $F$ gacha bo'lgan 16 ta hex raqamning har biriga bittadan mos keladi. To'rt bitli guruh **tetrada** yoki ko'pincha **nibble** deb ataladi.

### Ikkilikdan hexga misol

$1101011011_2$ ni hexga o'tkazamiz.

O'ngdan boshlab to'rt bitdan guruhlaymiz:
`11 0101 1011`

Chapdagi guruh to'liq emas. Chap tomondan ikkita nol qo'shamiz:
`0011 0101 1011`

Endi har bir guruhni tarjima qilamiz:
- $0011_2 = 3_{16}$
- $0101_2 = 5_{16}$
- $1011_2 = B_{16}$

Natija: $1101011011_2 = 35B_{16}$.

### Hexdan ikkilikka

Har bir hex belgini to'rt bit bilan almashtiramiz:
$A6F_{16} \rightarrow 1010\ 0110\ 1111_2$.

## 14. Uch va to'rt bitli moslik jadvallari

### Triada: ikkilikdan sakkizlikka

| Ikkilik | Sakkizlik | O'nlik qiymat |
|---|---:|---:|
| `000` | 0 | 0 |
| `001` | 1 | 1 |
| `010` | 2 | 2 |
| `011` | 3 | 3 |
| `100` | 4 | 4 |
| `101` | 5 | 5 |
| `110` | 6 | 6 |
| `111` | 7 | 7 |

### Tetrada: ikkilikdan hexga

| Ikkilik | Hex | O'nlik qiymat |
|---|---:|---:|
| `0000` | 0 | 0 |
| `0001` | 1 | 1 |
| `0010` | 2 | 2 |
| `0011` | 3 | 3 |
| `0100` | 4 | 4 |
| `0101` | 5 | 5 |
| `0110` | 6 | 6 |
| `0111` | 7 | 7 |
| `1000` | 8 | 8 |
| `1001` | 9 | 9 |
| `1010` | A | 10 |
| `1011` | B | 11 |
| `1100` | C | 12 |
| `1101` | D | 13 |
| `1110` | E | 14 |
| `1111` | F | 15 |

## 15. Kasr sonlar ham pozitsion qoida bilan ifodalanadi

Pozitsion sanoq sistemasi kasr qismida ham xuddi shu qoidaga asoslanadi. Ikkilik nuqtasidan chapdagi razryadlar $2^0, 2^1, 2^2$ kabi musbat darajalarga, o'ngdagi razryadlar esa $2^{-1}, 2^{-2}, 2^{-3}$ kabi manfiy darajalarga tegishli.

Masalan:
$$101.101_2 = 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 + 1 \times 2^{-1} + 0 \times 2^{-2} + 1 \times 2^{-3}$$
$$= 4 + 0 + 1 + 0.5 + 0 + 0.125 = 5.625_{10}$$

## 16. O'nlik kasrni ikkilikka o'tkazish: ketma-ket ko'paytirish

Kasr qismiga $2$ ni takroran ko'paytiramiz. Har bir qadamda natijaning butun qismi navbatdagi ikkilik raqam bo'ladi.

### Misol: $0.625_{10}$ ni ikkilikka o'tkazish

| Qadam | Kasr qismini 2 ga ko'paytirish | Natijaning butun qismi | Keyingi kasr qismi |
|---|---|---:|---:|
| 1 | $0.625 \times 2 = 1.25$ | 1 | 0.25 |
| 2 | $0.25 \times 2 = 0.5$ | 0 | 0.5 |
| 3 | $0.5 \times 2 = 1.0$ | 1 | 0 |

Hosil bo'lgan butun qismlarni yuqoridan pastga o'qiymiz: $0.101_2$.

## 17. Nega ayrim kasrlar ikkilikda cheksiz davom etadi?

$0.1_{10}$ ni ikkilikka aylantirsak:
$0.1 \times 2 = 0.2$  $\rightarrow$ butun qismi $0$
$0.2 \times 2 = 0.4$  $\rightarrow$ butun qismi $0$
$0.4 \times 2 = 0.8$  $\rightarrow$ butun qismi $0$
$0.8 \times 2 = 1.6$  $\rightarrow$ butun qismi $1$, kasr qismi $0.6$
$0.6 \times 2 = 1.2$  $\rightarrow$ butun qismi $1$, kasr qismi $0.2$

Endi $0.2$ kasr qismiga qaytdik. Shu ketma-ketlik takrorlanadi:
$$0.1_{10} = 0.00011001100110011\dots_2$$

Bu xato hisoblaganimiz uchun emas. Bu sonning ikkilikdagi **aniq yozuvi tugamaydigan, davriy kasr** bo'lgani uchun. Ikkilik kasrning chekli bo'lishi uchun qisqartirilgan kasr maxraji faqat $2$ ning darajasidan iborat bo'lishi kerak.

## 18. Bu holat dasturlashga qanday ta'sir qiladi?

Ko'p tillarda odatiy `float` tipi IEEE 754 formatiga mos keladi. Sonning cheksiz ikkilik yozuvini to'liq saqlash mumkin emas: kompyuter unga eng yaqin ifodalanadigan qiymatni tanlaydi.

Python'da:
```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
```
Natija:
```text
0.30000000000000004
False
```
Natija matematik jihatdan ideal o'nlik hisob-kitob bilan aynan bir xil chiqishi shart emas.

### Python misoli
```python
from decimal import Decimal
from math import isclose

print(0.1 + 0.2 == 0.3) # False
print(isclose(0.1 + 0.2, 0.3)) # True

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3")) # True
```

## 19. Eng muhim tushunchalarni bir-biriga bog'lash

Kompyuter fizik qurilma: elektron sxemalar holatlarni mantiqiy $0$ va $1$ sifatida ishonchli talqin qilish uchun loyihalanadi. Bitta bit ikkita holatdan birini bildiradi; ko'plab bitlar ma'lumotlarni kodlaydi. 
Sanoq sistemalari esa shu qiymatlarni yozish usulidir. Ikkilik kompyuter mantiqiga mos, o'nlik kundalik hisoblarda qulay, o'n oltilik esa uzun bit qatorlarini ixcham yozishga yordam beradi.

## Darsni yakunlash uchun savollar

1. Sanoq sistemasi nima va sonning qiymati bilan yozilishi o'rtasida qanday farq bor?
2. Asosi $b$ bo'lgan sistemada qaysi raqamlar ishlatilishi mumkin?
3. Nima uchun zamonaviy raqamli elektronika ko'pincha ikki mantiqiy holatdan foydalanadi?
4. $0$ va $1$ fizik kuchlanishning o'zi emas, deyish nimani anglatadi?
5. SRAM va DRAM katakchalari bitni qanday usulda saqlaydi?
6. Nega DRAM refresh talab qiladi?
7. $101101_2$ ni o'nlikka aylantirishda qaysi darajalar ishlatiladi?
8. O'nlik butun sonni istalgan asosga aylantirishda nega qoldiqlar teskari o'qiladi?
9. Nima uchun ikkilikdan sakkizlikka o'tishda uch bitdan, hexga o'tishda to'rt bitdan guruhlaymiz?
10. Nega $0.625_{10}$ ikkilikda tugaydi, $0.1_{10}$ esa tugamaydi?
11. Nega Python'da $0.1 + 0.2 == 0.3$ natijasi `False` bo'lishi mumkin?
12. Floating-point sonlarni taqqoslashda `math.isclose()` nima uchun foydali?

## O'qituvchi uchun qayd

- [ ] Sanoq sistemasiga ehtiyoj va pozitsion yozuv tushuntirildi.
- [ ] Kuchlanish, mantiqiy 0/1 va noise margin o'rtasidagi farq tushuntirildi.
- [ ] Tranzistor va bit tushunchalari yoritildi.
- [ ] SRAM va DRAM farqlari, refresh va volatile xotira tushuntirildi.
- [ ] Asosdan o'nlikka va o'nlikdan boshqa asosga o'tish misollari yechildi.
- [ ] Triada va tetrada jadvallari ishlatildi.
- [ ] Kasrlarni konvertatsiya qilish va davriy ikkilik kasr ko'rsatildi.
- [ ] Python floating-point misollari sinab ko'rildi.
- [ ] O'quvchilarning savollari va qiyinchiliklari qayd etildi.