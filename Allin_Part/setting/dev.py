from Allin_Part.settings import *
from decouple import config
# Initialise environment variables


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []


#Site ID
SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "Statics",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media/'

CSRF_COOKIE_SECURE = False