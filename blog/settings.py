import environ
import os
from pathlib import Path
import django_heroku


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')  # env

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # env

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'rest_framework',
    'corsheaders',
    'post',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

]

ROOT_URLCONF = 'blog.urls'

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

WSGI_APPLICATION = 'blog.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'sujal',
#         'USER': 'postgres',
#         'PASSWORD': 'sujal1012',
#         'HOST': '12.0.0.1',
#         'PORT': '5432',
#     }
# }
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'https://gutsnbraces.herokuapp.com',
    'https://gutsnbraces.firebaseapp.com',
    'https://gutsnbraces.web.app',
    'http://gutsnbraces.com',
    'https://gutsnbraces.com',
    'https://coroprate-site-1012.web.app'
]
CORS_ALLOW_CREDENTIALS = True

# DATABASES['default'] = dj_database_url.config(
#     conn_max_age=600, ssl_require=True)

django_heroku.settings(locals())


# S3 BUCKET CONFIG

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')  # env
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')  # env
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')  # env

AWS_S3_FILE_OVERWRITE = False  # env
AWS_DEFAULT_ACL = None  # env
DEFAULT_FILE_STORAGE = env('DEFAULT_FILE_STORAGE')  # env
STATICFILES_STORAGE = env('STATICFILES_STORAGE')  # env
AWS_S3_HOST = env('AWS_S3_HOST')  # env
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')  # change to your region   #env
AWS_S3_SIGNATURE_VERSION = env('AWS_S3_SIGNATURE_VERSION')  # env
AWS_S3_ADDRESSING_STYLE = 'virtual'


TINYMCE_DEFAULT_CONFIG = {
    "height": "320px",
    "width": "960px",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    # To force a specific language instead of the Django current language.
    "language": "en_US",
}
