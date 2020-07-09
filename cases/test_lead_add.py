# coding:utf-8

import unittest
import ddt
from framework.logger import Logger
from framework.browser_engine import BrowserEngine
from pages.opt_add_page import OptAdd
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
from tools.models import excel_to_dic

logger = Logger("OptAddSuccess").getlog()
logger2 = Logger("OptAddErrSub").getlog()
logger3 = Logger("OptAddErrInTime").getlog()
logger4 = Logger("OptAddErrInTimeNull").getlog()

file_path = r"E:\Desktop/testdata_optadd.xlsx"
file_sheet = "field_value"
field_value_exl = excel_to_dic.ExcelToDic(file_path, file_sheet)
field_value_data = field_value_exl.excel_to_dic()

file_sheet_err = "field_value_err"
field_value_err_exl = excel_to_dic.ExcelToDic(file_path, file_sheet_err)
field_value_err_data = field_value_err_exl.excel_to_dic()

file_sheet_err_intime = "field_value_err_intime"
field_value_err_intime_exl = excel_to_dic.ExcelToDic(file_path, file_sheet_err_intime)
field_value_err_intime_data = field_value_err_intime_exl.excel_to_dic()

file_sheet_assert_path = "field_assert_path"
field_assert_path_exl = excel_to_dic.ExcelToDic(file_path, file_sheet_assert_path)
field_assert_path_data = field_assert_path_exl.excel_to_dic()

file_sheet_field_path = "field_path"
field_path_exl = excel_to_dic.ExcelToDic(file_path, file_sheet_field_path)
field_path_data = field_path_exl.excel_to_dic()


@ddt.ddt
class OptAddSuccess(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self, test_server='inServer')
        self.driver.implicitly_wait(10)
        try:
            # SPN登录
            loginpage = LoginPage(cls.driver)
            loginpage.type_username('18811133441')
            loginpage.type_pwd('1234qwer')
            loginpage.click_login()

            # 进入添加lead的页面
            dashpage = DashBoardPage(cls.driver)
            # dashpage.sleep(1)
            dashpage.close_tip_last_login()
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/div', 'SPN')
            dashpage.sleep(0.5)
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/li[3]/a/span[2]', '线索管理')
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/a/button', '添加线索')
            logger.info("初始化完成！")
        except Exception as e:
            logger.error("初始化失败！err：%s" % e)
            print("初始化失败！err：%s" % e)
            raise AssertionError

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*field_value_data)
    def test_1_opt_add_success(self, data):
        """线索添加成功"""
        addpage = OptAdd(self.driver)
        # 输入客户名称
        if data["客户名称"] != '':
            addpage.type_customer_name(data["客户名称"])
        # 选择行业类型：从1开始
        if data["行业"] != '':
            addpage.select_customer_industry(data["行业"])
        # 选择省
        if data["省"] != '':
            addpage.select_customer_province(data["省"])
        # 选择市
        if data["市"]:
            addpage.select_customer_city(data["市"])
        # 输入公司网址
        if data["公司网址"]:
            addpage.type_customer_website(data["公司网址"])
        # 输入邮政编码
        if data["邮政编码"]:
            addpage.type_customer_zip(data["邮政编码"])
        # 输入详细地址
        if data["详细地址"]:
            addpage.type_customer_address(data["详细地址"])
        # 输入联系人姓氏
        if data["姓氏"]:
            addpage.type_contact_lastname(data["姓氏"])
        # 输入联系人名字
        if data["名字"]:
            addpage.type_contact_fistname(data["名字"])
        # 选择联系人性别
        if data["联系人性别"]:
            addpage.select_contact_gender(data["联系人性别"])
        # 输入联系人电话
        if data["联系人电话"]:
            addpage.type_contact_phone(data["联系人电话"])
        # 输入联系人邮箱
        if data["联系人邮箱"]:
            addpage.type_contact_email(data["联系人邮箱"])
        # 选择联系人状态
        if data["联系人状态"]:
            addpage.select_contact_status(data["联系人状态"])
        # 输入联系人职位
        if data["联系人职位"]:
            addpage.type_contact_position(data["联系人职位"])
        # 输入线索名称
        if data["线索名称"]:
            addpage.type_opt_name(data["线索名称"])
        # 输入服务开始时间
        if data["服务开始时间"]:
            addpage.type_opt_start_date(data["服务开始时间"])
        # 输入一次性收入
        if data["一次性收入"]:
            addpage.type_opt_income_onetime(data["一次性收入"])
        # 输入月度收入
        if data["月度收入"]:
            addpage.type_opt_income_monthly(data["月度收入"])
        # 选择对光环云的主要需求
        if data["对光环云主要需求"]:
            addpage.select_opt_apn_primary_need(data["对光环云主要需求"])
        # 选择竞争对手
        if data["竞争对手"]:
            addpage.select_opt_competitor(data["竞争对手"])
        # 输入竞争对手-其他
        if data["竞争对手"] == "9" and data["竞争对手-其他"]:
            addpage.type_opt_competitor_other(data["竞争对手-其他"])
        # 选择应用场景
        if data["应用场景"]:
            addpage.select_opt_application(data["应用场景"])
        # 输入技术需求
        if data["技术需求"]:
            addpage.type_opt_technology_need(data["技术需求"])
        # 输入客户痛点
        if data["客户痛点"]:
            addpage.type_opt_pain_spot(data["客户痛点"])
        # 选择客户需求
        if data["客户需求"]:
            addpage.select_opt_customer_need(data["客户需求"])
        # 输入客户需求-其他
        if data["客户需求"] == "5" and data["客户需求-其他"]:
            addpage.type_opt_customer_need_other(data["客户需求-其他"])
        # 点击提交按钮
        addpage.submit_data()
        addpage.sleep(0.5)
        try:
            self.assertEqual("保存成功！", addpage.find_element('xpath=>/html/body/div[3]/div/div[1]/p').text)
            logger.info("线索添加成功！")
            print("%s 线索添加成功！" % data["用例名称"])
        except (AssertionError, AttributeError) as e:
            logger.error("线索添加失败！err：%s" % e)
            print("线索添加失败！%s err：%s" % (data["用例名称"], e))
            raise AssertionError


@ddt.ddt
class OptAddErrSub(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self, test_server='inServer')
        self.driver.implicitly_wait(10)
        try:
            # SPN登录
            loginpage = LoginPage(cls.driver)
            loginpage.type_username('18811133441')
            loginpage.type_pwd('1234qwer')
            loginpage.click_login()

            # 进入添加lead的页面
            dashpage = DashBoardPage(cls.driver)
            # dashpage.sleep(1)
            dashpage.close_tip_last_login()
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/div', 'SPN')
            dashpage.sleep(0.5)
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/li[3]/a/span[2]', '线索管理')
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/a/button', '添加线索')
            logger.info("初始化完成！")
        except Exception as e:
            logger.error("初始化失败！err：%s" % e)
            print("初始化失败！err：%s" % e)
            raise AssertionError

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*field_value_err_data)
    def test_2_opt_add_err(self, data):
        """线索添加失败-点击提交后校验"""

        addpage = OptAdd(self.driver)
        # 输入客户名称
        if data["客户名称"] != '':
            addpage.type_customer_name(data["客户名称"])
        # 选择行业类型：从1开始
        if data["行业"] != '':
            addpage.select_customer_industry(data["行业"])
        # 选择省
        if data["省"] != '':
            addpage.select_customer_province(data["省"])
        # 选择市
        if data["市"]:
            addpage.select_customer_city(data["市"])
        # 输入公司网址
        if data["公司网址"]:
            addpage.type_customer_website(data["公司网址"])
        # 输入邮政编码
        if data["邮政编码"]:
            addpage.type_customer_zip(data["邮政编码"])
        # 输入详细地址
        if data["详细地址"]:
            addpage.type_customer_address(data["详细地址"])
        # 输入联系人姓氏
        if data["姓氏"]:
            addpage.type_contact_lastname(data["姓氏"])
        # 输入联系人名字
        if data["名字"]:
            addpage.type_contact_fistname(data["名字"])
        # 选择联系人性别
        if data["联系人性别"]:
            addpage.select_contact_gender(data["联系人性别"])
        # 输入联系人电话
        if data["联系人电话"]:
            addpage.type_contact_phone(data["联系人电话"])
        # 输入联系人邮箱
        if data["联系人邮箱"]:
            addpage.type_contact_email(data["联系人邮箱"])
        # 选择联系人状态
        if data["联系人状态"]:
            addpage.select_contact_status(data["联系人状态"])
        # 输入联系人职位
        if data["联系人职位"]:
            addpage.type_contact_position(data["联系人职位"])
        # 输入线索名称
        if data["线索名称"]:
            addpage.type_opt_name(data["线索名称"])
        # 输入服务开始时间
        if data["服务开始时间"]:
            addpage.type_opt_start_date(data["服务开始时间"])
        # 输入一次性收入
        if data["一次性收入"]:
            addpage.type_opt_income_onetime(data["一次性收入"])
        # 输入月度收入
        if data["月度收入"]:
            addpage.type_opt_income_monthly(data["月度收入"])
        # 选择对光环云的主要需求
        if data["对光环云主要需求"]:
            addpage.select_opt_apn_primary_need(data["对光环云主要需求"])
        # 选择竞争对手
        if data["竞争对手"]:
            addpage.select_opt_competitor(data["竞争对手"])
        # 输入竞争对手-其他
        if data["竞争对手"] == "9" and data["竞争对手-其他"]:
            addpage.type_opt_competitor_other(data["竞争对手-其他"])
        # 选择应用场景
        if data["应用场景"]:
            addpage.select_opt_application(data["应用场景"])
        # 输入技术需求
        if data["技术需求"]:
            addpage.type_opt_technology_need(data["技术需求"])
        # 输入客户痛点
        if data["客户痛点"]:
            addpage.type_opt_pain_spot(data["客户痛点"])
        # 选择客户需求
        if data["客户需求"]:
            addpage.select_opt_customer_need(data["客户需求"])
        # 输入客户需求-其他
        if data["客户需求"] == "5" and data["客户需求-其他"]:
            addpage.type_opt_customer_need_other(data["客户需求-其他"])
        try:
            # 点击提交按钮
            addpage.submit_data()
            addpage.sleep(0.5)
            self.assertEqual(data["断言内容"], addpage.find_element(data["断言路径"]).text)
            logger2.info("%s 断言成功！" % data["用例名称"])
            print("%s 断言成功！" % data["用例名称"])
        except AssertionError as e:
            logger2.error("%s 断言失败！err：%s" % (data["用例名称"], e))
            print("%s 断言失败！err：%s" % (data["用例名称"], e))
            raise AssertionError


@ddt.ddt
class OptAddErrInTime(unittest.TestCase):
    """字段规则校验-失焦后立即校验"""

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, test_server='inServer')
        cls.driver.implicitly_wait(10)
        try:
            # SPN登录
            loginpage = LoginPage(cls.driver)
            loginpage.type_username('18811133441')
            loginpage.type_pwd('1234qwer')
            loginpage.click_login()

            # 进入添加lead的页面
            dashpage = DashBoardPage(cls.driver)
            # dashpage.sleep(1)
            dashpage.close_tip_last_login()
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/div', 'SPN')
            dashpage.sleep(0.5)
            dashpage.click('xpath=>'
                           '//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/li[3]/a/span[2]', '线索管理')
            dashpage.click(
                'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/a/button', '添加线索')
            logger.info("初始化完成！")
        except Exception as e:
            logger.error("初始化失败！err：%s" % e)
            print("初始化失败！err：%s" % e)
            raise AssertionError

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.data(*field_value_err_intime_data)
    def test_3_opt_add_err_intime(self, data):
        """线索添加失败-失焦后立即校验"""

        addpage = OptAdd(self.driver)
        # 输入客户名称
        if data["客户名称"]:
            addpage.type_customer_name(data["客户名称"])
        # 选择行业类型：从1开始
        if data["行业"]:
            addpage.select_customer_industry(data["行业"])
        # 选择省
        if data["省"]:
            addpage.select_customer_province(data["省"])
        # 选择市
        if data["市"]:
            addpage.select_customer_city(data["市"])
        # 输入公司网址
        if data["公司网址"]:
            addpage.type_customer_website(data["公司网址"])
        # 输入邮政编码
        if data["邮政编码"]:
            addpage.type_customer_zip(data["邮政编码"])
        # 输入详细地址
        if data["详细地址"]:
            addpage.type_customer_address(data["详细地址"])
        # 输入联系人姓氏
        if data["姓氏"]:
            addpage.type_contact_lastname(data["姓氏"])
        # 输入联系人名字
        if data["名字"]:
            addpage.type_contact_fistname(data["名字"])
        # 选择联系人性别
        if data["联系人性别"]:
            addpage.select_contact_gender(data["联系人性别"])
        # 输入联系人电话
        if data["联系人电话"]:
            addpage.type_contact_phone(data["联系人电话"])
        # 输入联系人邮箱
        if data["联系人邮箱"]:
            addpage.type_contact_email(data["联系人邮箱"])
        # 选择联系人状态
        if data["联系人状态"]:
            addpage.select_contact_status(data["联系人状态"])
        # 输入联系人职位
        if data["联系人职位"]:
            addpage.type_contact_position(data["联系人职位"])
        # 输入线索名称
        if data["线索名称"]:
            addpage.type_opt_name(data["线索名称"])
        # 输入服务开始时间
        if data["服务开始时间"]:
            addpage.type_opt_start_date(data["服务开始时间"])
        # 输入一次性收入
        if data["一次性收入"]:
            addpage.type_opt_income_onetime(data["一次性收入"])
        # 输入月度收入
        if data["月度收入"]:
            addpage.type_opt_income_monthly(data["月度收入"])
        # 选择对光环云的主要需求
        if data["对光环云主要需求"]:
            addpage.select_opt_apn_primary_need(data["对光环云主要需求"])
        # 选择竞争对手
        if data["竞争对手"]:
            addpage.select_opt_competitor(data["竞争对手"])
        # 输入竞争对手-其他
        if data["竞争对手"] == "9" and data["竞争对手-其他"]:
            addpage.type_opt_competitor_other(data["竞争对手-其他"])
        # 选择应用场景
        if data["应用场景"]:
            addpage.select_opt_application(data["应用场景"])
        # 输入技术需求
        if data["技术需求"]:
            addpage.type_opt_technology_need(data["技术需求"])
        # 输入客户痛点
        if data["客户痛点"]:
            addpage.type_opt_pain_spot(data["客户痛点"])
        # 选择客户需求
        if data["客户需求"] != '':
            addpage.select_opt_customer_need(data["客户需求"])
        # 输入客户需求-其他
        if data["客户需求"] == "5" and data["客户需求-其他"]:
            addpage.type_opt_customer_need_other(data["客户需求-其他"])
        addpage.sleep(1)
        try:
            self.assertEqual(data["断言内容"], addpage.find_element(data["断言路径"]).text)
            logger3.info("%s 断言成功！" % data["用例名称"])
            print("%s 断言成功！" % data["用例名称"])
        except (AssertionError, AttributeError) as e:
            logger3.error("%s 断言失败！err：%s" % (data["用例名称"], e))
            print("%s 断言失败！err：%s" % (data["用例名称"], e))
            raise AssertionError


class OptAddErrInTimeNull(unittest.TestCase):
    """字段规则空值校验-失焦后立即校验"""

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls, test_server='inServer')
        cls.driver.implicitly_wait(10)
        try:
            # SPN登录
            loginpage = LoginPage(cls.driver)
            loginpage.type_username('18811133441')
            loginpage.type_pwd('1234qwer')
            loginpage.click_login()

            # 进入添加lead的页面
            dashpage = DashBoardPage(cls.driver)
            # dashpage.sleep(1)
            dashpage.close_tip_last_login()
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/div', 'SPN')
            dashpage.sleep(0.5)
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/li[3]/a/span[2]', '线索管理')
            dashpage.click('xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/a/button', '添加线索')
            logger.info("初始化完成！")
        except Exception as e:
            logger.error("初始化失败！err：%s" % e)
            print("初始化失败！err：%s" % e)
            raise AssertionError

    @classmethod
    def tearDownClass(cls):
        addpage = OptAdd(cls.driver)
        addpage.quit_browser()

    def test_4_opt_add_err_null_intime(self):
        """输入框空值校验-失焦后立即校验"""

        addpage = OptAdd(self.driver)

        # 客户名称不能为空
        addpage.type_customer_name(" ")
        # addpage.find_element(field_path_data[0]["field_path"]).send_keys(Keys.TAB)
        addpage.pres_tab(field_path_data[0]["field_path"])
        addpage.sleep(1)
        try:
            self.assertEqual(field_assert_path_data[0]["assert_content"],
                             addpage.find_element(field_assert_path_data[0]["assert_path"]).text)
            logger4.info("%s不能为空， 断言成功！" % (field_assert_path_data[0]["field_name"]))
        except (AssertionError, AttributeError) as e:
            logger4.error("%s不能为空，断言失败！err：%s" % (field_assert_path_data[0]["field_name"], e))
            raise AssertionError

        # 姓氏不能为空
        addpage.type_contact_lastname(" ")
        # addpage.find_element(field_path_data[7]["field_path"]).send_keys(Keys.TAB)
        addpage.pres_tab(field_path_data[7]["field_path"])
        addpage.sleep(1)
        try:
            self.assertEqual(field_assert_path_data[4]["assert_content"],
                             addpage.find_element(field_assert_path_data[4]["assert_path"]).text)
            logger4.info("%s不能为空， 断言成功！" % (field_assert_path_data[4]["field_name"]))
        except (AssertionError, AttributeError) as e:
            logger4.error("%s不能为空，断言失败！err：%s" % (field_assert_path_data[4]["field_name"], e))
            raise AssertionError

        # 名字不能为空
        addpage.type_contact_fistname(" ")
        # addpage.find_element(field_path_data[8]["field_path"]).send_keys(Keys.TAB)
        addpage.pres_tab(field_path_data[8]["field_path"])
        addpage.sleep(1)
        try:
            self.assertEqual(field_assert_path_data[5]["assert_content"],
                             addpage.find_element(field_assert_path_data[5]["assert_path"]).text)
            logger4.info("%s不能为空， 断言成功！" % (field_assert_path_data[5]["field_name"]))
        except (AssertionError, AttributeError) as e:
            logger4.error("%s不能为空，断言失败！err：%s" % (field_assert_path_data[5]["field_name"], e))
            raise AssertionError

        # 电话不能为空
        addpage.type_contact_phone(" ")
        # addpage.find_element(field_path_data[10]["field_path"]).send_keys(Keys.TAB)
        addpage.pres_tab(field_path_data[10]["field_path"])
        addpage.sleep(1)
        try:
            self.assertEqual(field_assert_path_data[6]["assert_content"],
                             addpage.find_element(field_assert_path_data[6]["assert_path"]).text)
            logger4.info("%s不能为空， 断言成功！" % (field_assert_path_data[6]["field_name"]))
        except (AssertionError, AttributeError) as e:
            logger4.error("%s不能为空，断言失败！err：%s" % (field_assert_path_data[6]["field_name"], e))
            raise AssertionError

        # 邮箱不能为空
        addpage.type_contact_email(" ")
        # addpage.find_element(field_path_data[11]["field_path"]).send_keys(Keys.TAB)
        addpage.pres_tab(field_path_data[11]["field_path"])
        addpage.sleep(1)
        try:
            self.assertEqual(field_assert_path_data[7]["assert_content"],
                             addpage.find_element(field_assert_path_data[7]["assert_path"]).text)
            logger4.info("%s不能为空， 断言成功！" % (field_assert_path_data[7]["field_name"]))
        except (AssertionError, AttributeError) as e:
            logger4.error("%s不能为空，断言失败！err：%s" % (field_assert_path_data[7]["field_name"], e))
            raise AssertionError

        # # 联系人选择“其他”，“其他联系人”输入框不能为空
        # addpage.select_opt_competitor("9")
        # addpage.type_opt_competitor_other(" ")
        # # addpage.find_element(field_path_data[20]["field_path"]).send_keys(Keys.TAB)
        # addpage.pres_tab(field_path_data[20]["field_path"])
        # addpage.sleep(1)
        # try:
        #     self.assertEqual(field_assert_path_data[13]["assert_content"], addpage.find_element(field_assert_path_data[13]["assert_path"]).text)
        #     logger4.info("%s不能为空， 断言成功！" % (field_assert_path_data[13]["field_name"]))
        # except (AssertionError, AttributeError) as e:
        #     logger4.error("%s不能为空，断言失败！err：%s" % (field_assert_path_data[13]["field_name"], e))
        #     raise AssertionError
        #
        # # 客户需求选择“其他”，“其他客户需求”输入框不能为空
        # addpage.select_opt_customer_need("5")
        # addpage.type_opt_customer_need_other(" ")
        # # addpage.find_element(field_path_data[25]["field_path"]).send_keys(Keys.TAB)
        # addpage.pres_tab(field_path_data[25]["field_path"])
        # addpage.sleep(1)
        # try:
        #     self.assertEqual(field_assert_path_data[16]["assert_content"], addpage.find_element(field_assert_path_data[16]["assert_path"]).text)
        #     logger4.info("%s不能为空， 断言成功！" % (field_assert_path_data[16]["field_name"]))
        # except (AssertionError, AttributeError) as e:
        #     logger4.error("%s不能为空，断言失败！err：%s" % (field_assert_path_data[16]["field_name"], e))
        #     raise AssertionError
