from app.api import db
from app.api import service

def test_getById(mocker):
  getbyidmock = mocker.MagicMock(return_value='item1')
  mocker.patch.object(db, 'getDebtPoint', getbyidmock)
  res = service.getById('id1')
  assert res == 'item1'
  getbyidmock.assert_called_once_with('id1')

def test_getByDate(mocker):
  getbydatemock = mocker.MagicMock(return_value=['item1', 'item2'])
  mocker.patch.object(db, 'getDebtPoints', getbydatemock)
  res = service.getByDate('adate')
  assert res == ['item1', 'item2']
  getbydatemock.assert_called_once_with('adate')

def test_getAll(mocker):
  getallmock = mocker.MagicMock(return_value=['item1', 'item2'])
  mocker.patch.object(db, 'getAllDebtPoints', getallmock)
  res = service.getAll()
  assert res == ['item1', 'item2']
  getallmock.assert_called_once_with()

def test_add(mocker):
  addmock = mocker.MagicMock(return_value='ok')
  testval = {'date': 'adate', 'name': 'aname', 'value': 123.45}
  mocker.patch.object(db, 'addDebtPoint', addmock)
  res = service.add(testval)
  assert res == 'ok'
  addmock.assert_called_once_with('adate', 'aname', 123.45)

def test_addMany(mocker):
  addmanymock = mocker.MagicMock(return_value='ok')
  testval = [{'date': 'adate', 'name': 'aname', 'value': 123.45}, {'date': 'bdate', 'name': 'bname', 'value': 678.9}]
  mocker.patch.object(db, 'addDebtPoint', addmanymock)
  res = service.add(testval)
  assert res == ['ok', 'ok']
  calls = [mocker.call('adate', 'aname', 123.45), mocker.call('bdate', 'bname', 678.9)]
  addmanymock.assert_has_calls(calls)

def test_delete(mocker):
  delmock = mocker.MagicMock(return_value='ok')
  mocker.patch.object(db, 'deleteDebtPoint', delmock)
  res = service.delete('id1')
  assert res == 'ok'
  delmock.assert_called_once_with('id1')
