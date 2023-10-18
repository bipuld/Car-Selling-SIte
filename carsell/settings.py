from pathlib import Path,os
from django.contrib.messages import constants as messages
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=True, cast=bool)
LOGIN_REDIRECT_URL = 'dashboard'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'cars.apps.CarsConfig',
    'pages.apps.PagesConfig',
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'django.contrib.humanize',
    'social_django',
    'Inquiry'
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

ROOT_URLCONF = 'carsell.urls'

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

WSGI_APPLICATION = 'carsell.wsgi.application'

# for the socail login
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2', #for facebook
    'django.contrib.auth.backends.ModelBackend',  # or other backends you use
)

SOCIAL_AUTH_FACEBOOK_KEY = '297042666599188'
SOCIAL_AUTH_FACEBOOK_SECRET = 'bbfe4b2eebb145f7fcb674e52e5696c5'


SOCIAL_AUTH_JSONFIELD_ENABLED = True
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST':'localhost',
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'carsell/static/')
]




MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MESSAGE_TAGS = {
    messages.INFO: "",
    50: "critical",
}




# # Email configuration for Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP as the email backend
EMAIL_HOST = 'smtp.gmail.com'  # SMTP server for Gmail
EMAIL_PORT = 587  # Port for TLS (secure) connection
EMAIL_HOST_USER =  config('EMAIL_ID')  # Your Gmail email address
EMAIL_HOST_PASSWORD =  config('EMAIL_PASSWORD') # Your Gmail password or an "App Password" if you have 2-factor authentication enabled
EMAIL_USE_TLS = True  # Use TLS (secure connection)
EMAIL_USE_SSL = False  # Do not use SSL (False for TLS)
