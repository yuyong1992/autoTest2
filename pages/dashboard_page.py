# coding:utf-8

from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger("DashBoardPage").getlog()


class DashBoardPage(BasePage):
    def confirm_dashboard_page(self):
        """确认进入Dashboard页"""
        path_welcome = 'xpath=>//*[@id="app"]/div/div[3]/div/div[1]/h4'
        try:
            assert '欢迎，测试余永渠道商公司' in self.find_element(path_welcome).text
            logger.info('已进入Dashboard页面！')
        except AssertionError as e:
            logger.info('Dashboard页面加载失败：%s ' % e)
            print('Dashboard页面加载失败：%s ' % e)
            raise AssertionError

    def close_tip_last_login(self):
        """关闭上次登录提示框"""
        self.sleep(0.5)
        path_tip = 'xpath=>/html/body/div[3]/div/div[2]'
        self.click(path_tip, '上次登录提示框关闭按钮')

    def product_select(self, product):
        """我的产品"""
        path_aws = \
            'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/ul/li[@class="aws_border"]'
        path_rubicon = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/ul/li[@class="rubicon_border"]'

        if product == 'aws':
            path = path_aws
            self.click(path, product)
        elif product == 'rubicon':
            path = path_rubicon
            self.click(path, product)
        else:
            logger.info('没有该产品！')
