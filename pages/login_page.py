# coding:utf-8

import os
import sys
sys.path.append(os.path.dirname(__file__))
from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger('LoginPage').getlog()


class LoginPage(BasePage):
    """
    登录页面对象
    """
    path_mobile = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/input'
    path_pwd = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/input'
    path_but = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[4]'
    path_welcome = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/h4'
    path_err_login = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[4]/p'
    path_err_mobile = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/div'
    path_err_pwd = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div[2]'

    def type_username(self, mobile):
        self.type(self.path_mobile, mobile)

    def type_pwd(self, pwd):
        self.type(self.path_pwd, pwd)

    def click_but(self, but_name='登录', path_button=path_but):
        self.click(path_button, but_name)

    def get_err_msg(self):
        err_msg = self.find_element(self.path_err_login)
        return err_msg.text

    def confirm_login_page(self):
        try:
            assert '欢迎登录' in self.find_element(self.path_welcome).text
            logger.info('已进入登录页面！')
        except AssertionError as e:
            logger.info('登录页面加载失败：%s ' % e)
            print('登录页面加载失败：%s ' % e)
            raise AssertionError

    def get_attr(self, attr_name, selector):
        try:
            attr = self.find_element(selector).get_attribute(attr_name)
            return attr
        except Exception as e:
            logger.info("获取元素属性异常！err：%s" % e)

    def back_browser(self):
        self.back()
