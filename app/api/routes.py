''' restful api routes '''
from aiohttp import web

from . import service

#pylint: disable=W0613
async def get_all(request):
  data = service.get_all()
  return web.json_response(data)

async def get_by_id(request):
  key = request.match_info.get('id')
  data = service.get_by_id(key)
  return web.json_response(data)

async def get_by_date(request):
  date = request.match_info.get('date')
  data = service.get_by_date(date)
  return web.json_response(data)

async def add(request):
  data = await request.json()
  res = service.add(data)
  return web.json_response(res)

async def delete(request):
  key = request.match_info.get('id')
  data = service.delete(key)
  return web.json_response(data)

def init(app):
  app.add_routes([
    web.get('/', get_all),
    web.get('/{id}', get_by_id),
    web.get('/date/{date}', get_by_date),
    web.post('/', add),
    web.delete('/{id}', delete)
  ])
