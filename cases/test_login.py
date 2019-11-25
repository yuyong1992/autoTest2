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
# 获取错误的登录测试数据
err_phone_sheetname = "err_phone"
err_phone_exl = excel_to_dic.ExcelToDic(file_path, err_phone_sheetname)
err_phone_data = err_phone_exl.excel_to_dic()
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
        print("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        logger1.info("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        loginpage.wait(2)
        loginpage.type_username(data["username"])
        loginpage.type_pwd(data["pwd"])
        loginpage.click_but(but_name="登录")
        loginpage.wait(10)
        try:
            self.assertIn(loginpage.get_page_title(), data["assert"])
            print('%s Login Test Pass!' % data["username"])
            logger1.info('%s Login Test Pass!' % data["username"])
            # loginpage.driver.quit()
        except AssertionError as e:
            logger1.error('%s 登录失败！ err: %s' % (data["username"], e))
            print('断言失败! err: %s' % e)
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
    def test_2_login_err(self, data):
        """手机号格式错误"""

        loginpage = LoginPage(self.driver)
        loginpage.confirm_login_page()
        print("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        logger2.info("测试数据： ' %s ' ' %s ' ' %s '" % (data["用例名"], data["username"], data["pwd"]))
        loginpage.wait(2)
        loginpage.type_username(data["username"])
        loginpage.type_pwd(data["pwd"])
        loginpage.click_but()
        loginpage.sleep(1.5)
        err_msg = loginpage.get_err_msg()
        try:
            self.assertEqual(err_msg, data["assert"])
            logger2.info("断言成功，提示正确")
            print("断言成功，提示正确")
        except AssertionError as e:
            logger2.error('断言失败！The wrong err_msg!')
            print('断言失败 ! err: %s' % e)
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

    def test_3_display_pwd(self):
        """显示和隐藏密码"""
        path_display_pwd = 'xpath=>//*[@id="app"]/div/div[3]/div/div[1]/form/div[2]/i'
        path_attr = 'xpath=>//*[@id="app"]/div/div[3]/div/div[1]/form/div[2]/input'
        loginpage = LoginPage(self.driver)
        # 第一次点击，显示密码：输入框的type属性变为text
        loginpage.click_but("显示密码按钮", path_display_pwd)
        attr = loginpage.get_attr("type", path_attr)
        try:
            self.assertEqual("text", attr)
            logger3.info("断言成功!密码输入框的属性是%s" % attr)
            print("断言成功!密码输入框的属性是%s" % attr)
        except AssertionError as e:
            logger3.error("断言失败！err：%s" % e)
            print("断言失败！err：%s" % e)
            raise AssertionError

        # 第二次点击，隐藏密码：输入框的type属性变为password
        loginpage.click_but("隐藏密码按钮", path_display_pwd)
        attr2 = loginpage.get_attr("type", path_attr)
        try:
            self.assertEqual("password", attr2)
            logger3.info("断言成功!密码输入框的属性是%s" % attr2)
            print("断言成功!密码输入框的属性是%s" % attr2)
        except AssertionError as e:
            logger3.error("断言失败！err：%s" % e)
            print("断言失败！err：%s" % e)
            raise AssertionError

    @ddt.data(*link_click_data)
    def test_4_link_click(self, data):
        """点击登录页面上的链接"""
        # link_name = "验证码登录"
        # path_link_capt = 'xpath=>//*[@id="app"]/div/div[3]/div/div[1]/form/div[3]/a'
        # path_next_page = 'xpath=>//*[@id="app"]/div/div[3]/div/div[1]/form/div[2]/p'
        # text_assert = "验证码"
        loginpage = LoginPage(self.driver)
        loginpage.click_but(data["link_name"], data["path_link"])
        loginpage.wait(5)
        text_next_page = loginpage.find_element(data["path_next_page"]).text
        try:
            self.assertIn(data["text_assert"], text_next_page)
            logger3.info("\' %s \' 链接跳转成功！" % data["link_name"])
            print("\' %s \' 链接跳转成功！" % data["link_name"])
            loginpage.back_browser()
        except AssertionError as e:
            logger3.error("\' %s \' 链接跳转失败！err：%s" % (data["link_name"], e))
            print("\' %s \' 链接跳转失败！err：%s" % (data["link_name"], e))
            raise AssertionError


if __name__ == '__main__':
    unittest.main()
