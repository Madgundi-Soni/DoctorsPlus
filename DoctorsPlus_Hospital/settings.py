"""
Django settings for DoctorsPlus_Hospital project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path,os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(j6-6g!n*_qcp@uhz#o^$y!2@bke_o7=pk0f(_ar(pfr9a=1n7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'doctors',
    'patients',
    'user_details',
    # 'rest_framework',
]

AUTH_USER_MODEL = 'user_details.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DoctorsPlus_Hospital.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
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




WSGI_APPLICATION = 'DoctorsPlus_Hospital.wsgi.application'


# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         # 'rest_framework.permissions.DjangoModelPermissions',
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'

#         # 'rest_framework.renderers.<corresponding_renderer>'

#     ]
# }

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
         'ENGINE': 'django.db.backends.sqlite3',
        
        'NAME': BASE_DIR / 'db.sqlite3',
        # 'NAME': 'doctorsplus_hospital',
        # 'HOST':'127.0.0.1',
        # 'POST':'3306',
        # 'USER':'root',
        # 'PASSWORD':'root',

    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', 
#         'NAME': 'Sonaa$d_database',
#         'USER': 'Sonaa',
#         'PASSWORD': 'Data1234',
#         'HOST': 'Sonaa.mysql.pythonanywhere-services.com',   # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


OAUTH2_PROVIDER = {
    'SCOPES': {'calendar': 'Read/write access to Calendar'},
    'CLIENT_ID': '650284881740-ogi5cv7h4n7qk5utoorkoq2mbmho4kh4.apps.googleusercontent.com',
    'CLIENT_SECRET': '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',
}

GOOGLE_TOKEN_FILE = 'token.json'



# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# STATIC_URL = 'static/'

# STATICFILES_DIRS = [
#     BASE_DIR, "static/",
    
# ]


# # Base url to serve media files
# MEDIA_URL = '/media/'

# # Path where media is stored
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # For Deployment

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TIME_ZONE =  'Asia/Kolkata'