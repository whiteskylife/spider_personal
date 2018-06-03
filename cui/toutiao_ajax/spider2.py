#!/usr/bin/env python
# -*-coding:utf-8 -*-
from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import requests
import json
import os
from hashlib import md5
import re
from config import *
import pymongo
from json.decoder import JSONDecodeError
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}


def get_page_index(offset, keyword):
    """获取指定offset的response.json"""
    data = {
        'offset': offset,
        "format": "json",
        'keyword': keyword,
        "autoload": "true",
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery',
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
            # return response.json()      # 将结果转换为json格式返回
        else:
            print('request failed ...')
    except RequestException:
        return 'get_page - RequestException....'


def parse_page_index(response):
    """返回article_url"""
    try:
        data = json.loads(response)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError as e:
        print(e)
        pass

def get_page_detail(url):
    try:
        print('请求详情页')
        response = requests.get(url, headers=headers, allow_redirects=True)  # allow_redirects允许跳转参数
        if response.status_code == 200:
            return response.text
        else:
            print('请求详情页出错', url)
            return None
    except RequestException:
        print('请求详情页出错', url)
        return None


def parse_page_detail(html, url):
    print('分析详情页', url)
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    img_pattern = re.compile('gallery: JSON.parse\((.*?)\),', re.S)  # 注意，需要转义
    out = re.search(img_pattern, html)
    if not out:return
    result = out.group(1)
    if result:
        try:
            # print(type(result), result)     # result是正则过滤服务器响应后得到的字符串
            data = json.loads(result)
            data = json.loads(data)  # loads两次才能转换为字典
            # print(type(data), data)
            if data and 'sub_images' in data.keys():
                sub_img = data.get('sub_images')
                imgs = [item.get('url') for item in sub_img]  # item是包含url的字典
                for img in imgs: download_img(img)
                return {
                    'title': title,
                    'url': url,
                    'images': imgs,
                }
        except JSONDecodeError as e:
            print(e, title, url)
    else:
        print('详情页数据获取失败...')

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
collection = db[MONGO_TABLE]


def save_to_mongo(result):
    if collection.insert(result):
        print('存储到MongoDB成功', result)
        return True
    return False


def download_img(url):
    """下载图片"""
    print('正在下载', url)
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)      # allow_redirects允许跳转参数
        if response.status_code == 200:
            save_img(response.content)  # text返回字符串，content返回二进制内容
        return None
    except RequestException:
        print('请求图片', url)
        return None


def save_img(content):
    file_path = '{0}/{1}.{2}'.format('img', md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            if result: save_to_mongo(result)


if __name__ == '__main__':
    print('-----------')
    groups = [x * 20 for x in range(START_PAGE, STOP_PAGE + 1)]
    p = ThreadPoolExecutor(20)
    try:
        p.map(main, groups)
    except AttributeError as e:
        print(e)
        pass
    except Exception as error:
        print(error)
    # p.close()
    # p.join()

# 请求返回结果不全，尝试添加allow_redirects允许跳转参数 ， response = requests.get(url, headers=headers, allow_redirects=True)
# 写正则时注意转义特殊字符，re.compile('gallery: JSON.parse\((.*?)\),', re.S)  # 注意，需要转义
# 反爬：json字符串问题, https://www.cnblogs.com/yum777/articles/9090391.html