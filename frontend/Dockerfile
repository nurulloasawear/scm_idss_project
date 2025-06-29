# ==============================================================================
#                 FRONTEND UCHUN DOCKERFILE
# ==============================================================================
# Bu Dockerfile Nginx web-serveridan foydalanib, sizning HTML, CSS, JS
# fayllaringizni foydalanuvchiga taqdim etish (serve) uchun mo'ljallangan.

# 1-BOSQICH: Asosiy obrazni tanlash
FROM nginx:alpine

# 2-BOSQICH: Fayllarni nusxalash
# Joriy papkadagi (frontend) barcha fayllarni konteynerning
# web-server uchun mo'ljallangan /usr/share/nginx/html papkasiga nusxalash.
COPY . /usr/share/nginx/html

# 3-BOSQICH: Portni ochish
EXPOSE 80

# Web-serverni ishga tushirish uchun standart buyruq.
CMD ["nginx", "-g", "daemon off;"]
