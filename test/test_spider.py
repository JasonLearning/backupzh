#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 下午9:11
# @Author  : Jason
# @File    : test_spider.py

import unittest
from src.spider import SpiderTask
from src.parse import Tomd


class TestSpider(unittest.TestCase):
    def test_init(self):
        s = SpiderTask('https://zhuanlan.zhihu.com/p/28370944')
        self.assertIsNotNone(s.get_content())
        # print(s.get_content())
        print(Tomd(s.get_content()).markdown)
