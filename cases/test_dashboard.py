# coding:utf-8

import unittest
from framework.logger import Logger
from pages.dashboard_page import DashBoardPage
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage

logger = Logger('LinkSkip').getlog()


class LinkSkip(unittest.TestCase):
    """Dashboard页面测试"""
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        cls.driver.implicitly_wait(10)
        loginpage = LoginPage(cls.driver)
        loginpage.type_username('18811133471')
        loginpage.type_pwd('1234qwer')
        loginpage.click_but('登录')
        loginpage.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        dashpage = DashBoardPage(cls.driver)
        dashpage.quit_browser()

    def test_1_have_tips(self):
        dashpage = DashBoardPage(self.driver)
        try:
            last_login_tip = dashpage.get_tip_last_login().text
            logger.info(last_login_tip)
            self.assertIn('您的账号', last_login_tip)
            logger.info('检测到上次登录的提示框')
            print('检测到上次登录的提示框')
        except AssertionError as e:
            logger.error('未检测到上次登录的提示框，err：% s' % e)
            print('未检测到上次登录的提示框，err：% s' % e)
        try:
            change_pwd_tip = dashpage.get_tip_change_pwd()
            logger.info(change_pwd_tip.text)
            self.assertIn('您的密码', change_pwd_tip.text)
            print('检测到修改密码的提示框！')
        except Exception as e:
            print('未检测到修改密码的提示框！err：% s' % e)

    def test_2_close_tip_last_login(self):
        dashpage = DashBoardPage(self.driver)
        try:
            dashpage.close_tip_last_login()
            self.assertFalse(self, dashpage.get_tip_last_login())
            logger.info('上次登录提示关闭成功！')
            print('上次登录提示关闭成功！')
        except AssertionError as e:
            logger.error('上次登录提示关闭失败！')
            print('上次登录提示关闭失败！')

    def test_3_close_tip_change_pwd(self):
        dashpage = DashBoardPage(self.driver)
        try:
            dashpage.close_tip_change_pwd()
            self.assertFalse(self, dashpage.get_tip_change_pwd())
            logger.info('修改密码提示关闭成功！')
            print('修改密码提示关闭成功！')
        except AssertionError as e:
            logger.error('修改密码提示关闭失败！')
            print('修改密码提示关闭失败！')
