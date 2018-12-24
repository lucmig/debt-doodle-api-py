''' test restful api routes '''
from aiohttp import web

from app.api import routes, service

async def test_get_all(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value=['item1', 'item2'])
  mocker.patch.object(service, 'get_all', mock)
  app = web.Application()
  app.router.add_get('/', routes.get_all)
  client = await aiohttp_client(app)
  resp = await client.get('/')
  assert resp.status == 200
  json = await resp.json()
  assert ['item1', 'item2'] == json

async def test_get_by_id(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value={'item': 'item1'})
  mocker.patch.object(service, 'get_by_id', mock)
  app = web.Application()
  app.router.add_get('/{id}', routes.get_by_id)
  client = await aiohttp_client(app)
  resp = await client.get('/id1')
  assert resp.status == 200
  json = await resp.json()
  assert {'item': 'item1'} == json

async def test_get_point(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value={'item': 'item1'})
  mocker.patch.object(service, 'get_by_id_date', mock)
  app = web.Application()
  app.router.add_get('/{id}/{date}', routes.get_point)
  client = await aiohttp_client(app)
  resp = await client.get('/id1/date1')
  assert resp.status == 200
  json = await resp.json()
  assert {'item': 'item1'} == json

async def test_get_by_date(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value=['item3', 'item4'])
  mocker.patch.object(service, 'get_by_date', mock)
  app = web.Application()
  app.router.add_get('/date/{date}', routes.get_by_date)
  client = await aiohttp_client(app)
  resp = await client.get('/date/adate')
  assert resp.status == 200
  json = await resp.json()
  assert ['item3', 'item4'] == json

async def test_add(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value={'is': 'ok'})
  mocker.patch.object(service, 'add', mock)
  app = web.Application()
  app.router.add_post('/', routes.add)
  client = await aiohttp_client(app)
  resp = await client.post('/', json={'value': 'foo'})
  assert resp.status == 200
  json = await resp.json()
  assert {'is': 'ok'} == json

async def test_delete(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value={'is': 'ok'})
  mocker.patch.object(service, 'delete', mock)
  app = web.Application()
  app.router.add_delete('/{id}', routes.delete)
  client = await aiohttp_client(app)
  resp = await client.delete('/id1')
  assert resp.status == 200
  json = await resp.json()
  assert {'is': 'ok'} == json
