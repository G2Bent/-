#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

import unittest
from Pages.page_login import loginPage
from Base.BrowserDriver import BrowserDriver
from time import sleep
import sys
sys.path.append('../')

class loginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls,'login_url')

    def setUp(self):
        self.log = loginPage(self.driver)
        self.url = 'http://127.0.0.1:8000/login/'

    def test_login01(self):
        '''账号为空'''
        self.driver.get(self.url)
        self.log.login('','root')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误',self.driver.page_source)

    def test_login02(self):
        '''密码为空'''
        self.driver.get(self.url)
        self.log.login('root','')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login03(self):
        '''账号错误'''
        self.driver.get(self.url)
        self.log.login('root1','root')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login04(self):
        '''密码错误'''
        self.driver.get(self.url)
        self.log.login('root','1234')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login05(self):
        '''账号密码合法性验证，账号前面带空格'''
        self.driver.get(self.url)
        self.log.login('  root', 'root')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login06(self):
        '''账号密码合法性验证，账号中间带空格'''
        self.driver.get(self.url)
        self.log.login('ro  ot', 'root')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login07(self):
        '''账号密码合法性验证，账号后面带空格'''
        self.driver.get(self.url)
        self.log.login('root  ', 'root')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login08(self):
        '''账号密码合法性验证，密码前面带空格'''
        self.driver.get(self.url)
        self.log.login('root', ' root')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login09(self):
        '''账号密码合法性验证，密码中间带空格'''
        self.driver.get(self.url)
        self.log.login('root', 'ro ot')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login10(self):
        '''账号密码合法性验证，密码后面带空格'''
        self.driver.get(self.url)
        self.log.login('root', 'root ')
        self.log.get_screent_img()
        self.assertIn('用户或密码错误', self.driver.page_source)

    def test_login81(self):
        '''登录成功'''
        self.driver.get(self.url)
        self.log.login('root', 'root')
        self.log.get_screent_img()
        self.assertIn('root', self.driver.page_source)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        pass

