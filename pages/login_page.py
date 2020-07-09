# coding:utf-8

import os
import sys
sys.path.append(os.path.dirname(__file__))
from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger('LoginPage').getlog()


class LoginPage(BasePage):
    # 手机号输入框位置
    path_username = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/input'
    # 密码输入框位置
    path_pwd = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/input'
    # 手机号报错信息位置
    path_err_phone = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/div'
    # 密码报错信息位置
    path_err_pwd = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div[2]'
    # 后台报错信息位置
    path_err_backend = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[4]/p'
    # 登录按钮位置
    path_but_login = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[4]'
    # 展示/隐藏密码按钮位置
    path_display_pwd = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/div[1]/i'

    # 输入手机号
    def type_username(self, username):
        self.clear(self.path_username)
        self.type(self.path_username, username, input_name='手机号')

    # 输入密码
    def type_pwd(self, pwd):
        self.clear(self.path_pwd)
        self.type(self.path_pwd, pwd, input_name='密码')

    # 点击登录按钮
    def click_login(self):
        self.click(self.path_but_login, but_name='登录')

    # 点击展示/隐藏密码按钮
    def click_display_pwd(self):
        self.click(self.path_display_pwd, '展示/隐藏密码')

    # 点击登录页面上的链接
    def click_link(self, path_link, name_link):
        self.click(path_link, name_link)

    # 获取页面上手机号输入框的错误信息
    def get_err_phone(self):
        err_msg_phone = self.find_element(self.path_err_phone)
        return err_msg_phone.text

    # 获取页面上密码输入框的错误信息
    def get_err_pwd(self):
        err_msg_pwd = self.find_element(self.path_err_pwd)
        return err_msg_pwd.text
    # 获取后台报错时页面上展示的错误信息

    def get_err_backend(self):
        err_msg_backend = self.find_element(self.path_err_backend)
        return err_msg_backend.text

    # 用登录页面上的文字确认是否进入登录页面
    def confirm_login_page(self):
        path_welcome = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/h4'
        try:
            assert '欢迎登录' in self.find_element(path_welcome).text
            logger.info('已进入登录页面！')
        except AssertionError as e:
            logger.info('登录页面加载失败：%s ' % e)
            print('登录页面加载失败：%s ' % e)
            raise AssertionError

    # 获取当前元素的某个属性的值
    def get_attr(self, attr_name, selector):
        try:
            attr = self.find_element(selector).get_attribute(attr_name)
            return attr
        except Exception as e:
            logger.info("获取元素属性异常！err：%s" % e)

    def back_browser(self):
        self.back()
