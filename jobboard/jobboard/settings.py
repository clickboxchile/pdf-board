
"""
Django settings for jobboard project.

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
SECRET_KEY = 'fqls(kr4gs+w#3uu3+)2b87vf0-^dd@^#2u!(^rw%ma1u+)!o@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'empleos',
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

ROOT_URLCONF = 'jobboard.urls'

WSGI_APPLICATION = 'jobboard.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'pdf_board.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

USE_I18N = True

LANGUAGE_CODE = 'es-py'

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'America/Asuncion'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"), )

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# SMTP Settings
EMAIL_BACKEND = 'util.email.SSLEmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.server.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@domain.com'
EMAIL_HOST_PASSWORD = 'smtp_server_password'
EMAIL_ADMINISTATOR = 'admin@domain.com'

DOMAIN_NAME = 'domain.com'

# """
# Django settings for jobboard project.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.7/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.7/ref/settings/
# """

# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'fqls(kr4gs+w#3uu3+)2b87vf0-^dd@^#2u!(^rw%ma1u+)!o@'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# TEMPLATE_DEBUG = True

# ALLOWED_HOSTS = []

# # Application definition

# INSTALLED_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'empleos',
# )

# MIDDLEWARE_CLASSES = (
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# )

# ROOT_URLCONF = 'jobboard.urls'

# WSGI_APPLICATION = 'jobboard.wsgi.application'

# # Database
# # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'pdf_board.db',
#         # 'USER': 'jobboard_login',
#         # 'PASSWORD': 'your_password',
#         # 'HOST': '127.0.0.1',
#         # 'PORT': '5432',
#     }
# }

# # Internationalization
# # https://docs.djangoproject.com/en/1.7/topics/i18n/

# USE_I18N = True

# LANGUAGE_CODE = 'es'

# USE_L10N = True

# USE_TZ = True

# TIME_ZONE = 'America/Santiago'

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"), )

# TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# # SMTP Settings
# EMAIL_BACKEND = 'util.email.SSLEmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.server.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'noreply@domain.com'
# EMAIL_HOST_PASSWORD = 'smtp_server_password'
# EMAIL_ADMINISTATOR = 'admin@domain.com'

# DOMAIN_NAME = 'domain.com'