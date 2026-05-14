# Personal Portfolio — skylargutman.com

A full-stack portfolio site built with Django, deployed on Oracle Cloud Ampere A1 (free tier), served via Gunicorn + Nginx, with Cloudflare handling DNS and SSL.

## Stack

- **Backend**: Django 5.2, Python 3.10
- **Server**: Gunicorn (systemd service) + Nginx reverse proxy
- **Infrastructure**: Oracle Cloud Ampere A1 (ARM, Ubuntu 22.04 LTS)
- **DNS/SSL**: Cloudflare (proxied, flexible SSL)
- **Frontend**: Tailwind CSS (CDN)
- **Database**: SQLite

## Architecture

Browser → Cloudflare (SSL/CDN) → Oracle Cloud VM → Nginx → Gunicorn (Unix socket) → Django

## Features

- Project portfolio with Django admin content management
- Dynamic project pages with tech stack tags, images, and video embeds
- Responsive dark theme UI
- Static file serving via Nginx
- Environment-based configuration via python-dotenv

## Local Development

```bash
git clone git@github.com:skylargutman/personal-portfolio.git
cd personal-portfolio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your SECRET_KEY
python manage.py migrate
python manage.py runserver
```

## Deployment Notes

- OCI Security List must allow ingress on ports 80/443 with source port range set to **All**
- iptables ACCEPT rules must appear before the default REJECT rule
- Nginx uses `alias` (not `root`) for static file serving
- `chmod 755 /home/skylar` required for www-data to traverse to the socket

## Author

Skylar Gutman — [skylargutman.com](https://skylargutman.com)
