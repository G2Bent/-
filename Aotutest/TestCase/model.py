#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

import unittest
from Pages.page_search import pagesearch
from Pages.page_login import loginPage
from Pages.page_manage import pagemanage
from Base.BrowserDriver import BrowserDriver
import sys
sys.path.append('../')

class ModelCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls,'login_url')
        cls.sear = pagesearch(cls.driver)
        cls.mana = pagemanage(cls.driver)
        cls.login = loginPage(cls.driver)
        cls.login.login('root','root')

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        pass

