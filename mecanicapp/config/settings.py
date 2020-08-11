"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cu-x@g)yw(2q18w6prl7tp@9lqa_wb%-y8_x!5%#u#+*8_ry40'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '*',
    '192.168.0.18',
    '192.168.0.19',
    '192.168.0.49',
    '192.168.0.17',
    '127.0.0.1',
    'mecanicapplication.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [    
    'aplicaciones.login',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Mis apps
    'aplicaciones.gestion',    
    'aplicaciones.homepage',
    #Mis librerias
    'django_userforeignkey',    
    'django_cleanup.apps.CleanupConfig',#Permite borrar imágenes subidas
    'import_export',#Permite importar y exportar archivos a la base de datos desde el administrador
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_userforeignkey.middleware.UserForeignKeyMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True, #Para buscar templates en las apps
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

WSGI_APPLICATION = 'config.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2seutse6rncl7',
        'USER':'uvllmrzpzxizlj',
        'PASSWORD':'e79d2108a2b48cfbdb830cd399ebe22506c96128503bfc4ab5f6b1f28021743a',
        'HOST':'ec2-52-200-48-116.compute-1.amazonaws.com',
        'PORT':5432,
    }
}
"""

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}  """


import dj_database_url
from decouple import config
DATABASES = {
    'default':dj_database_url.config(
        default = config('DATABASE_URL')
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #de codigofacilito no da problemas

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/app/dashboard/'

LOGOUT_REDIRECT_URL = '/cuentas/login/'

LOGIN_URL = '/cuentas/login/'#Reemplaza al accounts/login/


#Email
if DEBUG:
    #Aquí hay que configurar un email real para producción en este caso funciona con Gmail
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "aquítucorreo"
    EMAIL_HOST_PASSWORD = "aquítuclave"    
else:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend' #Esto es un backend para los emails basado en ficheros
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'#de codigofacilito toca ponerlo simpre al final