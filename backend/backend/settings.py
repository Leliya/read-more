from pathlib import Path

from decouple import Csv, config
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config(
    'SECRET_KEY',
    default='django-insecure-9okt4wf=#ft-+*81!q9mn2^=je&^*03&ea8&#j(6(2^-xlj##o'
)

DEBUG = config('DEBUG', cast=bool, default=True)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    cast=Csv(),
    default='127.0.0.1'
)

MODE = config('MODE', cast=str, default='dev')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',

    'core',
    'users',

    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'

if MODE == 'dev':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': config('DB_ENGINE'),
            'NAME': config('DB_NAME'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT')
        }
    }

AUTH_USER_MODEL = 'users.User'

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Samara'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True

CORS_URLS_REGEX = r'^/api/.*$'

DJOSER = {
    'LOGIN_FIELD': 'email',
    'HIDE_USER': 'False',
    'SERIALIZERS': {
        'current_user': 'users.serializers.UsersSerializer',
    },
    'PERMISSIONS': {
        'user': ['djoser.permissions.CurrentUserOrAdminOrReadOnly'],
    },
}