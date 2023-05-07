import os
from pathlib import Path as __Path

from django_yunohost_integration.base_settings import *  # noqa:F401,F403
from django_yunohost_integration.secret_key import get_or_create_secret as __get_or_create_secret

from django.template.defaultfilters import slugify
from django.conf.locale import LANG_INFO

from django_yunohost_integration.base_settings import LOGGING  # noqa:F401 isort:skip

# Add languages we're missing from Django
LANG_INFO.update({
    'am-et': {
        'bidi': False,
        'name': 'Amharic',
        'code': 'am-et',
        'name_local': 'አማርኛ'
    },
    'zh': {
        'bidi': False,
        'code': 'zh',
        'name': 'Chinese',
        'name_local': '简体中文',
    },
    'si': {
        'bidi': False,
        'code': 'si',
        'name': 'Sinhala',
        'name_local': 'සිංහල',
    },
    "ms": {
        "bidi": False,
        "code": "ms",
        "name": "Malay",
        "name_local": "Bahasa Melayu",
    },
})
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('am-et', 'Amharic'),
    ('ar', 'Arabic'),
    ('ast', 'Asturian'),
    ('bg', 'Bulgarian'),
    ('ca', 'Catalan'),
    ('cs-cz', 'Czech'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('en', 'English'),
    ('es', 'Spanish'),
    ('et', 'Estonian'),
    ('fa-ir', 'Persian (Iran)'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('gl', 'Galician'),
    ('he', 'Hebrew'),
    ('hr', 'Croatian'),
    ('hu', 'Hungarian'),
    ('id', 'Indonesian'),
    ('is', 'Icelandic'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('ko', 'Korean'),
    ('lt', 'Lithuanian'),
    ('ms', 'Malay'),
    ('nl', 'Dutch'),
    ('no', 'Norwegian'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('pt-br', 'Portuguese (Brazil)'),
    ('pt-pt', 'Portuguese (Portugal)'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('si-lk', 'Sinhala (Sri Lanka)'),
    ('sk-sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('sr', 'Serbian'),
    ('sv', 'Swedish'),
    ('th-th', 'Thai (Thailand)'),
    ('tr', 'Turkish'),
    ('uk-ua', 'Ukrainian'),
    ('vi', 'Vietnamese'),
    ('zh', 'Chinese'),
    ('zh-tw', 'Chinese (Taiwan)'),
)


FINALPATH = __Path('__FINALPATH__')  # /opt/yunohost/$app
assert FINALPATH.is_dir(), f'Directory not exists: {FINALPATH}'

PUBLIC_PATH = __Path('__PUBLIC_PATH__')  # /var/www/$app
assert PUBLIC_PATH.is_dir(), f'Directory not exists: {PUBLIC_PATH}'

LOG_FILE = __Path('__LOG_FILE__')  # /var/log/$app/django_example_ynh.log
assert LOG_FILE.is_file(), f'File not exists: {LOG_FILE}'

PATH_URL = '__PATH_URL__'  # $YNH_APP_ARG_PATH
PATH_URL = PATH_URL.strip('/')

YNH_CURRENT_HOST = '__YNH_CURRENT_HOST__'  # YunoHost main domain from: /etc/yunohost/current_host

# -----------------------------------------------------------------------------
# config_panel.toml settings:

DEBUG_ENABLED = True # '__DEBUG_ENABLED__'
DEBUG = True # bool(int(DEBUG_ENABLED))

LOG_LEVEL = '__LOG_LEVEL__'
ADMIN_EMAIL = '__ADMIN_EMAIL__'
DEFAULT_FROM_EMAIL = '__DEFAULT_FROM_EMAIL__'


# -----------------------------------------------------------------------------

# Function that will be called to finalize a user profile:
YNH_SETUP_USER = 'setup_user.setup_project_user'

SECRET_KEY = __get_or_create_secret(FINALPATH / 'secret.txt')  # /opt/yunohost/$app/secret.txt

INSTALLED_APPS += [
    'django.contrib.gis',
    'umap',
    # See https://github.com/peopledoc/django-agnocomplete/commit/26eda2dfa4a2f8a805ca2ea19a0c504b9d773a1c
    # Django does not find the app config in the default place, so the app is not loaded
    # so the "autodiscover" is not run.
    'agnocomplete.app.AgnocompleteConfig',
]
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Keep ModelBackend around for per-user permissions and superuser
AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',  # AxesBackend should be the first backend!
    #
    # Authenticate via SSO and nginx 'HTTP_REMOTE_USER' header:
    'django_yunohost_integration.sso_auth.auth_backend.SSOwatUserBackend',
    #
    # Fallback to normal Django model backend:
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = None
LOGIN_URL = '/yunohost/sso/'
LOGOUT_REDIRECT_URL = '/yunohost/sso/'
# /yunohost/sso/?action=logout
# ENABLE_ACCOUNT_LOGIN = False

ROOT_URLCONF = 'umap.urls'
WSGI_APPLICATION = 'umap.wsgi.application'

# -----------------------------------------------------------------------------
# App Settings
# Miscellaneous project settings
# =============================================================================
UMAP_ALLOW_ANONYMOUS = False
UMAP_EXTRA_URLS = {
    'routing': 'http://www.openstreetmap.org/directions?engine=osrm_car&route={lat},{lng}&locale={locale}#map={zoom}/{lat}/{lng}',  # noqa
    'ajax_proxy': '/ajax-proxy/?url={url}&ttl={ttl}',
    'search': 'https://photon.komoot.io/api/?',
}
UMAP_KEEP_VERSIONS = 10
SITE_URL = "http://umap.org"
SITE_NAME = 'uMap'
UMAP_DEMO_SITE = False
UMAP_EXCLUDE_DEFAULT_MAPS = False
UMAP_MAPS_PER_PAGE = 5
UMAP_MAPS_PER_PAGE_OWNER = 10
UMAP_USE_UNACCENT = False
UMAP_FEEDBACK_LINK = "https://wiki.openstreetmap.org/wiki/UMap#Feedback_and_help"  # noqa
USER_MAPS_URL = 'user_maps'
UMAP_READONLY = False
UMAP_GZIP = True
UMAP_XSENDFILE_HEADER = 'X-Accel-Redirect'
LOCALE_PATHS = [os.path.join(FINALPATH, 'locale')]

ADMINS = (('__ADMIN__', ADMIN_EMAIL),)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '__DB_NAME__',
        'USER': '__DB_USER__',
        'PASSWORD': '__DB_PWD__',
        'HOST': '127.0.0.1',
        'PORT': '5432',  # Default Postgres Port
        'CONN_MAX_AGE': 600,
    }
}

# ID for site to use
SITE_ID = 1

# Title of site to use
SITE_TITLE = '__APP__'

# Site domain
SITE_DOMAIN = '__DOMAIN__'

# Subject of emails includes site title
EMAIL_SUBJECT_PREFIX = f'[{SITE_TITLE}] '


# E-mail address that error messages come from.
SERVER_EMAIL = ADMIN_EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Default email address to use for various automated correspondence from
# the site managers. Used for registration emails.

# List of URLs your site is supposed to serve
ALLOWED_HOSTS = ['__DOMAIN__']

# _____________________________________________________________________________
# Static files (CSS, JavaScript, Images)

if PATH_URL:
    STATIC_URL = f'/{PATH_URL}/static/'
    MEDIA_URL = f'/{PATH_URL}/media/'
else:
    # Installed to domain root, without a path prefix?
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

STATIC_ROOT = str(PUBLIC_PATH / 'static')
MEDIA_ROOT = str(PUBLIC_PATH / 'media')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATICFILES_DIRS = []  # May be extended when using UMAP_CUSTOM_STATICS


# -----------------------------------------------------------------------------

# Set log file to e.g.: /var/log/$app/$app.log
LOGGING['handlers']['log_file']['filename'] = str(LOG_FILE)

# Example how to add logging to own app:
LOGGING['loggers']['django_example'] = {
    'handlers': ['syslog', 'log_file', 'mail_admins'],
    'level': 'INFO',
    'propagate': False,
}

# -----------------------------------------------------------------------------
# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(FINALPATH, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'umap.context_processors.settings',
                'umap.context_processors.version',
            )
        }
    },
]

try:
    from local_settings import *  # noqa:F401,F403
except ImportError:
    pass