#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Vant
# @Email   : 944921374@qq.com

from TestCase.model import ModelCase
from time import sleep
import sys
sys.path.append('../')

class searchCase(ModelCase):
    def test_search01(self):
        '''查询专业学生信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        for i in range(1,5):
            self.sear.search_major(i)
            sleep(3)

    def test_search02(self):
        '''查询年级学生信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        for i in range(1,5):
            self.sear.search_grade(i)
            sleep(3)

    def test_seach03(self):
        '''查询所有学生信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_all()

    def test_search04(self):
        '''查询学生基本信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(2)

    def test_search05(self):
        '''查询学生毕业设计信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(3)

    def test_search06(self):
        '''查询学生实习信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(4)

    def test_search07(self):
        '''查询学生工作信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(5)

    def test_search08(self):
        '''查询学生项目信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(6)

    def test_search09(self):
        '''查询学生交流建议信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(7)

    def test_search10(self):
        '''查询学生工作评价信息'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(8)

    def test_search11(self):
        '''查询学生综合评价'''
        self.driver.get('http://127.0.0.1:8000/majorsearch/')
        self.sear.search_basic(9)

