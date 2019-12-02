# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os.path
from .logger import Logger

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 退出浏览器结束测试
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("点击浏览器前进按钮")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("点击浏览器退回按钮")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒钟." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器")
        except NameError as e:
            logger.error("退出浏览器失败： %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/autoTest2/result/screenshots/'
        # logger.info('%s ;%s ' % (file_path, os.path.dirname(os.path.abspath('.'))))
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            # self.driver.save_screenshot(screen_name)
            logger.info("保存页面截图\'%s\' \n!!!!!!!!!!!!!!!!" % screen_name)
        except NameError as e:
            logger.error("页面截图失败! %s\n!!!!!!!!!!!!!!!!" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("通过 %s 定位元素成功，元素位置: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没有找到元素，元素地址: %s 。err：% s" % (selector_value, e))
                # 截图
                self.get_windows_img()
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("通过 %s 定位元素成功，元素位置: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("没有找到元素，元素地址: %s 。err：% s" % (selector_value, repr(e)))
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("请输入正确的定位方式！")

        return element

    # 输入
    def type(self, selector, text, input_name="输入框"):

        el = self.find_element(selector)
        try:
            el.clear()
            el.send_keys(text)
            logger.info("在输入框 \' %s \' 中输入 \' %s \'" % (input_name, text))
        except NameError as e:
            logger.error("操作失败，在输入框 \' %s \' 中输入 \' %s \'。err：%s" % (input_name, text, e))
            self.get_windows_img()
        except Exception as e:
            logger.error("操作失败，在输入框 \' %s \' 中输入 \' %s \'。err：%s" % (input_name, text, repr(e)))

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("清空输入框")
        except NameError as e:
            logger.error("操作失败，清空输入框失败。err： %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector, but_name="按钮"):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("已点击 \'%s\'按钮" % but_name)
        except NameError as e:
            logger.error("操作失败，点击\'%s\'按钮操作失败： %s" % (but_name, e))
        except Exception as e:
            logger.error("操作失败，点击\'%s\'按钮操作失败: %s" % (but_name, e))

    # 获取网页标题
    def get_page_title(self):
        logger.info("当前页面的标题为：\'%s\'" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("休眠%s 秒钟。。。" % seconds)

    def pres_tab(self, selector):
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.TAB)
            logger.info("点击TAB键")
        except NameError as e:
            logger.error("操作失败，点击TAB键失败！err: %s" % e)
