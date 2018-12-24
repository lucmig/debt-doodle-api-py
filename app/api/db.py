''' interface with redis store '''
import os
import redis

def get_redis():
  return redis.StrictRedis(
    host=os.environ['REDIS_HOST'],
    port=int(os.environ['REDIS_PORT']),
    password=os.environ['REDIS_PASSWORD'],
    decode_responses=True)

def add_debt_point(name, date, value):
  rds = get_redis()
  key = 'debt:%s' % (name)
  res = rds.hset(key, date, value)
  return {'ok': res}

def get_debts():
  rds = get_redis()
  search = 'debt:*'
  keys = rds.keys(search)
  if not keys:
    return []
  debts = []
  for key in keys:
    debts.append(key.split(':')[1])
  return debts

def get_debt(name):
  key = 'debt:%s' % (name)
  rds = get_redis()
  values = rds.hgetall(key)
  return {} if values is None else values

def get_debt_point(name, date):
  key = 'debt:%s' % (name)
  rds = get_redis()
  value = rds.hget(key, date)
  return {} if value is None else {
    'name': name,
    'date': date,
    'value': float(value)
  }

def delete_debt_point(key):
  rds = get_redis()
  value = rds.delete(key)
  return { 'deleted': value }
