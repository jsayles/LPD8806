import os
import logging


################################################################################
# Default Settings
#################################################################################


DEBUG = False

SECRET_KEY = 'change_me_before_production'

WEBCAM_URL = 'http://example.com/webcam'


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
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'flask.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'file']
    }
}


#################################################################################


# Load the local settings file if it exists
if os.path.isfile('webapp/local_settings.py'):
    from local_settings import *
else:
    logging.error("No local settings file found.")
