from aiohttp import web

from app.api import service

async def getAll(request):
  data = service.getAll()
  return web.json_response(data)

async def getById(request):
  id = request.match_info.get('id')
  data = service.getById(id)
  return web.json_response(data)

async def getByDate(request):
  date = request.match_info.get('date')
  data = service.getByDate(date)
  return web.json_response(data)

async def add(request):
  data = await request.json()
  res = service.add(data)
  return web.json_response(res)

async def delete(request):
  id = request.match_info.get('id')
  data = service.delete(id)
  return web.json_response(data)

def init(app):
  app.add_routes([
    web.get('/', getAll),
    web.get('/{id}', getById),
    web.get('/date/{date}', getByDate),
    web.post('/', add),
    web.delete('/{id}', delete)
    ])