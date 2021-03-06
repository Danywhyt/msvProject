"""
Django settings for proMSV project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from apps.helpDesk import *
from django.core.urlresolvers import reverse_lazy
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

###modificando la ruta por que esta en una parte mas adentro
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2o+6no*7*5@l%)rhni%ixbnawu-d_he*)uf&u6p=--0hn-4xri'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.helpDesk',
    'apps.usuario',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proMSV.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'proMSV.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True












# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATICFILES_DIRS = ('/home/msvcacom/ProyMSV/',)
# STATIC_ROOT = '/home/msvcacom/ProyMSV/static/'



'''
PROJECT_DIR = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(BASE_DIR,'staticfile2')
STATIC_URL = '/staticfile2/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(STATIC_ROOT, 'static'),
    )
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
ADMIN_MEDIA_PREFIX = '/staticfile2/admin/'


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT,)
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = os.path.join(os.path.join(PROJECT_ROOT, 'static'))

TEMPLATE_ROOT = '/home/msvcacom/ProyMsv/template/'
'''

LOGIN_REDIRECT_URL = reverse_lazy('helpDesk:trabajos')

LOGOUT_REDIRECT_URL = reverse_lazy ('helpDesk:msv')

STATIC_URL = '/ProyMSV/static_in_pro/static_root/'

STATIC_ROOT = os.path.join(BASE_DIR, "static_in_pro", "static_root")#'/home/msvcacom/ProyMSV/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    #'home/msvcacom/ProyMSV/static',
)