#!/usr/bin/env python
# -*-coding:utf-8 -*-

# import redis
#
#
# pool = redis.ConnectionPool(host='192.168.1.110', port=6379, password='redis-pass')
# conn = redis.Redis(connection_pool=pool)
# pb = conn.pubsub()
# pb.subscribe('fm104.5')
#

class SingleTon(object):

    _state = {}
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__dict__ = cls._state
        return obj

class TestClass(SingleTon):
    pass


obj1 = TestClass(1,2)
obj2 = TestClass()
print(id(obj1))
print(id(obj2))




