#!/usr/bin/env python
# -*-coding:utf-8 -*-
import requests
import time




def get_code(num):
    for i in range(num):
        base_url = 'https://www.gxyclub.com/getAuthCode'
        response = requests.get(base_url).content
        write_to_file(response)


def write_to_file(content):
    file_name = str(time.time() * 1000) + '.jpg'
    with open(file_name, 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    get_code(3)