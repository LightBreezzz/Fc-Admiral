#!/bin/bash

DOMAIN="${DOMAIN:-your-domain.com}"
EMAIL="${EMAIL:-your-email@example.com}"

if ! command -v certbot &> /dev/null; then
    echo "Certbot не установлен. Установите его с помощью:"
    echo "sudo apt update && sudo apt install certbot"
    exit 1
fi

echo "Установите DNS-плагин для вашего провайдера. Пример для Cloudflare:"
echo "sudo apt install python3-certbot-dns-cloudflare"
echo "Для других провайдеров посетите: https://certbot.eff.org/docs/using.html#dns-plugins"
echo ""
echo "Для использования DNS-валидации:"
echo "1. Установите соответствующий DNS-плагин для вашего провайдера"
echo "2. Создайте файл с вашими учетными данными DNS"
echo "3. Запустите certbot с параметрами для вашего DNS-провайдера"
echo ""
echo "Пример для Cloudflare (требуется установка python3-certbot-dns-cloudflare):"
echo "certbot certonly --dns-cloudflare --dns-cloudflare-credentials /path/to/credentials.ini -d $DOMAIN -d www.$DOMAIN --email $EMAIL --agree-tos --no-eff-email"
echo ""
echo "Альтернативно, вы можете использовать standalone-метод (требует открытые порты 80 и/или 443):"
echo "sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 --email $EMAIL --agree-tos --no-eff-email -d $DOMAIN -d www.$DOMAIN"
echo ""
echo "Или webroot-метод (требует запущенный веб-сервер):"
echo "sudo certbot certonly --webroot --webroot-path /var/www/certbot --email $EMAIL --agree-tos --no-eff-email -d $DOMAIN -d www.$DOMAIN"
echo ""
echo "После получения сертификатов вручную скопируйте их в нужные директории для использования в Docker:"
echo "sudo cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem ./ssl_certs/"
echo "sudo cp /etc/letsencrypt/live/$DOMAIN/privkey.pem ./ssl_private/"
echo ""
echo "Убедитесь, что директории ssl_certs и ssl_private существуют:"
echo "mkdir -p ssl_certs ssl_private"