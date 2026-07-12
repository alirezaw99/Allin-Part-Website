# Python 3.11 — matches Django 5.2 stack used for this project.
FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=300

WORKDIR /app

# If apt hits deb.debian.org timeouts in your region, uncomment the block below and remove
# the standalone `RUN apt-get update` pair (merge into one RUN after writing sources.list).
#
RUN rm -f /etc/apt/sources.list /etc/apt/sources.list.d/debian.sources \
    && cat <<'EOF' > /etc/apt/sources.list
deb http://linux-mirror.liara.ir/repository/debian/ bookworm main contrib non-free non-free-firmware
deb http://linux-mirror.liara.ir/repository/debian-security/ bookworm-security main contrib non-free non-free-firmware
deb http://linux-mirror.liara.ir/repository/debian/ bookworm-updates main contrib non-free non-free-firmware
deb http://linux-mirror.liara.ir/repository/debian/ bookworm-backports main contrib non-free non-free-firmware
EOF

RUN apt-get update -o Acquire::Retries=5 \
    && apt-get install -y --no-install-recommends libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --retries 10 --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p media staticfiles \
    && chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 --workers ${GUNICORN_WORKERS:-3} --timeout ${GUNICORN_TIMEOUT:-60} Allin_Part.wsgi:application"]
