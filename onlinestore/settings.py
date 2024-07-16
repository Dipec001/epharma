"""
Django settings for onlinestore project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

print(DEBUG)

ALLOWED_HOSTS = ['epharma-91ebb7c041f9.herokuapp.com','127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "myapp",
    'taggit',
    'modeltranslation',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    #Language Change Middleware
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "onlinestore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # custom
                'myapp.context_processors.cart_item_count',
                'myapp.context_processors.country_list',
                
            ],
        },
    },
]

WSGI_APPLICATION = "onlinestore.wsgi.application"


# Database\
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


# if DEBUG:
#     DATABASES = {
#     "default": {
#         "ENGINE": os.getenv("DB_ENGINE"),
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER"),
#         "PASSWORD": os.getenv("DB_PASSWORD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": os.getenv("DB_PORT"),
#         "CONN_MAX_AGE": 300,  # Maximum connection age in seconds (e.g., 5 minutes)
#         'CONN_MAX_NUM': 20,   # Maximum number of connections in the pool
#     }
# } 
# else:
#     DATABASES = {
#     'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
# }

# #Database configuration
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

#DYnamic url
if DEBUG:
    DOMAIN = 'http://localhost:8000'
else:
    DOMAIN = 'https://epharma-91ebb7c041f9.herokuapp.com'


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

from django.utils.translation import gettext_lazy as _

LANGUAGES = [
    ('en-us', _('English (USA)')),
    ('zh-hans', _('Chinese')),
    ('pt', _('Portuguese')),
    ('de', _('German')),
    ('de-ch', _('Swiss German')),  # Correct format for Swiss German
    ('en-uk', _('English (UK)')),
    ('en-ca', _('English (Canada)')),
    ('en-au', _('English (Australia)')),
    ('en-sg', _('English (Singapore)')),
    ('fr', _('French')),
    ('sv', _('Swedish')),
    ('es', _('Spanish')),
    ('nl', _('Dutch (Netherlands)')),
    ('nl-be', _('Flemish (Belgium)')),  # Correct format for Flemish
    ('it', _('Italian')),
    ('ru', _('Russian')),
    ('ar', _('Arabic (UAE)')),
    ('ja', _('Japanese')),
]

# modeltranslation settings
# MODELTRANSLATION_LANGUAGES = ('en-us', 'zh-Hans', 'pt', 'de', 'de-CH', 'en-uk', 'en-ca', 'en-au', 'en-sg', 'fr', 'sv', 'es', 'nl', 'nl-BE', 'it', 'ru', 'ar', 'ja')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en-us'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en-us'




LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Specify the locale path
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_URL = "static/"

# Add this setting
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Update this path to a directory that exists in your project
# These are directories where Django will search for additional static files (development)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#Media settings
# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

#Celery Settings
if DEBUG:
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
else:
    # Use REDIS_URL environment variable provided by your hosting service
    CELERY_BROKER_URL = os.getenv('REDIS_URL')
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'  # Use UTC for global consistency


from celery.schedules import crontab
from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    'update-currency-rates-daily': {
        'task': 'myapp.tasks.update_currency_rates',
        # 'schedule': crontab(hour=0, minute=0),  # Runs every day at midnight UTC
        'schedule': timedelta(minutes=2), 
    },
}



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')

# Static files (CSS, JavaScript, etc.)
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# Media files (uploaded user content)
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


AUTH_USER_MODEL = "myapp.User"

AUTHENTICATION_BACKENDS = [
    'myapp.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Optional settings for Django Allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
