import config
from redis import Redis

redis_store = Redis.from_url(config.REDIS_URL)

# turn dict into a string
def serialize_dict(d):
	return str(d)

# turn string into a dict
def deserialize_dict(s):
	try:
		return eval(s)
	except:
		return s

def create_if_not_exists(k, default):
	if not redis_store.exists(k):
		redis_store.set(k, serialize_dict(default))

def save(k, v):
	redis_store.set(k, serialize_dict(v))

def append(k, v):
	redis_store.rpush(k, serialize_dict(v))

def load(k):
	return deserialize_dict(redis_store.get(k))