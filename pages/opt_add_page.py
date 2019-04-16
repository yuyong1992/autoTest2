# coding:utf-8

from autoTest2.framework.logger import Logger
from autoTest2.framework.base_page import BasePage
from autoTest2.tools.models import excel_to_dic

logger = Logger("OptAdd").getlog()


class OptAdd(BasePage):
    # 从Excel读取字段名称和路径
    # 在字段区域输入或选择操作

    file_path = "E:\Desktop/testdata_optadd.xlsx"
    file_sheetname = "field_path"
    opt_field_exl = excel_to_dic.ExcelToDic(file_path, file_sheetname)
    opt_field_data = opt_field_exl.excel_to_dic()

    def type_customer_name(self, text):
        """输入客户名称"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[0]["field_name"])
        self.type(self.opt_field_data[0]["field_path"], text, self.opt_field_data[0]["field_name"])

    def select_customer_industry(self, index):
        """选择客户行业"""
        self.click(self.opt_field_data[1]["field_path"], self.opt_field_data[1]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[1]["field_name"], index))

    def select_customer_province(self, index):
        """选择省"""
        self.click(self.opt_field_data[2]["field_path"], self.opt_field_data[2]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[2]["field_name"], index))

    def select_customer_city(self, index):
        """选择市"""
        self.click(self.opt_field_data[3]["field_path"], self.opt_field_data[3]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[3]["field_name"], index))

    def type_customer_website(self, text):
        """输入公司网址"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[4]["field_name"])
        self.type(self.opt_field_data[4]["field_path"], text, self.opt_field_data[4]["field_name"])

    def type_customer_zip(self, text):
        """输入邮政编码"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[5]["field_name"])
        self.type(self.opt_field_data[5]["field_path"], text, self.opt_field_data[5]["field_name"])

    def type_customer_address(self, text):
        """输入详细地址"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[6]["field_name"])
        self.type(self.opt_field_data[6]["field_path"], text, self.opt_field_data[6]["field_name"])

    def type_contact_lastname(self, text):
        """输入联系人姓氏"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[7]["field_name"])
        self.type(self.opt_field_data[7]["field_path"], text, self.opt_field_data[7]["field_name"])

    def type_contact_fistname(self, text):
        """输入联系人名字"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[8]["field_name"])
        self.type(self.opt_field_data[8]["field_path"], text, self.opt_field_data[8]["field_name"])

    def select_contact_gender(self, index):
        """选择联系人性别"""
        self.click(self.opt_field_data[9]["field_path"], self.opt_field_data[9]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[9]["field_name"], index))

    def type_contact_phone(self, text):
        """输入联系人电话"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[10]["field_name"])
        self.type(self.opt_field_data[10]["field_path"], text, self.opt_field_data[10]["field_name"])

    def type_contact_email(self, text):
        """输入联系人邮箱"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[11]["field_name"])
        self.type(self.opt_field_data[11]["field_path"], text, self.opt_field_data[11]["field_name"])

    def select_contact_status(self, index):
        """选择联系人状态"""
        self.click(self.opt_field_data[12]["field_path"], self.opt_field_data[12]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[12]["field_name"], index))

    def type_contact_position(self, text):
        """输入联系人职位"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[13]["field_name"])
        self.type(self.opt_field_data[13]["field_path"], text, self.opt_field_data[13]["field_name"])

    def type_opt_name(self, text):
        """输入商机名称"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[14]["field_name"])
        self.type(self.opt_field_data[14]["field_path"], text, self.opt_field_data[14]["field_name"])

    def type_opt_start_date(self, text):
        """输入商机服务开始时间"""
        path = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[2]/div/label'
        logger.info("正在输入\' %s \'" % self.opt_field_data[15]["field_name"])
        self.type(self.opt_field_data[15]["field_path"], text, self.opt_field_data[15]["field_name"])
        self.click(path)

    def type_opt_income_onetime(self, text):
        """输入一次性收入"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[16]["field_name"])
        self.type(self.opt_field_data[16]["field_path"], text, self.opt_field_data[16]["field_name"])

    def type_opt_income_monthly(self, text):
        """输入月度收入"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[17]["field_name"])
        self.type(self.opt_field_data[17]["field_path"], text, self.opt_field_data[17]["field_name"])

    def select_opt_apn_primary_need(self, index):
        """选择对光环云主要需求"""
        self.click(self.opt_field_data[18]["field_path"], self.opt_field_data[18]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[18]["field_name"], index))

    def select_opt_competitor(self, index):
        """选择竞争对手"""
        self.click(self.opt_field_data[19]["field_path"], self.opt_field_data[19]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[19]["field_name"], index))

    def type_opt_competitor_other(self, text):
        """输入竞争对手-其他"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[20]["field_name"])
        self.type(self.opt_field_data[20]["field_path"], text, self.opt_field_data[20]["field_name"])

    def select_opt_application(self, index):
        """选择应用场景"""
        self.click(self.opt_field_data[21]["field_path"], self.opt_field_data[21]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.driver.find_element_by_xpath(path))
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[21]["field_name"], index))

    def type_opt_technology_need(self, text):
        """输入技术需求"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[22]["field_name"])
        self.type(self.opt_field_data[22]["field_path"], text, self.opt_field_data[22]["field_name"])

    def type_opt_pain_spot(self, text):
        """输入客户痛点"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[23]["field_name"])
        self.type(self.opt_field_data[23]["field_path"], text, self.opt_field_data[23]["field_name"])

    def select_opt_customer_need(self, index):
        """选择客户需求"""
        self.click(self.opt_field_data[24]["field_path"], self.opt_field_data[24]["field_name"])
        self.sleep(0.1)
        path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element_by_xpath(path))
        self.click(path_option, "选项 %s" % index)
        logger.info("%s 下拉框已选择第 %s 个选项！" % (self.opt_field_data[24]["field_name"], index))

    def type_opt_customer_need_other(self, text):
        """输入客户需求-其他"""
        logger.info("正在输入\' %s \'" % self.opt_field_data[25]["field_name"])
        self.type(self.opt_field_data[25]["field_path"], text, self.opt_field_data[25]["field_name"])

    def submit_data(self):
        """点击提交按钮"""
        self.click(self.opt_field_data[26]["field_path"], self.opt_field_data[26]["field_name"])