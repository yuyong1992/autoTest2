# coding:utf-8

from framework.logger import Logger
from framework.base_page import BasePage

logger = Logger("OptAdd").getlog()


class SpnLeadAdd(BasePage):
    path_customer_name = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[1]/input'  # 客户名称输入框地址
    path_customer_industry = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div/div[1]/input'  # 客户的行业下拉框地址
    path_customer_province = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/form/div[1]/div[3]/div/div/div[2]/div/div/div[1]/input'  # 客户所在的省下拉框
    path_customer_city = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/form/div[1]/div[3]/div/div/div[3]/div/div/div[1]/input'  # 客户所在的市下拉框
    path_customer_website = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div/div/input'  # 客户公司的网址
    path_customer_zip = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div[1]/div/div/div/input'  # 客户所在地的邮编
    path_customer_address = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/textarea'  # 客户公司的详细地址
    path_contact_lastname = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/form/div/div[1]/div[1]/div[1]/div/div/div/div[1]/input'  # 客户联系人姓氏
    path_contact_fistname = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/form/div/div[1]/div[1]/div[2]/div/div/div/div[1]/input'  # 客户联系人名字
    path_contact_gender = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/form/div/div[1]/div[2]/div/div/div/div[1]/input'  # 客户联系人性别
    path_contact_phone = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/form/div/div[1]/div[3]/div/div/div/input'  # 客户联系人电话
    path_contact_email = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div/div/input'  # 客户联系人邮箱
    path_contact_status = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[2]/div/div/div/div[1]/input'  # 客户联系人在职状态
    path_contact_position = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/form/div/div[2]/div[3]/div/div/div/input'  # 客户联系人职位
    path_opt_name = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[1]/div/div/div/input'  # 商机名称
    path_opt_start_date = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[2]/div/div/div/input'  # 开始时间
    path_opt_income_onetime = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[3]/div/div/div/input'  # 一次性收入预估
    path_opt_income_monthly = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[4]/div/div/div/input'  # 月度收入预估
    path_opt_apn_primary_need = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[5]/div/div/div/div[1]/input'  # 对光环云的主要需求
    path_opt_competitor = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[6]/div/div/div/div/div/div[1]/input'  # 竞争对手
    path_opt_competitor_other = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[6]/div/div/div[2]/div/div/input'  # 竞争对手-其他
    path_opt_application = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[7]/div/div/div/div[1]/input'  # 应用场景
    path_opt_technology_need = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[8]/div/div/div/input'  # 技术需求
    path_opt_pain_spot = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[9]/div/div/div/input'  # 客户痛点
    path_opt_customer_need = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[10]/div/div/div[1]/div[2]/div/div/div[2]/span/span/i'  # 客户需求
    path_opt_customer_need_other = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]/form/div/div[10]/div/div/div[2]/div/div/div/input'  # 客户需求-其他
    path_button_submit = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[4]/button[1]'  # 提交按钮
    path_button_back = ''   # 返回按钮
    
    def submit(self, path_button_submit, button_name='保存'):
        self.click(self.path_button_submit, button_name)
        logger.info("点击 保存 按钮")

    def back_to_lead_list(self, path_button_back, button_name='返回线索列表'):
        self.click(self.path_button_back, button_name)
        logger.info("点击 返回 按钮")

    def type_customer_name(self, text):
        """输入客户名称"""
        logger.info("正在输入：客户名称")
        self.type(self.path_customer_name, text, "客户名称")

    def select_customer_industry(self, index):
        """选择客户行业"""
        self.click(self.path_customer_industry, "客户行业")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("客户名称 下拉框已选择第 %s 个选项！" % index)

    def select_customer_province(self, index):
        """选择省"""
        self.click(self.path_customer_province, "省份")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("省份 下拉框已选择第 %s 个选项！" % index)

    def select_customer_city(self, index):
        """选择市"""
        self.click(self.path_customer_city, "城市")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("城市 下拉框已选择第 %s 个选项！" % index)

    def type_customer_website(self, text):
        """输入公司网址"""
        logger.info("正在输入 公司网址")
        self.type(self.path_customer_website, text, "公司网址")

    def type_customer_zip(self, text):
        """输入邮政编码"""
        logger.info("正在输入 邮政编码")
        self.type(self.path_customer_zip, text, "邮政编码")

    def type_customer_address(self, text):
        """输入详细地址"""
        logger.info("正在输入 详细地址")
        self.type(self.path_customer_address, text, "详细地址")

    def type_contact_lastname(self, text):
        """输入联系人姓氏"""
        logger.info("正在输入 联系人姓氏")
        self.type(self.path_contact_lastname, text, "联系人姓氏")

    def type_contact_fistname(self, text):
        """输入联系人名字"""
        logger.info("正在输入 联系人名字")
        self.type(self.path_contact_fistname, text, "联系人名字")

    def select_contact_gender(self, index):
        """选择联系人性别"""
        self.click(self.path_contact_gender, "联系人性别")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("城市 下拉框已选择第 %s 个选项！" % index)

    def type_contact_phone(self, text):
        """输入联系人电话"""
        logger.info("正在输入 联系人电话")
        self.type(self.path_contact_phone, text, "联系人电话")

    def type_contact_email(self, text):
        """输入联系人邮箱"""
        logger.info("正在输入 联系人邮箱")
        self.type(self.path_contact_email, text, "联系人邮箱")

    def select_contact_status(self, index):
        """选择联系人状态"""
        self.click(self.path_contact_status, "联系人状态")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("城市 下拉框已选择第 %s 个选项！" % index)

    def type_contact_position(self, text):
        """输入联系人职位"""
        logger.info("正在输入 联系人职位")
        self.type(self.path_contact_position, text, "联系人职位")

    def type_opt_name(self, text):
        """输入商机名称"""
        logger.info("正在输入 商机名称")
        self.type(self.path_opt_name, text, "商机名称")

    def type_opt_start_date(self, text):
        """输入商机服务开始时间"""
        path = 'xpath=>//*[@id="app"]/div[1]/div[2]/div/div[2]/div[3]\
            /form/div/div[2]/div/label'
        logger.info("正在输入 服务开始时间")
        self.type(self.path_opt_start_date, text, "服务开始时间")
        self.click(path)

    def type_opt_income_onetime(self, text):
        """输入一次性收入"""
        logger.info("正在输入 一次性收入")
        self.type(self.path_opt_income_onetime, text, "一次性收入")

    def type_opt_income_monthly(self, text):
        """输入月度收入"""
        logger.info("正在输入 月度收入")
        self.type(self.path_opt_income_monthly, text, "月度收入")

    def select_opt_apn_primary_need(self, index):
        """选择对光环云主要需求"""
        self.click(self.path_opt_apn_primary_need, "对光环云主要需求")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("对光环云主要需求 下拉框已选择第 %s 个选项！" % index)

    def select_opt_competitor(self, index):
        """选择竞争对手"""
        self.click(self.path_opt_competitor, "竞争对手")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("竞争对手 下拉框已选择第 %s 个选项！" % index)

    def type_opt_competitor_other(self, text):
        """输入竞争对手-其他"""
        logger.info("正在输入 竞争对手-其他")
        self.type(self.path_opt_competitor_other, text, "竞争对手-其他")

    def select_opt_application(self, index):
        """选择应用场景"""
        self.click(self.path_opt_application, "应用场景")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("应用场景 下拉框已选择第 %s 个选项！" % index)

    def type_opt_technology_need(self, text):
        """输入技术需求"""
        logger.info("正在输入 技术需求")
        self.type(self.path_opt_technology_need, text, "技术需求")

    def type_opt_pain_spot(self, text):
        """输入客户痛点"""
        logger.info("正在输入 客户痛点")
        self.type(self.path_opt_pain_spot, text, "客户痛点")

    def select_opt_customer_need(self, index):
        """选择客户需求"""
        self.click(self.path_opt_customer_need, "客户需求")
        self.sleep(0.1)
        # 下拉选项的位置，index为指定点击第几个选项
        # path = '/html/body/div[last()]/div[1]/div[1]/ul/li[' + index + ']'
        path_option = 'xpath=>/html/body/div[last()]/div[1]/div[1]/ul/li[' \
            + index + ']'
        self.driver.execute_script('arguments[0].scrollIntoView();',
                                   self.find_element(path_option))
        self.sleep(0.1)
        self.click(path_option, "选项 %s" % index)
        logger.info("客户需求 下拉框已选择第 %s 个选项！" % index)

    def type_opt_customer_need_other(self, text):
        """输入客户需求-其他"""
        logger.info("正在输入 客户需求-其他")
        self.type(self.path_opt_customer_need_other, text, "客户需求-其他")

