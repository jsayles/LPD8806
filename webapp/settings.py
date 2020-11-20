import os
import logging


################################################################################
# Default Settings
#################################################################################


DEBUG = False

# This needs to be set before app is moved into production
# os.urandom(32).hex()
SECRET_KEY = "SUPER_SECRET"

# Default to Port of Vancouver
WEBCAM_URL = "http://207.194.15.97/mjpg/video.mjpg"

DEFAULT_BRIGHTNESS = 50


#################################################################################
# Logging
#################################################################################


LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/flask.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file']
    },
}


#################################################################################


# Load the local settings file if it exists
if os.path.isfile('webapp/local_settings.py'):
    from webapp.local_settings import *
else:
    logging.error("No local settings file found.")
