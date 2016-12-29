from .settings_base import *

import dj_database_url

STATIC_ROOT = BASE_DIR.child("staticfiles")

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DEBUG = False
SECRET_KEY = get_environment_variable('DJANGO_SECRET_KEY')
