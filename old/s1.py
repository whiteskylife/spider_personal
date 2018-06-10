#!/usr/bin/env python
# -*-coding:utf-8 -*-

# import redis
# pool = redis.ConnectionPool(host='192.168.1.110', port=6379, password='redis-pass')
# conn = redis.Redis(connection_pool=pool)
# conn.publish('fm104.5', '1111')
import json

# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.__class__.__class__.__class__.__class__)
# ret = soup.find_all('ul')
# for i in ret:
#     print(i.find_all('li'))
#     for m in i.find_all('li'):
#         print(m.find('li'))
# import logging
#
# # logging.basicConfig(level=logging.DEBUG)
#
# logger = logging.getLogger('spider1')
# logger.setLevel(logging.INFO)
#
# handler = logging.FileHandler('hello.log', encoding='utf-8')
# handler.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
#
# # add the handlers to the logger
#
# logger.addHandler(handler)
#
# logger.info('Hello baby')
# logger.error('error-- 中文')
#
# import os
# logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
# logging.debug('this is a message')
# import os
# if not os.path.exists('stat_log'):
#     os.mkdir('stat_log')
# with open('stat_log/log.txt', 'a') as f:
#     f.write('asd')
#
# import logging

# a = logging.error('asd')
# import threading
#
# class Foo:
#     # def __call__(self, *args, **kwargs):
#     #     print('asasdasdasd')
#
#     def __new__(cls, *args, **kwargs):
#         print('=============')
#         return type.__new__(cls, *args, **kwargs)
#
#
#     def test(self):
#         print('in the test')
#
#
# obj = Foo()
# obj.test()




import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


class Foo(Singleton):
    def test(self):
        print('1111111111111111')


# a = Foo()
# b = Foo()
# print(a)
# print(b)
#
#


# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1,obj2)



