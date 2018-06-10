#!/usr/bin/env python
# -*-coding:utf-8 -*-
import redis
import scrapy
import scrapy_redis
from scrapyd_api import ScrapydAPI

# str = "<div>\
# <p>岗位职责：</p>\
# <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>\
# <p><br></p>\
# <p>必备要求：</p>\
# <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>\
# <p> <br></p>\
# <p>技术要求：</p>\
# <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>\
# <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>\
# <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>\
# <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>\
# <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>\
# <p> <br></p>\
# <p>加分项：</p>\
# <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>\
# </div> "
#
# import re
#
# pattern = re.compile('<div>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?br.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?br.*?<p>(.*?)</p>.*?<p>(.*?)</p>'+
#               '.*?<p>(.*?)</p>.*?<p>(.*?)<br></p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?br.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?</div>', re.S)
# # a = re.search(pattern, str).
# # print(a.groups())
#
# a = re.sub('</?\w+>| ', ' ',str)
# print(a)

# a = '''
# hello world ha ha
# '''
# import re
#
# pattern = re.compile(r'\b\w+\b')
# b = re.findall(pattern, a)
# print(b)


# python-scrapyd-api
# https://github.com/djm/python-scrapyd-api

# from scrapyd_api import ScrapydAPI
# scrapyd = ScrapydAPI('http://192.168.1.110:6800')
# a = scrapyd.schedule('zhihuuser', 'zhihu')
# print(a)

# ret = scrapyd.delete_project('zhihuuser')
# print(ret)

# ret = scrapyd.list_projects()
# print(ret)

# ret = scrapyd.list_jobs('zhihuuser')/
# print(ret)

# ret = scrapyd.list_spiders('zhihuuser')
# print(ret)

# ret = scrapyd.list_versions('zhihuuser')
# print(ret)




val = {'path': '123'}
ret = val['path']
print(ret)











