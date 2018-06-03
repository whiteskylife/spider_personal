#!/usr/bin/env python
# -*-coding:utf-8 -*-
import re

# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><div><a href="link3.html"><span class="bold">third item</span></a><span>美食</span></div></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
#
# from pyquery import PyQuery as pq
#
# doc = pq(html)
# a = doc('.item-0.active')
# print(a.text())
#

# import redis
#
# r = redis.Redis(host='192.168.1.110', port=6379, password='redis-pass', decode_responses=True)
# s = r.lrange('mylist', 0, -1)
# print(s)

# dict = {'acrawl_12312': '213123'}
# for k, v in dict.items():
#     if 'acrawl_1' in v:
#         print('yes')
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             
             <li class="item-0 active">
                <a href="link3.html"></a>
                <a href="link3123.html"></a>
                <spaan>asdasd</span>
             </li>
             
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.active span')
print(a)
s = '¥\n36.60\n'
s1 = 'asd123pppp'
# print(s.strip(), 'sdfsdfsdf')
# print(s1.strip('3'))
print(s.replace('\n', '222222', ))
