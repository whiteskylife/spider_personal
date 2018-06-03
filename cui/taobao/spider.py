#!/usr/bin/env python
# -*-coding:utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from pyquery import PyQuery as pq
from config import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

# browser = webdriver.Chrome()
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
browser.set_window_size(1400, 900)  # 调整窗口到合适爬取的大小
wait = WebDriverWait(browser, 10)


def search(value):
    """输入查询内容，返回页码"""
    print('in search function... ')
    try:
        browser.get('https://www.taobao.com')
        # 输入框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        # 提交操作
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        input.send_keys(value)
        submit.click()
        total_page = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total_page.text
    except TimeoutException:
        return search()


def next_page(page_number):
    print('正在翻页:', page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        # 判断是否跳转到page_number页, 每做一次页面动作都要检测是否操作成功
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'shop_url': item.find('.pic .pic-link').attr('data-href'),
            'price': item.find('.price').text().replace('\n', ''),
            # 'deal': item.find('.deal-cnt').text()[:-3]
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text(),
            'image': item.find('.pic .img').attr('data-src'),
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MongoDB成功', result)
    except Exception:
        print('存储MongoDB失败')


def main():
    try:
        total_page = search(SEARCH_CONTENT)
        total_page = int(re.compile('(\d+)').search(total_page).group(1))  # 获取总页码
        for i in range(2, total_page + 1):
            next_page(i)
    except Exception:
        print('出错了....')
    finally:
        browser.close()


if __name__ == '__main__':
    main()
