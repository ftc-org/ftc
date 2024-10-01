"""
Django settings for ftc project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import io
from pathlib import Path
import os
import environ
from google.cloud import secretmanager
from google.oauth2 import service_account

def str_to_bool(value):
    return value.lower() in ('true', 'yes', 'on', '1')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
env_file = os.path.join(BASE_DIR, '.env')

if os.path.isfile(env_file):
    # read a local .env file
    env.read_env(env_file)
    # load_dotenv()
elif os.environ.get('GOOGLE_CLOUD_PROJECT', None):
    # pull .env file from Secret Manager
    project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')
    client = secretmanager.SecretManagerServiceClient()
    settings_name = os.environ.get('SETTINGS_NAME', 'django_settings')
    name = f'projects/{project_id}/secrets/{settings_name}/versions/latest'
    payload = client.access_secret_version(
        name=name).payload.data.decode('UTF-8')

    env.read_env(io.StringIO(payload))
else:
    raise Exception(
        'No local .env or GOOGLE_CLOUD_PROJECT detected. No secrets found.')

# SECRET_KEY = "django-insecure-0%=ni=ch)5x04=-3j^e%=*k*z6hrzkbuhw9v43z4s7*oksl!5%"
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(',')


CORS_ALLOW_ALL_ORIGINS = str_to_bool(os.environ.get('CORS_ALLOW_ALL_ORIGINS', 'False'))
CORS_ORIGINS_WHITELIST = os.environ.get("CORS_ORIGINS_WHITELIST").split(',')

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(',')
CSRF_ALLOWED_ORIGINS = os.environ.get("CSRF_ALLOWED_ORIGINS").split(',')
CSRF_COOKIE_SECURE = str_to_bool(os.environ.get('CSRF_COOKIE_SECURE', 'False'))  # Set to False if you're not using HTTPS
CSRF_COOKIE_HTTPONLY = str_to_bool(os.environ.get('CSRF_COOKIE_HTTPONLY', 'False'))

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "update.apps.UpdateConfig",
    "api.apps.ApiConfig",
    "rest_framework",
    "django_filters",
    "corsheaders",
    'storages',
]

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ftc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "ftc/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ftc.wsgi.application"

DATABASES = {"default": env.db()}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     os.path.join(BASE_DIR, 'gcpCredentials.json')
# )

GS_BUCKET_NAME = env('GS_BUCKET_NAME')
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": GS_BUCKET_NAME
        }
    },
}
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "uploads"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


