import logging
import os
from datetime import datetime
from pathlib import Path

LOG_DIRECTORY = "../applog"


class AppFileHandler(logging.FileHandler):
    def __init__(self):
        log_directory = Path(LOG_DIRECTORY)
        if not log_directory.exists():
            os.mkdir(log_directory)
        filename = '{}/{:%Y-%m-%d}.log'.format(LOG_DIRECTORY, datetime.utcnow())
        super(AppFileHandler, self).__init__(filename)


config = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s:%(levelname)s:%(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'class': 'core.logger.AppFileHandler',
            'formatter': 'default',
        },
    },
    'root': {
        'level': "INFO",
        'handlers': ['console', 'file']
    }
}
