#!/usr/bin/env python
# -*-coding:utf-8 -*-
# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# response = requests.get('http://www.jianshu.com', headers=headers)
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)
# import re
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# content = re.sub('\d+', 'Replacement', content)
# print(content)

# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
#
# a = doc('#container ul li')
# print(a )
# try:
#     int('asdasd')
# except Exception as e:
#     print(e.args)
#     print(e)

#
# first_letters = set()
# words = 'happy new year!'
# # for w in words:
# #     first_letters.add(w[0])
# # print(first_letters)
# original = {'key1': '666', 'whisky': 'hahaa'}
# flipped = {}
# for key, value in original.items():
#     flipped[value] = key
#
# flipped = {v:k for k, v in original.items()}
# print(flipped)





class Scheduler():
    def __init__(self):
        self._process = 'asssssssssd'

import sys

try:

    if sys.argv[1] == 'asd':
        print('asd')

    int('sad')
except IndexError as e:
    print(e)
except Exception as other:
    print('other', other)
finally:
    print('------------------------')









