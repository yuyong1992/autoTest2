# coding:utf-8

from framework.base_page import BasePage
from framework.logger import Logger

logger = Logger('LoginPage').getlog()


class LoginPage(BasePage):
    path_username = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[1]/input'
    path_pwd = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[2]/input'
    path_err = 'xpath=>/html/body/div[3]/p'
    path_but = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/form/div[4]'

    def type_username(self, username):
        self.type(self.path_username, username, input_name='手机号')

    def type_pwd(self, pwd):
        self.type(self.path_pwd, pwd, input_name='密码')

    def click_but(self):
        self.click(self.path_but, but_name='登录')

    def get_err_msg(self):
        err_msg = self.find_element(self.path_err)
        return err_msg.text

    # 用登录页面上的文字确认是否进入登录页面
    def confirm_login_page(self):
        path_welcome = 'xpath=>//*[@id="app"]/div/div/div[2]/div[2]/h4'
        try:
            assert '欢迎登录' in self.find_element(path_welcome).text
            logger.info('已进入登录页面！')
        except AssertionError as e:
            logger.info('登录页面加载失败：%s ' % e)
            print('登录页面加载失败：%s ' % e)
            raise AssertionError

    # 获取当前元素的某个属性的值
    def get_attr(self, attr_name, selector):
        try:
            attr = self.find_element(selector).get_attribute(attr_name)
            return attr
        except Exception as e:
            logger.info("获取元素属性异常！err：%s" % e)

    def back_browser(self):
        self.back()
