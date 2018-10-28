import os
import logging
import asyncio
import redis

db = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=int(os.environ['REDIS_PORT']), password=os.environ['REDIS_PASSWORD'], decode_responses=True)

def addDebtPoint(date, name, value):
  key = 'debt:%s:%s' % (date, name)
  res = db.set(key, value)
  return { 'ok': res }

def getDebtPoint(id):
  value = db.get(id)
  return unpackResult(id, value)

def getDebtPoints(date):
  search = 'debt:%s:*' % (date)
  keys = db.keys(search)
  if len(keys) == 0:
    return []
  values = db.mget(keys)
  debtPoints = [unpackResult(keys[values.index(dp)], dp) for dp in values]
  return debtPoints

def getAllDebtPoints():
  search = 'debt:*'
  keys = db.keys(search)
  if len(keys) == 0:
    return []
  values = db.mget(keys)
  debtPoints = [unpackResult(keys[values.index(dp)], dp) for dp in values]
  return debtPoints

def deleteDebtPoint(id):
  value = db.delete(id)
  return unpackResult(id, value)

def unpackResult(id, value):
  return {
    'date' : id.split(':')[1], 
    'name' : id.split(':')[2], 
    'value' : float(value)
    }