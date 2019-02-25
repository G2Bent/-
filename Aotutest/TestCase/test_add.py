#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Vant
# @Email:944921374@qq.com
from TestCase.model import ModelCase
from time import sleep
import sys
sys.path.append('../')

class testadd(ModelCase):
    url = 'http://127.0.0.1:8000/baseinfoinsert/'

    def test_add01(self):
        '''添加学生信息'''
        self.driver.get(self.url)
        self.mana.add_all_stu('nihao', '888888888888888', '9923838@qq.com', '国贸2班', '赴大陆', '看框架')
        sleep(2)