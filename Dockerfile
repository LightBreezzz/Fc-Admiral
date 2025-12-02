FROM python:3.12-slim-bookworm

RUN echo "precedence ::ffff:0:0/96 100" >> /etc/gai.conf

RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    ca-certificates \
    dnsutils \
    iputils-ping && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    pip --default-timeout=120 install --no-cache-dir --upgrade pip setuptools wheel build

WORKDIR /app

COPY pyproject.toml .
RUN python3 -m build
RUN pip install --no-cache-dir dist/*.whl gunicorn psycopg[binary]

COPY . .

RUN mkdir -p /app/staticfiles /app/media && \
    chown -R www-data:www-data /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER www-data

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]
