''' test debt servie '''
from app.api import db, service

def test_add(mocker):
  addmock = mocker.MagicMock(return_value='ok')
  testval = {'date': 'adate', 'name': 'aname', 'value': 123.45}
  mocker.patch.object(db, 'add_debt_point', addmock)
  res = service.add(testval)
  assert res == 'ok'
  addmock.assert_called_once_with('aname', 'adate', 123.45)

def test_add_many(mocker):
  addmanymock = mocker.MagicMock(return_value='ok')
  testval = [
    {'date': 'adate', 'name': 'aname', 'value': 123.45},
    {'date': 'bdate', 'name': 'bname', 'value': 678.9}
    ]
  mocker.patch.object(db, 'add_debt_point', addmanymock)
  res = service.add(testval)
  assert res == ['ok', 'ok']
  calls = [mocker.call('aname', 'adate', 123.45), mocker.call('bname', 'bdate', 678.9)]
  addmanymock.assert_has_calls(calls)

def test_get_by_id(mocker):
  getbyidmock = mocker.MagicMock(return_value={'name': 'namea', 'date': 'adate', 'value': 1.23})
  mocker.patch.object(db, 'get_debt', getbyidmock)
  res = service.get_by_id('id1')
  assert res == {'name': 'namea', 'date': 'adate', 'value': 1.23}
  getbyidmock.assert_called_once_with('id1')

def test_get_by_id_date(mocker):
  mock = mocker.MagicMock(return_value={'name': 'namea', 'date': 'adate', 'value': 1.23})
  mocker.patch.object(db, 'get_debt_point', mock)
  res = service.get_by_id_date('id1', 'adate')
  assert res == {'name': 'namea', 'date': 'adate', 'value': 1.23}
  mock.assert_called_once_with('id1', 'adate')

def test_get_by_date(mocker):
  mock_get_debts = mocker.MagicMock(return_value=['name1', 'name2'])
  mocker.patch.object(db, 'get_debts', mock_get_debts)
  mock_get_debt = mocker.MagicMock(return_value={'1': '1', '2': '2', '3': '3', '4': '4'})
  mocker.patch.object(db, 'get_debt', mock_get_debt)
  res = service.get_by_date('3')
  assert res == 6
  mock_get_debts.assert_called_once()
  assert mock_get_debt.call_count == 2

def test_get_all(mocker):
  getallmock = mocker.MagicMock(return_value=['item1', 'item2'])
  mocker.patch.object(db, 'get_debts', getallmock)
  res = service.get_all()
  assert res == ['item1', 'item2']
  getallmock.assert_called_once_with()

def test_delete(mocker):
  delmock = mocker.MagicMock(return_value='ok')
  mocker.patch.object(db, 'delete_debt_point', delmock)
  res = service.delete('id1')
  assert res == 'ok'
  delmock.assert_called_once_with('id1')
