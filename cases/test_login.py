# coding:utf-8

import unittest
import ddt
from pages.login_page import LoginPage
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from tools.models import excel_to_dic

logger1 = Logger("LoginSuccess").getlog()
logger2 = Logger("LoginErrPhone").getlog()
logger3 = Logger("LinkClick").getlog()
# 测试数据文件
file_path = "E:\Desktop\\testdata_login.xlsx"

# 获取正确的手机号、密码数据
file_sheetname = "correct"
correct_exl = excel_to_dic.ExcelToDic(file_path, file_sheetname)
correct_data = correct_exl.excel_to_dic()
# 获取手机号错误的登录测试数据
err_phone_sheetname = "err_phone"
err_phone_exl = excel_to_dic.ExcelToDic(file_path, err_phone_sheetname)
err_phone_data = err_phone_exl.excel_to_dic()
# 获取密码错误的测试数据
err_pwd_sheetname = "err_pwd"
err_pwd_exl = excel_to_dic.ExcelToDic(file_path, err_pwd_sheetname)
err_pwd_data = err_pwd_exl.excel_to_dic()
# 获取后台报错的测试数据
err_backend_sheetname = "err_backend"
err_backend_exl = excel_to_dic.ExcelToDic(file_path, err_backend_sheetname)
err_backend_data = err_backend_exl.excel_to_dic()
# 获取链接点击的测试数据
link_click_sheetname = "link_click"
link_click_exl = excel_to_dic.ExcelToDic(file_path, link_click_sheetname)
link_click_data = link_click_exl.excel_to_dic()

# test_data = [
#         {"用例名": "手机号错误-中文", "username": "中文的手机号", "pwd": "1234qwer", "path_err_msg": "xpath=>/html/body/div[3]/p"},
#         {"用例名": "手机号错误-少于11位数字", "username": "1881234", "pwd": "1234qwer", "path_err_msg": "xpath=>/html/body/div[3]/p"},
#         {"用例名": "手机号错误-英文", "username": "qwertqwertqw", "pwd": "1234qwer", "path_err_msg": "xpath=>/html/body/div[3]/p"}
#     ]


@ddt.ddt
class LoginSuccess(unittest.TestCase):
    # 登录成功的测试

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self, test_server='inServer')

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*correct_data)
    def test_1_login_success(self, data):
        """登录成功"""
        loginpage = LoginPage(self.driver)
        loginpage.confirm_login_page()
        # print("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        logger1.info("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        loginpage.wait(2)
        loginpage.type_username(data["username"])
        loginpage.type_pwd(data["pwd"])
        loginpage.click_login()
        loginpage.wait(10)
        try:
            self.assertIn(loginpage.get_page_title(), data["assert"])
            # print('%s Login Test Pass!' % data["username"])
            logger1.info('断言成功，%s 登录成功!' % data["username"])
            logger1.info('--------------------')
            # loginpage.driver.quit()
        except AssertionError as e:
            logger1.error('断言失败，%s 登录失败！ err: %s' % (data["username"], e))
            loginpage.get_windows_img()
            logger1.info('--------------------')
            # print('断言失败! err: %s' % e)
            raise AssertionError


@ddt.ddt
class LoginErr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, test_server='inServer')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.data(*err_phone_data)
    def test_2_login_err_phone(self, data):
        """手机号格式错误"""

        loginpage = LoginPage(self.driver)
        loginpage.confirm_login_page()
        # print("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        logger2.info("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        loginpage.type_username(data["username"])
        loginpage.type_pwd(data["pwd"])
        loginpage.click_login()
        err_msg = loginpage.get_err_phone()
        try:
            self.assertEqual(err_msg, data["assert"])
            logger2.info("断言成功，提示正确")
            logger2.info('--------------------')
            # print("断言成功，提示正确")
        except AssertionError as e:
            logger2.error('断言失败，提示错误！err: % s' % e)
            loginpage.get_windows_img()
            logger2.info('--------------------')
            # print('断言失败 ! err: %s' % e)
            raise AssertionError

    @ddt.data(*err_pwd_data)
    def test_3_login_err_pwd(self, data):
        """密码错误"""

        loginpage = LoginPage(self.driver)
        loginpage.confirm_login_page()
        # print("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        logger2.info("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        loginpage.type_username(data["username"])
        loginpage.type_pwd(data["pwd"])
        loginpage.click_login()
        err_msg = loginpage.get_err_pwd()
        try:
            self.assertEqual(err_msg, data["assert"])
            logger2.info("断言成功，提示正确")
            # print("断言成功，提示正确")
        except AssertionError as e:
            logger2.error('断言失败，提示错误!err：% s' % e)
            # print('断言失败 ! err: %s' % e)
            loginpage.get_windows_img()
            logger2.info('--------------------')
            raise AssertionError

    @ddt.data(*err_backend_data)
    def test_4_login_err_backend(self, data):
        """后台报错"""

        loginpage = LoginPage(self.driver)
        loginpage.confirm_login_page()
        # print("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        logger2.info("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        loginpage.type_username(data["username"])
        loginpage.type_pwd(data["pwd"])
        loginpage.click_login()
        err_msg = loginpage.get_err_backend()
        try:
            self.assertEqual(err_msg, data["assert"])
            logger2.info("断言成功，提示正确")
            # print("断言成功，提示正确")
            logger2.info('--------------------')
        except AssertionError as e:
            logger2.error('断言失败，提示错误!err：% s' % e)
            loginpage.get_windows_img()
            # print('断言失败 ! err: %s' % e)
            logger2.info('--------------------')
            raise AssertionError


@ddt.ddt
class LinkClick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, test_server='inServer')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_5_display_pwd(self):
        """显示和隐藏密码"""

        loginpage = LoginPage(self.driver)
        loginpage.type_username('18811133446')
        loginpage.type_pwd('1234qwer')
        # 第一次点击，显示密码：输入框的type属性变为text
        loginpage.click_display_pwd()
        attr = loginpage.get_attr("type", loginpage.path_pwd)
        try:
            self.assertEqual("text", attr)
            logger3.info("断言成功，密码输入框的属性是 %s" % attr)
            # print("断言成功!密码输入框的属性是%s" % attr)
            logger3.info('--------------------')
        except AssertionError as e:
            logger3.error("断言失败，密码输入框的属性是 % s. err：%s" % (attr, e))
            loginpage.get_windows_img()
            # print("断言失败！err：%s" % e)
            logger3.info('--------------------')
            raise AssertionError

        # 第二次点击，隐藏密码：输入框的type属性变为password
        loginpage.click_display_pwd()
        attr2 = loginpage.get_attr("type", loginpage.path_pwd)
        try:
            self.assertEqual("password", attr2)
            logger3.info("断言成功，密码输入框的属性是%s" % attr2)
            # print("断言成功!密码输入框的属性是%s" % attr2)
            logger3.info('--------------------')
        except AssertionError as e:
            logger3.error("断言失败，密码输入框的属性是 % s. err：%s" % (attr2, e))
            loginpage.get_windows_img()
            # print("断言失败！err：%s" % e)
            logger3.info('--------------------')
            raise AssertionError

    @ddt.data(*link_click_data)
    def test_6_link_click(self, data):
        """点击登录页面上的链接"""

        loginpage = LoginPage(self.driver)
        loginpage.click_link(data["path_link"], data["link_name"])
        text_next_page = loginpage.find_element(data["path_next_page"]).text
        try:
            self.assertIn(data["text_assert"], text_next_page)
            logger3.info("断言成功，\' %s \' 链接跳转成功！" % data["link_name"])
            # print("\' %s \' 链接跳转成功！" % data["link_name"])
            loginpage.back_browser()
            logger3.info('--------------------')
        except AssertionError as e:
            logger3.error("断言失败，\' %s \' 链接跳转失败！err：%s" % (data["link_name"], e))
            loginpage.get_windows_img()
            # print("\' %s \' 链接跳转失败！err：%s" % (data["link_name"], e))
            logger3.info('--------------------')
            raise AssertionError
