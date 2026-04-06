from settings_base import *
from django.utils.translation import gettext_lazy as _

DEBUG = True

SECRET_KEY = "8iysa30^no&oi5kv$k1w)#gsxzrylr-h6%)loz71expnbf7z%)"


EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = "gitignore/emails"

WAFER_TALKS_OPEN = True
# NB: Dont turn this setting on in prod until the program team is happy with the setup

GRANT_APPLICATIONS_OPEN = True
VISA_LETTER_REQUESTS_OPEN = True
