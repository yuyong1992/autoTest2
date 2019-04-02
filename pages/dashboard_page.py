# coding:utf-8

from autoSinnetCloud.framework.base_page import BasePage
from autoSinnetCloud.framework.logger import Logger

logger = Logger("DashBoardPage").getlog()


class DashBoardPage(BasePage):
    def confirm_login_page(self):
        path_welcome = 'xpath=>//*[@id="app"]/div/div[3]/div/div[1]/h4'
        try:
            assert '欢迎，北京光环云数据有限责任公司' in self.find_element(path_welcome).text
            logger.info('已进入Dashboard页面！')
        except AssertionError as e:
            logger.info('Dashboard页面加载失败：%s ' % e)
            print('Dashboard页面加载失败：%s ' % e)
            raise AssertionError

    def click_but(self, selector, but_name):
        self.click(selector, but_name)
