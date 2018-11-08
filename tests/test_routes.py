from aiohttp import web

from app.api import routes, service

async def test_getAll(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value=['item1', 'item2'])
  mocker.patch.object(service, 'getAll', mock)  
  app = web.Application()
  app.router.add_get('/', routes.getAll)
  client = await aiohttp_client(app)
  resp = await client.get('/')
  assert resp.status == 200
  json = await resp.json()
  assert ['item1', 'item2'] == json

async def test_getById(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value={ 'item': 'item1'})
  mocker.patch.object(service, 'getById', mock)  
  app = web.Application()
  app.router.add_get('/{id}', routes.getById)
  client = await aiohttp_client(app)
  resp = await client.get('/id1')
  assert resp.status == 200
  json = await resp.json()
  assert { 'item': 'item1' } == json

async def test_getByDate(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value=['item3', 'item4'])
  mocker.patch.object(service, 'getByDate', mock)  
  app = web.Application()
  app.router.add_get('/date/{date}', routes.getByDate)
  client = await aiohttp_client(app)
  resp = await client.get('/date/adate')
  assert resp.status == 200
  json = await resp.json()
  assert ['item3', 'item4'] == json

async def test_add(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value={ 'is': 'ok' })
  mocker.patch.object(service, 'add', mock)  
  app = web.Application()
  app.router.add_post('/', routes.add)
  client = await aiohttp_client(app)
  resp = await client.post('/', json={'value': 'foo'})
  assert resp.status == 200
  json = await resp.json()
  assert { 'is': 'ok' } == json

async def test_delete(aiohttp_client, mocker):
  mock = mocker.MagicMock(return_value={ 'is': 'ok' })
  mocker.patch.object(service, 'delete', mock)  
  app = web.Application()
  app.router.add_delete('/{id}', routes.delete)
  client = await aiohttp_client(app)
  resp = await client.delete('/id1')
  assert resp.status == 200
  json = await resp.json()
  assert { 'is': 'ok' } == json
