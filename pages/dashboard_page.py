# -*- coding:utf-8 -*-

from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger("DashBoardPage").getlog()


class DashBoardPage(BasePage):
    path_tip_last_login = 'xpath=>/html/body/div[3]/div/div[1]/p'
    path_tip_change_pwd = 'xpath=>/html/body/div[4]/div/div[1]/p'

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

    def get_tip_last_login(self):
        value = self.find_element(self.path_tip_last_login)
        return value

    def get_tip_change_pwd(self):
        return self.find_element(self.path_tip_change_pwd)

    def close_tip_last_login(self):
        """关闭上次登录提示框"""
        self.sleep(0.5)
        # path_tip = 'xpath=>/html/body/div[3]/div/div[2]'
        self.click(self.path_tip_last_login, '上次登录提示框关闭按钮')

    def close_tip_change_pwd(self):
        """"关闭密码3个月未修改的提示框"""
        self.sleep(0.5)
        # path_tip = 'xpath=>/html/body/div[4]/div/div[1]'
        self.click(self.path_tip_change_pwd, '密码修改提示框关闭按钮')

    def product_select(self, product):
        """我的产品"""
        """
        1.aws ：AWS
        2.rubicon ：Inspire Connect
        """
        # 不同产品的地址
        path_aws = 'xpath=>' \
                   '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/ul/li[@class="aws_border"]'
        path_rubicon = 'xpath=>' \
                       '//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/div/ul/' \
                       'li[@class="rubicon_border"]'

        if product == 'aws':
            path = path_aws
            self.click(path, product)
        elif product == 'rubicon':
            path = path_rubicon
            self.click(path, product)
        else:
            logger.info('没有该产品！')

    def recommend_product(self, product):
        """推荐产品"""
        """
        1.ec2 ：EC2
        2.s3 ：S3
        3.rds ：RDS
        4.training ：AWS 培训
        """
        path_ec2 = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[1]/span'
        path_s3 = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/span'
        path_rds = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[3]/span'
        path_training = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[4]/span'

        if product == 'ec2':
            self.click(path_ec2, product)
        elif product == 's3':
            self.click(path_s3, product)
        elif product == 'rds':
            self.click(path_rds, product)
        else:
            self.click(path_training, product)

    def download_resource(self):
        """下载演讲资料"""
        path = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/h2/a'

        self.click(path, "下载演讲资料")

    def goto_spn(self):
        """点击【SPN信息】按钮"""
        path = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/span[1]'

        self.click(path, 'SPN 信息')

    def goto_resource_manage(self):
        """点击【添加资源】按钮"""
        path = 'xpath=>//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/span[2]'

        self.click(path, '添加资源')
