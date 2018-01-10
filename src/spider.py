#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午9:05
# @Author  : Jason
# @File    : spider.py
from selenium import webdriver


class SpiderTask(object):
    def __init__(self, url, is_article=True):
        self.driver = None
        self.init_driver()
        self.content = None
        if is_article:
            self.article_spider(url)
        else:
            pass

    def init_driver(self, use_chrome=False):
        if use_chrome:
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.PhantomJS()

    def article_spider(self, url):
        pass
