#!/usr/bin/env python
# -*-coding:utf-8 -*-
from urllib.parse import urlencode
from requests.exceptions import ConnectionError, ReadTimeout
import requests
from pyquery import PyQuery as pq
import time
import random
import re
import pymongo
from config import *

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

base_url = 'http://weixin.sogou.com/weixin?'
# keyword = '风景'
headers = {
    # 'Cookie': 'CXID=89760980C4A6BCB95E534B89346286BD; SUID=7D275A713565860A5AE07E1D000A4E2E; ad=CGiNsZllll2zc4cNlllllV7a7WGllllltqoXKyllll9lllll44Dll5@@@@@@@@@@; SUV=1527849575213910; ABTEST=0|1527849586|v1; weixinIndexVisited=1; SUIR=4B38446C1E18708C2EFE8CAB1E74A95C; PHPSESSID=mv2m3p6jb6ci9sj0kbj3u3ivr5; sct=3; JSESSIONID=aaaVul0-MH5RWbkG18jnw; SNUID=D2ADD2F9888DEA26F039563688217C25; IPLOC=CN4403; ppinf=5|1527922535|1529132135|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTozNjolRTUlOUIlOUUlRTUlQkYlODYlRTYlOUMlQUElRTYlOUQlQTV8Y3J0OjEwOjE1Mjc5MjI1MzV8cmVmbmljazozNjolRTUlOUIlOUUlRTUlQkYlODYlRTYlOUMlQUElRTYlOUQlQTV8dXNlcmlkOjQ0Om85dDJsdUFKemRPU01ueVkzWUlpbXpMSldtOEFAd2VpeGluLnNvaHUuY29tfA; pprdig=Y0Gq1u4mIcy5UbP_8WjrZsuiVtaonC29lbKL-JLdtQ7mXcwgjKthbx4R57Gc6A0Ouy2wU4PrjxhKwOtj8W5P9yRjgredNUi_6q6FolKgQstk3exMnan4tKg-UUQxUiXU-OJE9x218Fl4OgEZmyqzbxfcCDP5_WB3WBBOPt-OBNk; sgid=10-35332799-AVsSP2cJW6y0CC4lQt4NYCc; ppmdig=1527922535000000c428920123d91e7982d1c9df218de4d0',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}

proxy = None


def get_proxy():
    """通过接口获取代理池中的代理"""
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print(response.text, 'in get_proxy-------------------------')
            return response.text
        print('代理请求出错,,,')
        return None
    except ConnectionError:
        return None


def parse_200(result):
    doc = pq(result)
    content = doc('.header .other .s1').text()
    # pattern = re.compile('window.location.href\s=\s"(.*?)".*?apk"', re.S)
    # ret = re.search(pattern, result).group()

    if content == '您的访问出错了':
        return False
    # elif ret:
    #     return False
    else:
        return True


def get_html(url, count=1):
    '''
    :param url:
    :param count: 失败请求次数
    :return:
    '''
    print('Crawling ', url)
    print('Trying Count ', count)

    global proxy
    if count >= MAX_COUNT:  # max_count全局变量不修改不需声明
        print('Tried Too Many Counts-----------------------------------------------------')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            print('使用代理 %s  请求' % proxies)
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies, timeout=2)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        print('response status_code: ', response.status_code)
        if response.status_code == 200:
            # return response.text
            if parse_200(response.content.decode('utf-8')):
                # print(response.content.decode('utf-8'))
                return response.content.decode('utf-8')
            else:
                print(response.content.decode('utf-8'))
                print(' 200访问限制:‘您的访问出错’开始使用代理')
                proxy = get_proxy()
                print('当前代理：%s' % proxy)
                return get_html(url)

        if response.status_code == 302:
            # Proxy
            print('302-------------')
            proxy = get_proxy()
            if proxy:
                print('Using Proxy: ', proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed------------')
                return None
        else:
            print('other status_code:', response.status_code)
            proxy = get_proxy()
            return get_html(url)

    except ConnectionError as e:
        print('Error Occurred', e.args)
        proxy = get_proxy()  # 异常时尝试更换代理
        print('代理连接出错，切换代理...swith proxy')
        count += 1
        return get_html(url, count)
    except ReadTimeout as e:
        print('代理超时，切换代理：proxy timeout ', e.args)
        proxy = get_proxy()
        return get_html(url)
    except Exception as e:
        print('other exception:', e)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        return None
    except ConnectionError:
        return None


def get_tiltle(html):
    try:
        pattern = re.compile('document.write.*?>(.*?)</span>', re.S)
        ret = re.search(pattern, html).group(1)
        if ret:
            return ret
        else:
            return None
    except Exception as e:
        print(e)
        return None


def get_date(html):
    try:
        pattern = re.compile('var.publish_time.=."(.*?)".\|\|', re.S)
        ret = re.search(pattern, html).group(1)
        if ret:
            return ret
        else:
            return None
    except Exception as e:
        print(e)
        return None


def parse_detail(html, article_url):
    doc = pq(html)
    title = get_tiltle(html)
    content = doc('.rich_media_content').text()
    date = get_date(html)
    nickname = doc('#profileBt a').text()
    wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
    return {
        'title': title,
        'content': content,
        'date': date,
        'nickname': nickname,
        'wechat': wechat,
        'article_url': article_url,
    }


def main():
    for page in range(1, 11):
        sleep_time = random.choice([i for i in range(1, 5)])
        time.sleep(sleep_time)
        html = get_index(KEYWORD, page)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                article_html = get_detail(article_url)
                # print(article_url, '页码：', page)
                if article_html:
                    article_data = parse_detail(article_html, article_url)
                    print(article_data)
                    save_to_mongo(article_data)
    print('全部请求结束--------')


def save_to_mongo(data):
    if db[MONGO_TABLE].update({'title': data['title']}, {'$set': data}, True):  # 不存在则插入MongoDB，存在则更新
        print('Save to Mongo', data['title'])
    else:
        print('Failed save to Mongo! ', data['title'])


if __name__ == '__main__':
    main()
