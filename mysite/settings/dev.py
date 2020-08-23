from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b8sywq9!zqh0h0=_uqwat#dvajl+41lx!5q#tjxchv5v-%zd%c'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions',
    'wagtail.contrib.styleguide',
]


MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


CACHES = {
     "default": {
         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
         "LOCATION": "/home/rudi/cms/mysite/cache"
     }
 }

try:
    from .local import *
except ImportError:
    pass