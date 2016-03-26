#-*-coding: utf-8 -*-
import time
import random

import wrapcache
from wrapcache.adapter.RedisAdapter import RedisAdapter

def cache_filter(a,b):
    print a,b
    return a+b<10
@wrapcache.wrapcache(timeout=3600,adapter = RedisAdapter,cache_filter=cache_filter)
def need_redis_cache_function(a,b):
    time.sleep(2)
    return (random.randint(1, 100), 'Hello wrapcache')

if __name__ =='__main__':
    import redis
    REDIS_POOL = redis.ConnectionPool(host = '127.0.0.1', port = 6379, password = '', db = 1)
    REDIS_INST = redis.Redis(connection_pool = REDIS_POOL, charset = 'utf8')
    RedisAdapter.db = REDIS_INST

    print need_redis_cache_function(10,3)
