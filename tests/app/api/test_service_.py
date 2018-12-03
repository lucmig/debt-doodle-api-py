''' test debt servie '''
from app.api import db, service

def test_get_by_id(mocker):
  getbyidmock = mocker.MagicMock(return_value='item1')
  mocker.patch.object(db, 'get_debt_point', getbyidmock)
  res = service.get_by_id('id1')
  assert res == 'item1'
  getbyidmock.assert_called_once_with('id1')

def test_get_by_date(mocker):
  getbydatemock = mocker.MagicMock(return_value=['item1', 'item2'])
  mocker.patch.object(db, 'get_debt_points', getbydatemock)
  res = service.get_by_date('adate')
  assert res == ['item1', 'item2']
  getbydatemock.assert_called_once_with('adate')

def test_get_all(mocker):
  getallmock = mocker.MagicMock(return_value=['item1', 'item2'])
  mocker.patch.object(db, 'get_all_debt_points', getallmock)
  res = service.get_all()
  assert res == ['item1', 'item2']
  getallmock.assert_called_once_with()

def test_add(mocker):
  addmock = mocker.MagicMock(return_value='ok')
  testval = {'date': 'adate', 'name': 'aname', 'value': 123.45}
  mocker.patch.object(db, 'add_debt_point', addmock)
  res = service.add(testval)
  assert res == 'ok'
  addmock.assert_called_once_with('adate', 'aname', 123.45)

def test_add_many(mocker):
  addmanymock = mocker.MagicMock(return_value='ok')
  testval = [
    {'date': 'adate', 'name': 'aname', 'value': 123.45},
    {'date': 'bdate', 'name': 'bname', 'value': 678.9}
    ]
  mocker.patch.object(db, 'add_debt_point', addmanymock)
  res = service.add(testval)
  assert res == ['ok', 'ok']
  calls = [mocker.call('adate', 'aname', 123.45), mocker.call('bdate', 'bname', 678.9)]
  addmanymock.assert_has_calls(calls)

def test_delete(mocker):
  delmock = mocker.MagicMock(return_value='ok')
  mocker.patch.object(db, 'delete_debt_point', delmock)
  res = service.delete('id1')
  assert res == 'ok'
  delmock.assert_called_once_with('id1')
