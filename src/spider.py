#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午9:05
# @Author  : Jason
# @File    : spider.py
from selenium import webdriver


class SpiderTask(object):
    def __init__(self, url, is_article=True):
        self.init_driver()
        self.__content = None
        if is_article:
            self.article_spider(url)
        else:
            pass

    @staticmethod
    def init_driver(use_chrome=False):
        if use_chrome:
            return webdriver.Chrome()
        else:
            return webdriver.PhantomJS()

    def article_spider(self, url):
        driver = self.init_driver()
        driver.get(url)
        element = driver.find_element_by_xpath(".//*[@class='RichText PostIndex-content av-paddingSide av-card']")
        self.__content = element.get_attribute('innerHTML')

    def get_content(self):
        return self.__content
