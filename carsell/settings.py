from pathlib import Path,os
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-3@w6l=22xu_wgr_yf66_96y5c%*g!_zsu-(jkz_-7u7c!0+i@*'

DEBUG = True
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
# # SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your_client_id'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your_client_secret'
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your_client_id'
# for google login and signin

SOCIAL_AUTH_JSONFIELD_ENABLED = True
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carsell_db',
        'USER':'postgres',
        'PASSWORD':'12345',
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
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Use SMTP as the email backend
# EMAIL_HOST = 'smtp.gmail.com'  # SMTP server for Gmail
# EMAIL_PORT = 587  # Port for TLS (secure) connection
# EMAIL_HOST_USER = 'bida_csit2077@lict.edu.np'  # Your Gmail email address
# EMAIL_HOST_PASSWORD =  '' # Your Gmail password or an "App Password" if you have 2-factor authentication enabled
# EMAIL_USE_TLS = True  # Use TLS (secure connection)
# EMAIL_USE_SSL = False  # Do not use SSL (False for TLS)

# # Additional email settings (optional)
# DEFAULT_FROM_EMAIL = 'dawadirishab@gmail,com'  # Default "from" address for emails
# EMAIL_SUBJECT_PREFIX = '[Car Zone] '  # Prefix for email subjects
