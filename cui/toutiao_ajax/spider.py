#!/usr/bin/env python
# -*-coding:utf-8 -*-
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests
import os
from hashlib import md5
import re


def get_page(offset):
    """获取指定offset的response.json"""
    data = {
        'offset': offset,
        "format": "json",
        'keyword': '街拍',
        "autoload": "true",
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
    }

    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response.json())
            return response.json()      # 将结果转换为json格式返回
    except RequestException:
        return 'get_page - RequestException....'


def get_images(json):
    """解析服务器返回json， 返回多个标题、图片url的字典"""
    if json.get('data'):
        for item in json.get('data'):           # 循环第一页（没有滚屏），xhr的data
            title = item.get('title')           # title有可能为空！
            images = item.get('image_list')     # images有可能为空！
            if images:
                for image in images:
                    img_url = image.get('url')
                    img_url = re.sub('^//', 'http://', img_url)
                    if title:
                        yield {
                            'title': title,
                            'image': img_url,
                        }


def save_img(item):
    """传入解析后的json（包含标题、图片url的字典），下载存储"""
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('already down...', file_path)
        else:
            print(response.status_code, 'response.status_code')
    except RequestException:
        print('requests exception in save_img func...')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_img(item)


if __name__ == '__main__':

    main(20)