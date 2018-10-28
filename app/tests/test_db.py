import mock 
import pytest
from pytest_mock import mocker 

@mock.patch('api.db.db')
@mock.patch('os.environ')

def test_unpackResult(mock_db, mock_env):
  from api import db

  assert db.unpackResult('1:2:3', 4) == { 'date': '2', 'name': '3', 'value': 4.0 }
