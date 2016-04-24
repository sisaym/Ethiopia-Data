"""
Django settings for ethdata project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n9!b&2^fz4mc41m5wsgvv!kcuv1ca_hhv)@jnvd89v%raq1(fl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# change in production to ['*'] or specific host
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'tastypie',
    'utility',
    'data',
    'publications',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ethdata.urls'

WSGI_APPLICATION = 'ethdata.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'NAME': 'ethdata',
    #     'ENGINE': 'mysql.connector.django',
    #     'USER': 'root',
    #     'PASSWORD': 'root',
    #     'PORT': 3308,
    #     'OPTIONS': {
    #       'autocommit': True,
    #     },
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data.sqlite',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# absolute file path static files will be collected by collectstatic for deployment
STATIC_ROOT = "static_files"

# static file url used by django to display
STATIC_URL = '/static/'


MEDIA_URL = '/media/'
MEDIA_ROOT= (
    os.path.join(BASE_DIR, '/media/')
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# heroku related settings
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')