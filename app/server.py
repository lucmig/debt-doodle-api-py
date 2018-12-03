#pylint: disable=E0611
''' main server '''
import os
import logging
from aiohttp import web

from api import routes

APP = web.Application()
logging.info('Starting up...')
routes.init(APP)
web.run_app(APP, port=int(os.environ['PORT']), print=logging.info)
