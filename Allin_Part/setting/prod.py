from decouple import config
import os
from pathlib import Path    
import dj_database_url
from dotenv import load_dotenv
from Allin_Part.settings import *
# Initialise environment variables

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY' ,default= 'django-insecure-*0%#&!+!+&@44%+646*=a+-^@*n7#694+55423@+*@#+-+*@')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)


ALLOWED_HOSTS = ["*"]


#Site ID
SITE_ID = config('SITE_ID', cast=int, default=1)


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }


# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': config('NAME', default='postgre'),
#        'USER': config('USER', default='postgre'),
#        'PASSWORD': config('PASSWORD', default='postgre'),
#        'HOST': config('HOST', default='postgre'),
#        'PORT': config('PORT', default='5432'),
#    }
# }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

STATIC_ROOT = BASE_DIR / 'staticfiles/'
MEDIA_ROOT = BASE_DIR / 'media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

GUNICORN_TIMEOUT=60

#http settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

#HSTS settings
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

#more Security settings
