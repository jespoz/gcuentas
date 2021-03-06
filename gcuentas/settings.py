"""
Django settings for gcuentas project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jm-hv!q5ay6#9k2$@a7_%-7q#f143uw*h0e@guunimu3n23f=o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'text',
    'atributes',
    'vending',
    'other',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gcuentas.urls'

WSGI_APPLICATION = 'gcuentas.wsgi.application'

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as tcp

TEMPLATE_CONTEXT_PROCESSORS = tcp + (
    'principal.context_processors.menu',
)

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'dlegacy',
        'USER': 'gcuentas',
        'PASSWORD': 'paso',
        'HOST': '192.168.9.80',
        'PORT': '1532',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'es-CL'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static-only')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'static', 'templates'),
    os.path.join(BASE_DIR, 'principal', 'templates'),
    os.path.join(BASE_DIR, 'other', 'templates'),
)
