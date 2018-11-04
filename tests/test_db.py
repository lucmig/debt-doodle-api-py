import os
import redis

import mock 
import pytest
from pytest_mock import mocker 

from app.api import db

def test_addDebtPoint(mocker):
  def setMock(aname, aval):
    return 'yes'

  class RedCli:
    def __init__(self):
      self.set = setMock
  rds = RedCli()
  mocker.patch.object(db, 'getRedis', return_value=rds, autospec=True)

  value = db.addDebtPoint('7', '8', 9)
  assert value == {'ok': 'yes'}

def test_getDebtPoint(mocker):
  stub = mocker.stub(name='id')

  class RedCli:
    def __init__(self):
      self.get = stub
  rds = RedCli()
  mocker.patch.object(db, 'getRedis', return_value=rds, autospec=True)

  value = db.getDebtPoint('7:8:9')
  assert value == {'date': '8', 'id': '7:8:9', 'name': '9', 'value': 1.0}

def test_getDebtPoints_empty(mocker):
  stub = mocker.stub(name='id')

  class RedCli:
    def __init__(self):
      self.keys = stub
      self.mget = stub
  rds = RedCli()
  mocker.patch.object(db, 'getRedis', return_value=rds, autospec=True)

  value = db.getDebtPoints('7')
  assert value == []

def test_getDebtPoints(mocker):
  def keysMock(search):
    return ['1:2:3', '4:5:6']
  def mgetMock(keys):
    return ['1', '2']

  class RedCli:
    def __init__(self):
      self.keys = keysMock
      self.mget = mgetMock
  rds = RedCli()
  mocker.patch.object(db, 'getRedis', return_value=rds, autospec=True)

  value = db.getDebtPoints('7')
  assert value == [
    {'date': '2', 'id': '1:2:3', 'name': '3', 'value': 1.0}, 
    {'date': '5', 'id': '4:5:6', 'name': '6', 'value': 2.0}
  ]

def test_getAllDebtPoints_empty(mocker):
  stub = mocker.stub(name='id')

  class RedCli:
    def __init__(self):
      self.keys = stub
      self.mget = stub
  rds = RedCli()
  mocker.patch.object(db, 'getRedis', return_value=rds, autospec=True)

  value = db.getAllDebtPoints()
  assert value == []

def test_getAllDebtPoints(mocker):
  def keysMock(search):
    return ['1:2:3', '4:5:6']
  def mgetMock(keys):
    return ['1', '2']

  class RedCli:
    def __init__(self):
      self.keys = keysMock
      self.mget = mgetMock
  rds = RedCli()
  mocker.patch.object(db, 'getRedis', return_value=rds, autospec=True)

  value = db.getAllDebtPoints()
  assert value == [
    {'date': '2', 'id': '1:2:3', 'name': '3', 'value': 1.0}, 
    {'date': '5', 'id': '4:5:6', 'name': '6', 'value': 2.0}
  ]

def test_deleteDebtPoint(mocker):
  mock = mocker.Mock()
  mock.return_value = 'true'
  stub = mocker.stub(name='id')
  class RedCli:
    def __init__(self):
      self.delete = stub
  rds = RedCli()
  mocker.patch.object(db, 'getRedis', return_value=rds, autospec=True)
  
  value = db.deleteDebtPoint('1:2:3')
  assert value == { 'id': '1:2:3', 'date': '2', 'name': '3', 'value': 1.0 }
  stub.assert_called_once_with('1:2:3')

def test_unpackResult(mocker):
  assert db.unpackResult('1:2:3', 4) == { 'id': '1:2:3', 'date': '2', 'name': '3', 'value': 4.0 }
