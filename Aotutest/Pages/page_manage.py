#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Vant
# @Email:944921374@qq.com

from selenium.webdriver.common.by import By
from Base.Selenium2 import BasePage
import sys
sys.path.append('../')

class pagemanage(BasePage):
    stu_id = (By.XPATH,'//*[@name="stu_id"]')
    # stu_id = (By.XPATH,'/html/body/form[2]/p[1]/input')
    stu_name = (By.XPATH,'//*[@name="stu_name"]')
    major = (By.XPATH,'//*[@name="major"]/option[3]')
    grade = (By.XPATH,'//*[@name="grade"]/option[3]')
    identity_id = (By.XPATH,'//*[@name="identity_id"]')
    email = (By.XPATH,'//*[@name="email"]')
    class1 =(By.XPATH,'//*[@name="class"]')
    teacher_name = (By.XPATH,'//*[@name="teacher_name"]')
    instructor_name = (By.XPATH,'//*[@name="instructor_name"]')
    update = (By.XPATH,'/html/body/form[2]/input[2]')

    title = (By.XPATH,'//*[@name="title"]')
    is_outstanding = (By.XPATH, '//*[@name="is_outstanding"]')
    content = (By.XPATH, '//*[@name="content"]')
    update_bs = (By.XPATH,'/html/body/form/input[2]')

    check = (By.XPATH,'/html/body/p')

    add = (By.XPATH,'/html/body/form/input[2]')

    def get_txt(self):
        return self.get_text(self.check)

    def update_stu_id(self,id):
        self.send_key(self.stu_id,id)
        self.click(self.update)
        self.back()

    def update_name(self,name):
        self.send_key(self.stu_name,name)
        self.click(self.update)

    def update_major(self):
        self.click(self.major)
        self.click(self.update)

    def update_grade(self):
        self.click(self.grade)
        self.click(self.update)

    def update_idcard(self,card):
        self.send_key(self.identity_id,card)
        self.click(self.update)

    def update_email(self,email):
        self.send_key(self.email,email)
        self.click(self.update)

    def update_teacher(self,name):
        self.send_key(self.teacher_name,name)
        self.click(self.update)

    def update_fu(self,name):
        self.send_key(self.instructor_name,name)
        self.click(self.update)

    def update_class(self,name):
        self.send_key(self.class1,name)
        self.click(self.update)

    def update_all_stu(self,name,card,email,cla,tename,funame):
        self.send_key(self.stu_name, name)
        self.click(self.major)
        self.click(self.grade)
        self.send_key(self.identity_id, card)
        self.send_key(self.email, email)
        self.send_key(self.teacher_name, tename)
        self.send_key(self.instructor_name, funame)
        self.send_key(self.class1, cla)
        self.click(self.update)

    def update_title(self,name):
        self.send_key(self.title,name)
        self.click(self.update_bs)

    def update_level(self,name):
        self.send_key(self.is_outstanding,name)
        self.click(self.update_bs)

    def update_content(self,name):
        self.send_key(self.content,name)
        self.click(self.update_bs)

    def update_all_bs(self,title,name,level,content):
        self.send_key(self.title,title)
        self.send_key(self.teacher_name,name)
        self.send_key(self.is_outstanding,level)
        self.send_key(self.content,content)
        self.click(self.update_bs)

    def add_all_stu(self,name,card,email,cla,tename,funame):
        self.send_key(self.stu_name, name)
        self.click(self.major)
        self.click(self.grade)
        self.send_key(self.identity_id, card)
        self.send_key(self.email, email)
        self.send_key(self.teacher_name, tename)
        self.send_key(self.instructor_name, funame)
        self.send_key(self.class1, cla)
        self.click(self.add)