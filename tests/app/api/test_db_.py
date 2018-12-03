
''' test redis data store '''
from app.api import db

def test_add_debt_point(mocker):
  def set_mock(aname, aval):
    return 'yes'

  class RedCli:
    def __init__(self):
      self.set = set_mock
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.add_debt_point('7', '8', 9)
  assert value == {'ok': 'yes'}

def test_get_debt_point(mocker):
  stub = mocker.stub(name='id')

  class RedCli:
    def __init__(self):
      self.get = stub
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debt_point('7:8:9')
  assert value == {'date': '8', 'id': '7:8:9', 'name': '9', 'value': 1.0}

def test_get_debt_points_empty(mocker):
  stub = mocker.stub(name='id')

  class RedCli:
    def __init__(self):
      self.keys = stub
      self.mget = stub
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debt_points('7')
  assert value == []

def test_get_debt_points(mocker):
  def keys_mock(search):
    return ['1:2:3', '4:5:6']
  def mget_mock(keys):
    return ['1', '2']

  class RedCli:
    def __init__(self):
      self.keys = keys_mock
      self.mget = mget_mock
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debt_points('7')
  assert value == [
    {'date': '2', 'id': '1:2:3', 'name': '3', 'value': 1.0},
    {'date': '5', 'id': '4:5:6', 'name': '6', 'value': 2.0}
  ]

def test_get_all_debt_points_empty(mocker):
  stub = mocker.stub(name='id')

  class RedCli:
    def __init__(self):
      self.keys = stub
      self.mget = stub
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_all_debt_points()
  assert value == []

def test_get_all_debt_points(mocker):
  def keys_mock(search):
    return ['1:2:3', '4:5:6']
  def mget_mock(keys):
    return ['1', '2']

  class RedCli:
    def __init__(self):
      self.keys = keys_mock
      self.mget = mget_mock
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_all_debt_points()
  assert value == [
    {'date': '2', 'id': '1:2:3', 'name': '3', 'value': 1.0},
    {'date': '5', 'id': '4:5:6', 'name': '6', 'value': 2.0}
  ]

def test_delete_debt_point(mocker):
  mock = mocker.Mock()
  mock.return_value = 'true'
  stub = mocker.stub(name='id')
  class RedCli:
    def __init__(self):
      self.delete = stub
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.delete_debt_point('1:2:3')
  assert value == {'id': '1:2:3', 'date': '2', 'name': '3', 'value': 1.0}
  stub.assert_called_once_with('1:2:3')

def test_unpack_result():
  assert db.unpack_result('1:2:3', 4) == {'id': '1:2:3', 'date': '2', 'name': '3', 'value': 4.0}
