# !/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:11
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : run.py
# @Software: PyCharm
from Base.base import Base
from PageObject.elem_params import Register_page_elem


# 封装速涡手游加速器注册页面操作对象及各个元素及操作方法
class Register_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.elem_locator = Register_page_elem()

    def get_username_attribute_value(self):
        """
            获得账号输入框的placeholder值
        @return: 获得账号输入框的placeholder值
        """
        elem = self.elem_locator.get_locator("Username")
        return super().get_placeholder(elem)

    def get_password_attribute_value(self):
        """
            获得密码输入框的placeholder值
        @return: 获得密码输入框的placeholder值
        """
        elem = self.elem_locator.get_locator("Password")
        return super().get_placeholder(elem)

    def get_code_attribute_value(self):
        """
            获得验证码输入框的placeholder值
        @return: 获得验证码输入框的placeholder值
        """
        elem = self.elem_locator.get_locator("code")
        return super().get_placeholder(elem)

    def find_button_other_register(self):
        """
            查找海外注册按钮
        @return: 海外注册按钮文本值
        """
        elem = self.elem_locator.get_locator("InputWarningA")
        return super().get_text(elem)

    def find_button_register(self):
        """
            查找注册按钮
        @return: 注册按钮文本值
        """
        elem = self.elem_locator.get_locator("RegisterBtn")
        return super().get_text(elem)

    def find_button_login(self):
        """
            查找登录按钮文本值
        @return: 登录按钮文本值
        """
        elem = self.elem_locator.get_locator("登录")
        return super().get_text(elem)

    def find_button_code(self):
        """
            查找验证码按钮文本值
        @return: 验证码按钮文本值
        """
        elem = self.elem_locator.get_locator("RegisterSendCode")
        return super().get_text(elem)

    def click_other_register_btn(self):
        """
            点击海外用户注册登录按钮
        """
        elem = self.elem_locator.get_locator("海外用户注册")
        super().click_btn(elem)

    def check_page_is_other_page(self):
        """
            海外用户登录界面检查，检查select元素是否存在
        @return: TRUE/FALSE
        """
        elem = self.elem_locator.get_locator("country-code")
        return super().check_select_is_existence(elem)

    def click_login_btn(self):
        """
            登录按钮点击
        """
        elem = self.elem_locator.get_locator("登录")
        super().click_btn(elem)

    def get_login_page_title(self):
        """
            获取登录页面的title
        @return: title
        """
        elem = self.elem_locator.get_locator("InputTitleText")
        return super().get_text(elem)

    def click_register_btn(self):
        """
            点击注册按钮
        """
        elem = self.elem_locator.get_locator("RegisterBtn")
        super().click_btn(elem)

    def click_code_btn(self):
        """
            点击发送验证码按钮
        """
        elem = self.elem_locator.get_locator("发送验证码")
        super().click_btn(elem)

    def get_error_text(self):
        """
            获得输入框输入错误的返回信息
        @return: 获得输入框输入错误的返回信息
        """
        elem = self.elem_locator.get_locator("error_return")
        return super().get_text(elem)

    def username_send_keys(self, value):
        """
            输入账号输入框的值
        @param value: value
        """
        elem = self.elem_locator.get_locator("Username")
        super().send_key(elem, value)

    def password_send_keys(self, value):
        """
            输入密码输入框的值
        @param value: value
        """
        elem = self.elem_locator.get_locator("Password")
        super().send_key(elem, value)

    def code_send_keys(self, value):
        """
            输入验证码输入框的值
        @param value: value
        """
        elem = self.elem_locator.get_locator("Password")
        super().send_key(elem, value)
