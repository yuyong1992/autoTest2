# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os.path
from .logger import Logger

logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 浏览器退出
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 关闭当前浏览器窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 屏幕截图
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(
            os.path.abspath('.')) + 'autoTest2/result/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            # self.driver.save_screenshot(screen_name)
            logger.info(
                "Had take screenshot and save to folder : /result/screenshots")
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 元素定位方法
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
                logger.info("Had find the element successful "
                            "by %s via value: %s " %
                            (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(
                selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element successful by %s via value: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % repr(e))
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 输入框输入文本
    def type(self, selector, text, input_name="inputBox"):

        el = self.find_element(selector)
        try:
            el.clear()
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox \' %s \'" %
                        (text, input_name))
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()
        except Exception as e:
            logger.error("Failed to type in input box with %s" % repr(e))

    # 清除输入框文本
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击按钮
    def click(self, selector, but_name="按钮"):

        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element \' %s \' was clicked." % but_name)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)
        except Exception as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

    # 点击tab键
    def pres_tab(self, selector):
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.TAB)
            logger.info("Press the TAB key!")
        except NameError as e:
            logger.error("Failed to press the TAB key！err: %s" % e)
