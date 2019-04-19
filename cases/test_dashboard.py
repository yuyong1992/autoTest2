# coding:utf-8

import unittest
from framework.logger import Logger
from pages.dashboard_page import DashBoardPage
from framework.browser_engine import BrowserEngine
from pages.login_page import LoginPage

logger = Logger('DashboardPage').getlog()


class CloseTipOfLastLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        cls.driver.implicitly_wait(10)
        loginpage = LoginPage(cls.driver)
        loginpage.type_username('18811133441')
        loginpage.type_pwd('1234qwer')
        loginpage.click_but('登录')
        loginpage.sleep(3)

    @classmethod
    def tearDownClass(cls):
        dashpage = DashBoardPage(cls.driver)
        dashpage.quit_browser()

    def test_close_tip(self):
        dashpage = DashBoardPage(self.driver)
        dashpage.close_tip_last_login()

    def test_select_product(self):
        dashpage = DashBoardPage(self.driver)
        dashpage.product_select('rubico')
        dashpage.sleep(1)