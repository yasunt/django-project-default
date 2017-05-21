from .base import *


SECURE_SSL_HOSTS = True

DEBUG = False

ALLOWED_HOSTS = ['www.some.domain.com']

# security settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
