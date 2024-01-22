from Allin_Part.settings import *
from decouple import config
import os
import dj_database_url
# Initialise environment variables


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


#Site ID
SITE_ID = config('SITE_ID', cast=int, default=1)


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
'''
# DATABASES = {
#     'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
#     }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': config('NAME', default='postgre'),
       'USER': config('USER', default='postgre'),
       'PASSWORD': config('PASSWORD', default='postgre'),
       'HOST': config('HOST', default='postgre'),
       'PORT': config('PORT', default='5432'),
   }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = 'media/'
MEDIA_ROOT = 'media/'

CSRF_COOKIE_SECURE = False