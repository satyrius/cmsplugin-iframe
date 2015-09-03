# This settings module is for Django 1.7 or higher
from settings import *  # NOQA

# To stop django warn about MIDDLEWARE_CLASSES changed
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware'
)

# Native django migrations was placed in migrations_django folder before
# cms 3.1 release, so we have to hack this in runtime
if is_30:
    MIGRATION_MODULES = {
        'cms': 'cms.migrations_django',
    }
