LANGUAGE_CODE = 'en'
SECRET_KEY = 'ji2r2iGkZqJVbWDhXrgDKDR2qG#mmtvBZXPXDugA4H)KFLwLHy'
SITE_ID = 1

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nologcapture', '--with-id']

MEDIA_ROOT = '/tmp/cmsplugin-iframe/media/'
STATIC_ROOT = '/tmp/cmsplugin-iframe/static/'
ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sites',
    'django_nose',
    'cms',
    'menus',
    'mptt',
    'cmsplugin_iframe',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
]
