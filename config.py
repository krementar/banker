import logging


DB_NAME = "payments.db"

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
        },
    },

    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'banker.log',
        },
    },
    'loggers': {
        'banker': {
            'handlers': ['file', ],
            'level': logging.DEBUG
        },
    },
}
