# -*- encoding = utf-8 -*-
import os.path
from logging.config import dictConfig

if not os.path.exists('../logs'):
    os.mkdir('../logs')

dictConfig({
    'version': 1,
    "disable_existing_loggers": False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        "log_file": {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'logs/log.log',
            'maxBytes': 20 * 1024 * 1024,  # 1MB
            'backupCount': 10,
            "encoding": "utf-8"
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'log_file']
    }
})