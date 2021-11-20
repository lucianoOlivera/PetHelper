"""
Django settings for petHelper project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4o7-)zx=7z(ztyi6iitii7o7bybyv8dbmjxs@7gf48qycyt(ng'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'verify_email.apps.VerifyEmailConfig',
    'django_filters',
    'easy_pdf',
    'bases',
    'usuario',
    'donacionV2',
    'insumo',
    'solicitud',
    'organizaciones',
    'mapa',
    'reportes',
    'widget_tweaks',
    'smart_selects',
    'social_django',
    'geocoder',
    'captcha',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'mercadopago'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'petHelper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'petHelper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-Ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

LOGIN_URL = 'bases:login'

LOGIN_REDIRECT_URL = 'bases:home'

LOGOUT_REDIRECT_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

AUTH_USER_MODEL = "usuario.Usuario"

LOGOUT_URL = 'logout'

SOCIAL_AUTH_FACEBOOK_KEY = '603112644018191'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '59bff6660482a1f84b71bcdb051d1606'  # App Secret
SOCIAL_AUTH_URL_NAMESPACE = 'bases:social'
CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME  = "http://"
SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 32312312312312
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_PRELOAD = True
SECURE_FRAME_DENY = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'pethelper70@gmail.com'
EMAIL_HOST_PASSWORD = 'proyecto2021'

DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'
SUBJECT = 'Confirmación de email'
HTML_MESSAGE_TEMPLATE = 'bases/verificacion_email.html'
VERIFICATION_SUCCESS_TEMPLATE = 'bases/verificacion_exito.html'
VERIFICATION_FAILED_TEMPLATE = 'bases/verificacion_error.html'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
EASY_MAPS_GOOGLE_KEY = 'AIzaSyADpYBTwpzczBSJa28xgSILCfNwLBkHfRk'

RECAPTCHA_PUBLIC_KEY = '6LcejBUdAAAAAIVU8UZFxGChhOOdn4Wu7niMhi9Z'
RECAPTCHA_PRIVATE_KEY = '6LcejBUdAAAAAPEieTcmoWLvFK9wv7A66i-xd_xj'
RECAPTCHA_REQUIRED_SCORE = 0.85

PUBLIC_KEY = 'TEST-e67cc838-dc71-4d4d-a6e9-8b33375a378f'