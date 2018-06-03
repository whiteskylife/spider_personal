#!/usr/bin/env python
# -*-coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400'
}


def get_page():
    for i in range(1, 2):
        start_url = 'http://www.xicidaili.com/nn/{}'.format(i)
        response = requests.get(start_url, headers=headers).text

        # pattern = re.compile('<tr class.*?<td>(\d+\.\d+\.\d+\.\d+)</td>.*?<td>(\d+)</td>.*?</tr>', re.S)
        # result = pattern.findall(response)
        # for i in result:
        #     yield ':'.join([i[0], i[1]])
        #
        # # BS4
        # soup = BeautifulSoup(response, 'lxml')  # BeautifulSoup不支持jQuery选择器！
        # ret = soup.find_all('table')  # find_all 只能找标签，找属性要通过：find_all(attrs={}) , 返回一个列表
        # for i in ret:
        #     for tr in i.find_all('tr')[1:]:
        #         tag = tr.find_all('td')
        #         # port = tr.select('td:eq(2)')
        #         print(tag)
        #         #  省略n行代码...
        #
        # # pyquery
        # doc = pq(response)
        # # ip = doc('table tr td:nth-child(2)').items()      # css选择器很不好用
        # ip = doc('table tr:gt(1) td:eq(1)')  # jQuery选择器很好用
        # port = doc('table tr:gt(1) td:eq(2)')
        # ip_list = [i.text() for i in ip.items()]  # 直接列表推倒式获取
        # port_list = [i.text() for i in port.items()]
        # yield {k: v for k, v in zip(ip_list, port_list)}

        # xpath方法
        html = etree.HTML(response)
        # result = html.xpath('//table/tr/td[position()<4 and position()>1]/text()')
        ip = html.xpath('//table/tr/td[2]/text()')
        ip_list = [i for i in ip]
        port = html.xpath('//table/tr/td[3]/text()')
        port_list = [i for i in port]
        yield {k: v for k, v in zip(ip_list, port_list)}


def main():
    for i in get_page():
        for k, v in i.items():
            print(k, v)


if __name__ == '__main__':
    main()
