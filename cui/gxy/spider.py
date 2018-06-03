#!/usr/bin/env python
# -*-coding:utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

# browser = webdriver.Chrome()
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser.set_window_size(1400, 900)

wait = WebDriverWait(browser, 10)


def search():
    browser.get('https://www.gxyclub.com')

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ink_con a"))
    )

    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.select('#ink_con a')[0].select('span')[0].get_text())
    for item in soup.select('#ink_con a'):
        # print(item.find_all('span'))

        borrow_name_html = item.find_all('span')[0].get_text()
        borrow_name = re.sub('\s', '', borrow_name_html)
        borrow_list = {
            'borrow_name': borrow_name,
            'borrow_money': item.find_all('span')[1].get_text(),
            'borrow_time': item.find_all('span')[2].get_text(),
        }
        print(borrow_list)

search()
