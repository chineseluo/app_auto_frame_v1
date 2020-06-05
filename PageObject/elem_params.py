# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm

import os
from Common.publicMethod import PubMethod
import logging
from selenium.webdriver.common.by import By

pub_api = PubMethod()
root_dir = os.path.dirname(os.path.dirname(__file__))
config_path = os.path.join(root_dir, 'PageObject')
config_path = os.path.abspath(config_path)


class Elem_params:
    def __init__(self, dir_name, file_name, root_dir_name=config_path):
        self.elem_name = []
        self.desc = []
        self.data = []
        self.info = []
        self.__run(dir_name, root_dir_name, file_name)

    def __run(self, dir_name, root_dir_name, file_name):
        config_dir_name = os.path.join(root_dir_name, dir_name)
        file_path = os.path.abspath(os.path.join(config_dir_name, file_name))
        try:

            self.info = PubMethod().read_yaml(file_path)['parameters']
            for i in self.info:
                self.elem_name.append(i['elem_name'])
                self.desc.append(i['desc'])
                self.data.append(i['data'])
        except Exception as e:
            logging.error("文件解析失败！{},文件路径：{}".format(e, file_path))

    def get_locator(self, elem_name):
        """

        @param page_elem_class:传入页面元素对象
        @param elem_name:传入自定义的元素名称
        @return:
        """
        page_obj_elem = self.info
        elems_info = page_obj_elem
        for item in elems_info:
            if item["elem_name"] == elem_name:
                method = item["data"]["method"]
                value = item["data"]["value"]
                logging.info("元素名称为：{}，元素定位方式为：{}，元素对象值为：{}".format(elem_name, method, value))
                if method == "ID" and value is not None:
                    elem_locator = (By.ID, value)
                    return elem_locator
                elif method == "XPATH" and value is not None:
                    elem_locator = (By.XPATH, value)
                    return elem_locator
                elif method == "LINK_TEXT" and value is not None:
                    elem_locator = (By.LINK_TEXT, value)
                    return elem_locator
                elif method == "PARTIAL_LINK_TEXT" and value is not None:
                    elem_locator = (By.PARTIAL_LINK_TEXT, value)
                    return elem_locator
                elif method == "NAME" and value is not None:
                    elem_locator = (By.NAME, value)
                    return elem_locator
                elif method == "TAG_NAME" and value is not None:
                    elem_locator = (By.TAG_NAME, value)
                    return elem_locator
                elif method == "CLASS_NAME" and value is not None:
                    elem_locator = (By.CLASS_NAME, value)
                    return elem_locator
                elif method == "CSS_SELECTOR" and value is not None:
                    elem_locator = (By.CSS_SELECTOR, value)
                    return elem_locator
                else:
                    logging.error("元素名称：{}，此元素定位方式异常，定位元素值异常，请检查！！！".format(elem_name))


# 注册yaml文件对象
class Login_page_elem(Elem_params):
    def __init__(self):
        super(Login_page_elem, self).__init__('Login_page', 'Login_page.yaml')


class Buy_page_elem(Elem_params):
    def __init__(self):
        super(Buy_page_elem, self).__init__('Buy_page', 'Buy_page.yaml')


class Register_page_elem(Elem_params):
    def __init__(self):
        super(Register_page_elem, self).__init__('Register_page', 'Register_page.yaml')


if __name__ == '__main__':
    login_page = Login_page_elem()
