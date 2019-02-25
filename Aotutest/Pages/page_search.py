#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Vant
# @Email:944921374@qq.com

from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage
import sys
sys.path.append('../')

class pagesearch(BasePage):
    search_btn = (By.XPATH,'/html/body/a[1]/font/font')#点击查询学生信息
    major_select = (By.XPATH,'//*[@name = "major"]')#点击专业
    grade_select = (By.XPATH,'//*[@name = "grade"]')#点击年级
    submit_btn = (By.XPATH,'/html/body/form/input[2]')#点击查询
    back_btn = (By.XPATH,'/html/body/form/input[3]')#点击返回
    search_form = (By.XPATH,'//*[@id="ta"]/tbody/tr[2]/td[5]/form/input[2]')

    dele= (By.XPATH,'//*[@id="ta"]/tbody/tr[2]/td[5]/form/input[10]')

    def select_major(self,num):
        major_option = (By.XPATH,'//*[@name = "major"]/option[%s]'%num)#选择第一个专业
        return major_option

    def select_grade(self,num):
        grade_option = (By.XPATH,'//*[@name = "grade"]/option[%s]'%num)
        return grade_option

    def select_formation(self,num):
        formation = (By.XPATH,'//*[@id="ta"]/tbody/tr[2]/td[5]/form/input[%s]'%num)
        return formation

    def search_major(self,num):
        self.click(self.select_major(num))
        self.click(self.submit_btn)

    def search_grade(self,num):
        self.click(self.select_grade(num))
        self.click(self.submit_btn)

    def search_all(self):
        self.click(self.submit_btn)

    def search_basic(self,num):
        self.click(self.submit_btn)
        self.click(self.select_formation(num))
        self.back()

    def manage_basic(self,num):
        self.click(self.submit_btn)
        self.click(self.select_formation(num))

    def dele_stu(self):
        self.click(self.submit_btn)
        self.click(self.dele_stu())

