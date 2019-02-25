#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Vant
# @Email:944921374@qq.com
from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage
import sys
sys.path.append('../')

class loginPage(BasePage):
    user_input = (By.XPATH,"//*[@name='name']")
    passwd_input = (By.XPATH,"//*[@name='password']")
    submit_btn = (By.XPATH,"/html/body/form/input[4]")

    def login(self,name,password):
        self.send_key(self.user_input,name)
        self.send_key(self.passwd_input,password)
        self.click(self.submit_btn)