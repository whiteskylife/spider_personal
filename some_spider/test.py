#!/usr/bin/env python
# -*-coding:utf-8 -*-
import json
import datetime
import pymongo

# client = pymongo.MongoClient('mongodb://192.168.1.110:27017')
client = pymongo.MongoClient('mongodb://whisky:123456@192.168.1.110:27017/whisky')
db = client.whisky  # 等同于：client.['whisky']

# 查看库下所有的集合
# print(db.collection_names(include_system_collections=False))

# 创建集合
table_user = db['userinfo']  # 等同于：db.userinfo
# print(table_user)

# 插入文档

user0 = {
    "_id": 1,
    "name": "clex",
    "birth": datetime.datetime.now(),
    "age": 10,
    'hobbies': ['music', 'read', 'dancing'],
    'addr': {
        'country': 'China',
        'city': 'BJ'
    }
}

user1 = {
    "_id": 2,
    "name": "blex",
    "birth": datetime.datetime.now(),
    "age": 10,
    'hobbies': ['music', 'read', 'dancing'],
    'addr': {
        'country': 'China',
        'city': 'weifang'
    }
}
# res = table_user.insert_many([user0, user1]).inserted_ids
# print(res)
# print(table_user.count())


# 查找
from pprint import pprint       # 格式化
# pprint(table_user.find_one({'name': 'blex'}))
# for item in table_user.find():
#     pprint(item)

# pprint(table_user.find_one({"_id": {"$gte": 1}, "name": 'blex'}))


# 更新
# table_user.update({'_id': 1}, {'name': 'EGON'})
# pprint((table_user.find_one({"_id": {"$gte": 1}, "name": "blex"})))


# 传入新的文档替换旧的文档  会把userinfo这个collection中的所有其他数据清空，只换成下面两个
table_user.save(
    {
        "_id": 2,
        "name": 'egon_xxxxxxxxxxxxxx    '
    }
)