#!/usr/bin/env python
# -*-coding:utf-8 -*-

import requests
import json
import pymongo
from lxml import etree
from urllib.parse import urlencode

COUNT = 0
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}


def get_index(page):
    start_url = 'https://www.huya.com/cache.php?'
    params = {
        'm': 'LiveList',
        'do': 'getLiveListByPage',
        'gameId': 2793,
        'tagAll': 0,
        'page': page,
    }
    response = requests.get(start_url, headers=headers, params=urlencode(params))
    if response.status_code == 200:
        parse_data(response.json())


def parse_data(response):
    result = response.get('data')
    for item in result.get('datas'):
        avata = {
            'avatar_url': item.get('avatar180'),
            'introduction': item.get('introduction'),
            'bluRayMBitRate': item.get('bluRayMBitRate'),
            'channel': item.get('channel'),
            'gameFullName': item.get('gameFullName'),
            'roomName': item.get('roomName'),
            'screenshot': item.get('screenshot'),
            'popularity': item.get('totalCount'),
        }
        save_to_mongo(avata)


client = pymongo.MongoClient('192.168.1.110')
db = client['huya_live']
collection = db['huya_绝地求生']


def save_to_mongo(data):
    if collection.insert(data):
        global COUNT
        print('第 %s 条信息存储到MongoDB成功！' % COUNT)
        COUNT += 1


def main(page):
    for num in range(0, page + 1):
        get_index(num)


if __name__ == '__main__':
    main(14)
