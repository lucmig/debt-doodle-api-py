import os
import logging
import asyncio
import redis

def getRedis():
  return redis.StrictRedis(host=os.environ['REDIS_HOST'], port=int(os.environ['REDIS_PORT']), password=os.environ['REDIS_PASSWORD'], decode_responses=True)

def addDebtPoint(date, name, value):
  rds = getRedis()
  key = 'debt:%s:%s' % (date, name)
  res = rds.set(key, value)
  return { 'ok': res }

def getDebtPoint(id):
  rds = getRedis()
  value = rds.get(id)
  return unpackResult(id, value)

def getDebtPoints(date):
  rds = getRedis()
  search = 'debt:%s:*' % (date)
  keys = rds.keys(search)
  if len(keys) == 0:
    return []
  values = rds.mget(keys)
  debtPoints = [unpackResult(keys[values.index(dp)], dp) for dp in values]
  return debtPoints

def getAllDebtPoints():
  rds = getRedis()
  search = 'debt:*'
  keys = rds.keys(search)
  if len(keys) == 0:
    return []
  values = rds.mget(keys)
  debtPoints = [unpackResult(keys[values.index(dp)], dp) for dp in values]
  return debtPoints

def deleteDebtPoint(id):
  rds = getRedis()
  value = rds.delete(id)
  return unpackResult(id, value)

def unpackResult(id, value):
  return {
    'id': id,
    'date': id.split(':')[1], 
    'name': id.split(':')[2], 
    'value': float(value)
    }