''' service returning debt data '''
from functools import reduce
from . import db

def numify(num):
  try:
    return float(num)
  except ValueError:
    return 0

def add(data):
  if isinstance(data, list):
    res = []
    for value in data:
      res.append(db.add_debt_point(value['name'], value['date'], value['value']))
  else:
    res = db.add_debt_point(data['name'], data['date'], data['value'])
  return res

def get_by_id(name):
  res = db.get_debt(name)
  return res

def get_by_id_date(name, date):
  res = db.get_debt_point(name, date)
  return res

def get_by_date(date):
  values = []
  debts = db.get_debts()
  for debt in debts:
    points = db.get_debt(debt)
    in_frame = list(filter(lambda d: d <= date, points))
    if in_frame:
      point = in_frame[-1]
      values.append(points[point])
  if values:
    total = reduce((lambda x, y: numify(x) + numify(y)), values)
  return round(total, 2) if values else 0

def get_all():
  res = db.get_debts()
  return res

def delete(key):
  res = db.delete_debt_point(key)
  return res
