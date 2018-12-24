
''' test redis data store '''
from app.api import db

def test_add_debt_point(mocker):
  def mock_hset(hname, vname, val):
    return 'yes'

  class RedCli:
    def __init__(self):
      self.hset = mock_hset

  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.add_debt_point('7', '8', 9)
  assert value == {'ok': 'yes'}

def test_get_debts_empty(mocker):
  def mock_keys(search): 
    return None

  class RedCli:
    def __init__(self):
      self.keys = mock_keys
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debts()
  assert value == []

def test_get_debts(mocker):
  def mock_keys(search): 
    return ['debt:a', 'debt:b', 'debt:c']

  class RedCli:
    def __init__(self):
      self.keys = mock_keys
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debts()
  assert value == ['a', 'b', 'c']

def test_get_debt_empty(mocker):
  def mock_hgetall(name): 
    return None

  class RedCli:
    def __init__(self):
      self.hgetall = mock_hgetall
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debt('7')
  assert value == {}

def test_get_debt(mocker):
  def mock_hgetall(name): 
    return {
      'date1': '1.23',
      'date2': '45.67'
    }

  class RedCli:
    def __init__(self):
      self.hgetall = mock_hgetall
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debt('7')
  assert value == {
    'date1': '1.23',
    'date2': '45.67'
  }

def test_get_debt_point_empty(mocker):
  def mock_hget(key, date): 
    return None

  class RedCli:
    def __init__(self):
      self.hget = mock_hget
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

def test_get_debt_point(mocker):
  def mock_hget(key, date): 
    return 1.23

  class RedCli:
    def __init__(self):
      self.hget = mock_hget
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.get_debt_point('hkey', 'adate')
  assert value == {'date': 'adate', 'name': 'hkey', 'value': 1.23}

def test_delete_debt_point(mocker):
  def mock_delete(key): 
    return 'ok'

  class RedCli:
    def __init__(self):
      self.delete = mock_delete
  rds = RedCli()
  mocker.patch.object(db, 'get_redis', return_value=rds, autospec=True)

  value = db.delete_debt_point('1:2:3')
  assert value == { 'deleted': 'ok' }
  # mock_delete.assert_called_once_with('1:2:3')
