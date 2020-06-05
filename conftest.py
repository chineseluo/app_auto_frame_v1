# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 9:15
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
import logging
from appium import webdriver
from Common.publicMethod import PubMethod

selenium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "appium_config.yaml")
selenium_config = PubMethod.read_yaml(selenium_config_path)


# 定义钩子函数hook进行测试用例name和_nodeid输出
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        logging.info(item.name)
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")
        logging.info(item._nodeid)


