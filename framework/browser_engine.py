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
        file_path = os.path.dirname(
            os.path.abspath('.')) + '/autoTest2/config/config.ini'
        config.read(file_path)
        # logger.info(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get(test_server, "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            # 设置无头浏览器，运行脚本不显示浏览器界面，减少脚本运行时间
            firefox_opt = webdriver.FirefoxOptions()
            firefox_opt.add_argument("--headless")
            driver = webdriver.Firefox(firefox_options=firefox_opt)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            # 设置无头浏览器，运行脚本不显示浏览器界面，减少脚本运行时间
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.add_argument("--headless")
            driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=chrome_opt)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            # 设置无头浏览器，运行脚本不显示浏览器界面，减少脚本运行时间
            ie_opt = webdriver.IeOptions()
            ie_opt.add_argument("--headless")
            driver = webdriver.Ie(self.ie_driver_path, ie_options=ie_opt)
            logger.info("Starting IE browser.")

        driver.maximize_window()
        driver.get(url)
        logger.info("Open url: %s" % url)
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()