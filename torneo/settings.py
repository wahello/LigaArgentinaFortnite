"""
Django settings for torneo project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
from .validators import user_val

SEND_BROKEN_LINK_EMAILS=True

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't+xx-go%&%j(pii++m&973m76m%)21h2#j!91a@^0u)o0wgz%)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

ADMINS = [('Manu', 'mmquiroga10@gmail.com')]

ALLOWED_HOSTS = ['192.168.2.162', '127.0.0.1', 'quiroserver.ddns.net', 'ligafortnitearg.herokuapp.com', 'www.lafortnite.com']

ACCOUNT_SIGNUP_FORM_CLASS = 'sistema.forms.SignupForm'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'sistema',
    "django_rq"
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.twitch',
]

RQ_QUEUES = {
    'default': {
         'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'), # If you're on Heroku
         'DEFAULT_TIMEOUT': 3000,
     }
}

#DJANGO_SETTINGS_MODULE=settings rq worker high default low

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'torneo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# try:
#    from .local_settings import *
# except ImportError:
#     raise Exception("A local_settings.py file is required to run this project")


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ligafortnitearg@gmail.com'
EMAIL_HOST_PASSWORD = 'Newcode10'
EMAIL_PORT = 587
ACCOUNT_USERNAME_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE=True
ACCOUNT_EMAIL_VERIFICATION='mandatory'

WSGI_APPLICATION = 'torneo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_USERNAME_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATIC_URL = '/static/'
