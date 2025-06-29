SCM-IDSS Loyihasi uchun Texnik Hujjat
Versiya: 1.0
Sana: 29-iyun, 2025-yil

1. Loyiha haqida
SCM-IDSS (Supply Chain Management - Intelligent Decision Support System) — bu ta'minot zanjirini boshqarish jarayonlarini avtomatlashtirish va optimallashtirish uchun mo'ljallangan kompleks dasturiy ta'minot. Tizim mikroservislar arxitekturasi asosida qurilgan bo'lib, har bir qism mustaqil ravishda ishlash va rivojlanish imkoniyatiga ega.

Ushbu hujjat loyihaning texnik tuzilmasi, arxitekturasi, texnologiyalari va ishga tushirish jarayonlari haqida batafsil ma'lumot beradi.

2. Arxitektura va Dizayn
Loyiha uchun Mikroservislar Arxitekturasi tanlangan. Bu yondashuv tizimni kichik, mustaqil va ixtisoslashgan servislarga ajratish imkonini beradi. Bu esa loyihani boshqarish, yangilash va kengaytirishni ancha osonlashtiradi.

Servislar va ularning vazifalari:
Frontend (Foydalanuvchi Interfeysi):

Nginx web-serverida ishlaydigan, foydalanuvchi bilan muloqot qiladigan qism.

Bootstrap 5 va JavaScript yordamida qurilgan. Barcha HTML sahifalar shu yerda joylashgan.

src (Asosiy Servis):

Loyihaning markaziy, umumiy funksiyalari uchun javobgar.

App'lar: core (AuditLog), notifications (Xabarnomalar), reports (Hisobotlar).

Celery Worker: Fondagi vazifalarni (masalan, hisobot generatsiyasi) bajaradi.

user_service (Foydalanuvchilar Servisi):

Tizimdagi "Pasport Stoli".

Vazifasi: Ro'yxatdan o'tkazish, tizimga kiritish (login) va JWT tokenlarini yaratish.

inventory_service (Inventar Servisi):

Mahsulotlar katalogi, omborlar va ulardagi qoldiqlar uchun javobgar.

RabbitMQ Iste'molchisi: Boshqa servislardan kelgan xabarlar asosida ombordagi miqdorni o'zgartiradi.

order_service (Buyurtmalar Servisi):

Tizimning "Orkestr Dirijyori".

Vazifasi: Buyurtmalarni yaratish va boshqarish jarayonini nazorat qiladi. Boshqa servislarga HTTP so'rovlari va RabbitMQ xabarlarini yuboradi.

logistics_service (Logistika Servisi):

Jo'natmalar va tashuvchi kompaniyalarni boshqarish uchun javobgar.

RabbitMQ Iste'molchisi: order_servicedan kelgan xabarlar asosida avtomatik ravishda yangi jo'natma (Shipment) yaratadi.

Servislararo Aloqa:
Sinxron Aloqa (HTTP): Bir servis boshqasidan darhol javob olishi kerak bo'lganda (masalan, order_servicening inventory_servicedan mahsulot narxini so'rashi) requests kutubxonasi orqali to'g'ridan-to'g'ri API so'rovlari yuboriladi.

Asinxron Aloqa (RabbitMQ): Bir servisda sodir bo'lgan voqea haqida boshqa servislarni xabardor qilish, lekin ularning javobini kutmaslik uchun ishlatiladi (masalan, order_service yangi buyurtma yaratganda logistics_servicega xabar yuborishi).

3. Texnologiyalar To'plami (Stack)
Backend: Python 3.9+, Django 5.x, Django REST Framework

Frontend: HTML5, Bootstrap 5, JavaScript (ES6+)

Ma'lumotlar Bazasi: PostgreSQL 13 (mustaqil konteynerda)

Xabarlar Brokeri: RabbitMQ (Asinxron aloqa uchun)

Caching / In-Memory: Redis (Celery uchun natijalarni saqlash)

Fondagi Vazifalar: Celery

Konteynerizatsiya: Docker & Docker Compose

4. Ishga Tushirish va Sozlash
Talablar:
Docker

Docker Compose

Sozlash:
Loyiha papkasidagi .env faylini oching.

SECRET_KEY uchun tasodifiy satr generatsiya qilib, uni o'zgartiring.

Qolgan barcha sozlamalar (RABBITMQ_..., POSTGRES_...) standart holatda ishlashga tayyor.

Ishga Tushirish:
Loyihaning asosiy papkasida terminalni oching.

Quyidagi buyruqni bajaring:

docker-compose up --build

Bu buyruq barcha kerakli obrazlarni (images) quradi va barcha servislarni (frontend, backend, baza, RabbitMQ, Redis) ishga tushiradi.

Frontend: http://localhost:8000/login.html manzilida ochiladi.

Backend Servislar: 9090, 9001, 8080, 9002 portlarida ishlaydi.

RabbitMQ Management: http://localhost:15672/ manzilida ochiladi (login: guest, parol: guest).

5. API Endpoint'lari
Har bir servis o'zining API endpoint'lariga ega. Ularga kirish uchun Bearer token orqali autentifikatsiya talab etiladi. Token user_servicening /api/auth/login/ manzilidan olinadi.

(Bu yerda har bir servisning asosiy endpoint'lari (masalan, inventory_service uchun /api/admin/products/) ro'yxati keltirilishi mumkin).

6. Kelajakdagi Rivojlanish va Yaxshilanishlar
Ushbu loyiha keyingi darajaga o'tish uchun mustahkam poydevor hisoblanadi. Kelajakda quyidagi yo'nalishlarda rivojlantirish mumkin:

Avtomatik Testlash: pytest va Django'ning TestCase yordamida unit va integration testlar yozish.

CI/CD: GitHub Actions yordamida avtomatik testlash va deployment jarayonlarini yo'lga qo'yish.

Kod Sifati: black va flake8 kabi vositalarni integratsiya qilish.

Monitoring va Loglash: Servislarning holatini kuzatish uchun Prometheus, Grafana va loglarni yig'ish uchun ELK Stack kabi vositalarni qo'shish.