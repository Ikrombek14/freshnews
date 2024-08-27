from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# Bazaviy fayl yo'lini olish
BASE_DIR = Path(__file__).resolve().parent.parent

# Maxfiy kalit (Uni xavfsiz saqlash zarur)
SECRET_KEY = 'django-insecure-opz@qu0!$q1isl%otg!exxkcpf(x=m#id%3*7s%ijc-(*8c2up'

# Debug holati (Uni ishlab chiqarish uchun o'chiring)
DEBUG = True

# Ruxsat etilgan xostlar ro'yxati
ALLOWED_HOSTS = ['*']

# Ilovalar ro'yxati
INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cuser',
    'news',


    'whitenoise.runserver_nostatic',
]

# O'rta qatlamlar (Middlewares)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cuser.middleware.CuserMiddleware',
]

# Statik fayllar uchun saqlash usuli
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# URL konfiguratsiyasi
ROOT_URLCONF = 'config.urls'

# Django shablonlar konfiguratsiyasi
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath("templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news.context_processors.currency_rates',
            ],
        },
    },
]

# WSGI ilova uchun konfiguratsiya
WSGI_APPLICATION = 'config.wsgi.application'

# Ma'lumotlar bazasi konfiguratsiyasi
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Parolni tasdiqlash uchun sozlamalar
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

# Model translatsiya qilish uchun modullar
TRANSLATABLE_MODEL_MODULES = (
    'news.models',
)

# Til konfiguratsiyasi
LANGUAGE_CODE = 'uz'  # Default til
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Dastur til konfiguratsiyasi
LANGUAGES = [
    ('uz', _('Uzb')),
    ('en', _('Eng')),
    ('ru', _('Рус')),
]

# Standart model translatsiya tili
MODEL_TRANSLATION_DEFAULT_LANGUAGE = 'uz'

# Tarjima fayllari yo'llari
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Statik fayllar (CSS, JavaScript, Rasm)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# Media fayllar uchun konfiguratsiya
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

# Default asosiy kalit turi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
