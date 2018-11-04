from app.api import db

def getById(id):
  res = db.getDebtPoint(id)
  return res

def getByDate(date):
  res = db.getDebtPoints(date)
  return res

def getAll():
  res = db.getAllDebtPoints()
  return res

def add(data):
  if isinstance(data, list):
    res = []
    for value in data:
      res.append(db.addDebtPoint(value['date'], value['name'], value['value']))
  else:
    res = db.addDebtPoint(data['date'], data['name'], data['value'])
  return res

def delete(id):
  res = db.deleteDebtPoint(id)
  return res
