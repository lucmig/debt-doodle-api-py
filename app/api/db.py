''' interface with redis store '''
import os
import redis

def get_redis():
  return redis.StrictRedis(
    host=os.environ['REDIS_HOST'],
    port=int(os.environ['REDIS_PORT']),
    password=os.environ['REDIS_PASSWORD'],
    decode_responses=True)

def add_debt_point(date, name, value):
  rds = get_redis()
  key = 'debt:%s:%s' % (date, name)
  res = rds.set(key, value)
  return {'ok': res}

def get_debt_point(key):
  rds = get_redis()
  value = rds.get(key)
  return {} if value is None else unpack_result(key, value)

def get_debt_points(date):
  rds = get_redis()
  search = 'debt:%s:*' % (date)
  keys = rds.keys(search)
  if not keys:
    return []
  values = rds.mget(keys)
  debt_points = [unpack_result(keys[values.index(dp)], dp) for dp in values]
  return debt_points

def get_all_debt_points():
  rds = get_redis()
  search = 'debt:*'
  keys = rds.keys(search)
  if not keys:
    return []
  values = rds.mget(keys)
  debt_points = [unpack_result(keys[values.index(dp)], dp) for dp in values]
  return debt_points

def delete_debt_point(key):
  rds = get_redis()
  value = rds.delete(key)
  return unpack_result(key, value)

def unpack_result(key, value):
  return {
    'id': key,
    'date': key.split(':')[1],
    'name': key.split(':')[2],
    'value': float(value)
    }
