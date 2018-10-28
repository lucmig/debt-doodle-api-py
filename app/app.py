import os
import logging
from aiohttp import web

from api import routes

app = web.Application()
logging.info('Starting up...')
routes.init(app)
web.run_app(app, port=int(os.environ['PORT']), print=logging.info)