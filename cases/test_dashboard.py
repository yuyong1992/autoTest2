# coding:utf-8

import unittest
from autoSinnetCloud.pages.dashboard_page import DashBoardPage
from autoSinnetCloud.framework.browser_engine import BrowserEngine


class LinkClick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine()
