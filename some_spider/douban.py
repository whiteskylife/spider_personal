#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
'''
# content = requests.request(method="GET", url="https://book.douban.com/")
content = requests.request(method="GET", url="https://movie.douban.com/top250", headers=headers)
html = content.text

pattern = re.compile('<div.*?item">.*?title">(.*?)</span>.*?class="">(.*?)<br>.*?inq">(.*?)</span>.*?</div>', re.S)
ret = re.findall(pattern, html)
# print(ret)
for item in ret:
    name, director, quote = item
    print(name, director.strip(), quote.strip())

'''

content = requests.request(url='https://book.douban.com/', method="GET", headers=headers)
html = content.text
r = '<li.*?cover">.*?href="(.*?)" title="(.*?)">.*?<span class="author">(.*?)'
r += '</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?abstract">(.*?)</p>.*?</li>'
# pattern = re.compile('<li.*?cover">.*?href="(.*?)" title="(.*?)">.*?<span class="author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?abstract">(.*?)</p>.*?</li>', re.S)
pattern = re.compile(r, re.S)
ret = re.findall(pattern, html)
for item in ret:
    href, title, author, year, publisher, abstract = item
    author = re.sub('\s', '', author)
    abstract = re.sub('\s', '', abstract)
    print(href, title, author, year.strip(), publisher.strip(), abstract)

# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）


