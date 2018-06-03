#!/usr/bin/env python
# -*-coding:utf-8 -*-
from bs4 import BeautifulSoup

html = '''
<html xmlns="http://www.w3.org/1999/xhtml">
    <head> 
        <base href="https://www.gxyclub.com/"/>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <meta http-equiv="pragma" content="no-cache">
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="expires" content="0">
        <title>共信赢</title>
        <script type="text/javascript" src="statics/front/js/index/gxy-main.js"></script>
       	<script type="text/javascript" src="statics/front/js/index/web-master.js"></script>
    </head>
    <body>
		
'''

soup = BeautifulSoup(html, 'lxml')
a = soup.select('title')[0].get_text()
print(a)
print(type(a))