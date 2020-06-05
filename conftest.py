# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 9:15
# @Author  : luozhongwen
# @Email   : luozw@inhand.com.cn
# @File    : conftest.py
# @Software: PyCharm
import os
import pytest
import logging
from selenium import webdriver
from selenium.webdriver import Remote
from Common.publicMethod import PubMethod
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.firefox.options import Options as FO
from selenium.webdriver.ie.options import Options as IEO


selenium_config_path = os.path.join(os.path.dirname(__file__), "Conf", "selenium_config.yaml")
selenium_config = PubMethod.read_yaml(selenium_config_path)


# 定义钩子函数hook进行命令行定义浏览器传参，默认chrome,定义浏览器启动方式传参，默认启动
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser option: firefox or chrome or ie")
    parser.addoption("--browser_opt", action="store", default="open", help="browser GUI open or close")


# 定义钩子函数hook进行测试用例name和_nodeid输出
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        logging.info(item.name)
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode_escape")
        logging.info(item._nodeid)


@pytest.fixture(scope="function")
def function_driver(request):
    browser = request.config.getoption("--browser")
    browser_opt = request.config.getoption("--browser_opt")
    print("获取命令行传参：{}".format(request.config.getoption("--browser")))
    # 是否开启浏览器设置，根据命令行传参，browser_opt判断，默认open
    if browser_opt == "open":
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "ie":
            driver = webdriver.Ie()
        else:
            logging.info("发送错误浏览器参数：{}".format(browser))
    else:
        if browser == "chrome":
            chrome_options = CO()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == "firefox":
            firefox_options = FO()
            firefox_options.add_argument('--headless')
            driver = webdriver.Firefox(firefox_options=firefox_options)
        elif browser == "ie":
            ie_options = IEO()
            ie_options.add_argument('--headless')
            driver = webdriver.Ie(ie_options=ie_options)
        else:
            logging.info("发送错误浏览器参数：{}".format(browser))
    yield driver
    # driver.close()
    driver.quit()


@pytest.fixture(scope="function")
def function_remote_driver(request):
    browser = request.config.getoption("--browser")
    print("获取命令行传参：{}".format(request.config.getoption("--browser")))
    driver = Remote(command_executor=selenium_config["selenium_hub_url"],
                    desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                          'javascriptEnabled': True})
    yield driver
    # driver.close()
    driver.quit()
