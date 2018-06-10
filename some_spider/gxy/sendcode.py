#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
from urllib.parse import urlencode

base_url = 'https://www.gxyclub.com/sendMsgCode'

data = {
    'mobilePhone': 13069647090,
    'authCode': 1616,
}

def req_api():
    ret = requests.post(
        url=base_url,
        data=data,
        cookies={
            'aliyungf_tc': 'AQAAAP+z6gTpdwoANyZacfSBNRHQh/qv',
            'gr_user_id': '89a68517-3ee6-47e2-99a9-1a3df2dd17a4',
            'acw_tc': 'AQAAAN6Pcm6DDgsANyZacf2OZTByQk5W',
            'gr_session_id_8bafc438baad40f1': '0d2a4c16-acbe-45a1-9c4f-dc2dd8e1fbd1_true',
            'SESSION': 'e104beb9-a756-4a6d-8c60-19f946d26599',
        })

    print(ret.text)

req_api()
