import os

import dj_database_url
from decouple import Csv, config
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

from Allin_Part.settings import *  # noqa: F403

load_dotenv()

SECRET_KEY = config("SECRET_KEY", default="")
if not SECRET_KEY:
    raise ImproperlyConfigured("Set SECRET_KEY in the environment for production.")

DEBUG = config("DEBUG", cast=bool, default=False)

_allowed = config(
    "ALLOWED_HOSTS", default="localhost,127.0.0.1", cast=Csv()
)
ALLOWED_HOSTS = _allowed if _allowed else ["localhost"]

SITE_ID = config("SITE_ID", cast=int, default=1)

database_url = os.environ.get("DATABASE_URL") or config("DATABASE_URL", default="")
if not database_url:
    raise ImproperlyConfigured(
        "Set DATABASE_URL (or pass it in the OS environment)."
    )

DATABASES = {
    "default": dj_database_url.parse(
        database_url,
        conn_max_age=config("DB_CONN_MAX_AGE", cast=int, default=600),
        ssl_require=config("DATABASE_SSL_REQUIRE", cast=bool, default=False),
    )
}


STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / "staticfiles/"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool, default=True)
SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", cast=bool, default=True)
CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", cast=bool, default=True)

if config("BEHIND_REVERSE_PROXY", cast=bool, default=False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    USE_X_FORWARDED_HOST = True

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS", default="", cast=Csv()
)

if SECURE_SSL_REDIRECT:
    SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", cast=int, default=31536000)
    SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", cast=bool, default=True)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = config(
        "SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool, default=True
    )
else:
    SECURE_HSTS_SECONDS = 0
    SECURE_HSTS_PRELOAD = False
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
