# These are the minimum settings required to host the project

# fill in secret key
SECRET_KEY = ''

# fill in database details
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '', # leave blank to use default postgres port
    }
}

# False - production, True - development
DEBUG = False

# add hosting server ip address or domain
ALLOWED_HOSTS = []

# add website url prefix (remove if no prefix is used)
SITE_PREFIX = ''
FORCE_SCRIPT_NAME = SITE_PREFIX
STATIC_URL = SITE_PREFIX + '/static/'
