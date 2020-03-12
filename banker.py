import logging
from logging.config import dictConfig

from flask import Flask

from config import LOGGING

dictConfig(LOGGING)


app = Flask(__name__)
app.logger = logging.getLogger('banker')
app.logger.info("Banker started")


import views
