''' service returning debt data '''
from . import db

def get_by_id(key):
  res = db.get_debt_point(key)
  return res

def get_by_date(date):
  res = db.get_debt_points(date)
  return res

def get_all():
  res = db.get_all_debt_points()
  return res

def add(data):
  if isinstance(data, list):
    res = []
    for value in data:
      res.append(db.add_debt_point(value['date'], value['name'], value['value']))
  else:
    res = db.add_debt_point(data['date'], data['name'], data['value'])
  return res

def delete(key):
  res = db.delete_debt_point(key)
  return res
