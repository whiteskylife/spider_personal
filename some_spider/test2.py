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




# val = {'path': '123'}
# ret = val['path']
# print(ret)
#




# import requests
# from urllib.parse import urlencode
# base_url = 'http://op.juhe.cn/onebox/stock/query?'
# key = '阿里巴巴'
# params = {
#     'key': '8bcb478d3704170298e1aa1c7f5c6a19',
#     'stock': key,
# }
# url = base_url + urlencode(params)
# print(url)
# # ret = requests.get(url)
# ret = requests.get(base_url, params=params)
# print(ret.json())
# print(type(ret.json()))
#
import threading
import requests
from queue import Queue
from lxml import etree


class Spider(threading.Thread):
    def __init__(self, threadname, u_queue, h_queue):
        threading.Thread.__init__(self)
        self.u_queue = u_queue
        self.h_queue = h_queue
        self.threadname = threadname

    def run(self):
        print(self.threadname + ":正在获取")
        headers = {"User-Agent": "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"}
        while not self.u_queue.empty():
            response = requests.get(self.u_queue.get(), headers=headers)
            html = response.text
            self.h_queue.put(html)


class ParseInfo(threading.Thread):
    def __init__(self, threadname, h_queue, filename, lock):
        threading.Thread.__init__(self)
        self.h_queue = h_queue
        self.filename = filename
        self.lock = lock
        self.threadname = threadname

    def run(self):
        print(self.threadname + ":正在解析")
        while not self.h_queue.empty():
            e = etree.HTML(self.h_queue.get())
            infos = e.xpath('//div[@id="content-left"]//div[@class="content"]/span/text()')

            if self.lock.acquire():
                for info in infos:
                    self.filename.write(info)
                self.lock.release()

# //div[@id="content-left"]//div[@class="content"]/span/text()

def main(num):
    url_queue = Queue()
    html_queue = Queue()
    url = "https://www.qiushibaike.com/8hr/page/{}/"
    filename = open("qiushi.html", "a", encoding='utf-8')
    for i in range(1, num + 1):
        new_url = url.format(i)
        url_queue.put(new_url)

    spider1 = Spider("1号", url_queue, html_queue)
    spider2 = Spider("2号", url_queue, html_queue)
    spider3 = Spider("3号", url_queue, html_queue)
    spider_array = []
    spider_array.append(spider1)
    spider_array.append(spider2)
    spider_array.append(spider3)

    for s in spider_array:
        s.start()

    for s in spider_array:
        s.join()

    lock = threading.Lock()
    parse1 = ParseInfo("4号", html_queue, filename, lock)
    parse2 = ParseInfo("5号", html_queue, filename, lock)
    parse3 = ParseInfo("6号", html_queue, filename, lock)
    parese_array = []
    parese_array.extend([parse1,parse2,parse3])
    for p in parese_array:
        p.start()

    for p in parese_array:
        p.join()
    threading.Lock()
    filename.close()


if __name__ == '__main__':
    num = 1
    # num = int(input("请输入要下载几页:"))
    main(num)
