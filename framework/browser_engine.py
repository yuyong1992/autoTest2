# -*- coding:utf-8 -*-

import os.path
from configparser import ConfigParser
from selenium import webdriver
from .logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/autoTest2/tools/chromedriver.exe'
    ie_driver_path = dir + 'autoTest2/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

        # read the browser type from config.ini file, return the driver

    def open_browser(self, driver, test_server):
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/autoTest2/config/config.ini'
        config.read(file_path)
        # logger.info(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("设置测试浏览器为：% s" % browser)
        url = config.get(test_server, "URL")
        # logger.info("设置测试地址为: %s" % url)

        if browser == "Firefox":
            # 设置无头浏览器，运行脚本不显示浏览器界面，减少脚本运行时间
            # firefox_opt = webdriver.FirefoxOptions()
            # firefox_opt.add_argument("--headless")
            # driver = webdriver.Firefox(firefox_options=firefox_opt)

            # 启用浏览器界面
            driver = webdriver.Firefox()
            logger.info("Firefox浏览器启动")
        elif browser == "Chrome":
            # 设置无头浏览器，运行脚本不显示浏览器界面，减少脚本运行时间
            # chrome_opt = webdriver.ChromeOptions()
            # chrome_opt.add_argument("--headless")
            # driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=chrome_opt)

            # 启用浏览器界面
            driver = webdriver.Chrome()
            logger.info("Chrome浏览器启动")
        elif browser == "IE":
            # 设置无头浏览器，运行脚本不显示浏览器界面，减少脚本运行时间
            # ie_opt = webdriver.IeOptions()
            # ie_opt.add_argument("--headless")
            # driver = webdriver.Ie(self.ie_driver_path, ie_options=ie_opt)

            # 启用浏览器界面
            driver = webdriver.Ie()
            logger.info("IE浏览器启动")

        driver.maximize_window()
        logger.info("最大化浏览器界面")
        driver.implicitly_wait(10)
        logger.info("设置隐式等待，最大等待时间：10s")
        driver.get(url)
        logger.info("访问URL: %s" % url)
        logger.info("----------浏览器环境准备完成----------")
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("退出浏览器！")
