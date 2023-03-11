import redis

def redis_init():

    redis_client = redis.Redis(host='localhost', port=6379, db=0)

    return redis_client

