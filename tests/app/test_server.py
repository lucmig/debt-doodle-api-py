import os
import logging
from aiohttp import web

from app.api import routes

def test_server_start(mocker):
