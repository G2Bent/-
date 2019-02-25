#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Vant
# @Email:944921374@qq.com

from TestCase.model import ModelCase
from time import sleep
import sys
sys.path.append('../')

class manageCase(ModelCase):
    url = 'http://127.0.0.1:8000/majorsearchupdate/'

    def test_manage01(self):
        '''修改姓名成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_name('kkkk')
        sleep(2)
        self.assertEqual('success',self.mana.get_txt())

    def test_manage02(self):
        '''修改失败'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_name('')
        self.assertEqual('请将信息填写完整',self.mana.get_txt())

    def test_manage03(self):
        '''修改专业名称成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_major()
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage04(self):
        '''修改年级成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_grade()
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage05(self):
        '''修改身份证号码成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_idcard('550022212233')
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage06(self):
        '''修改身份证号码失败'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_idcard('')
        self.assertEqual('请将信息填写完整', self.mana.get_txt())

    def test_manage07(self):
        '''修改邮箱成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_email('233@qq.com')
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage08(self):
        '''修改邮箱失败'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_email('')
        self.assertEqual('请将信息填写完整', self.mana.get_txt())

    def test_manage09(self):
        '''修改班级成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_class('信息工程3班')
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage10(self):
        '''修改班级失败'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_class('')
        self.assertEqual('请将信息填写完整', self.mana.get_txt())

    def test_manage11(self):
        '''修改导师成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_teacher('奚老师')
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage12(self):
        '''修改老师失败'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_teacher('')
        self.assertEqual('请将信息填写完整', self.mana.get_txt())

    def test_manage13(self):
        '''修改辅导员成功'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_fu('奚看框')
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage14(self):
        '''修改辅导员失败'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_fu('')
        self.assertEqual('请将信息填写完整', self.mana.get_txt())

    # def test_manage15(self):
    #     '''删除学生成功'''
    #     self.driver.get(self.url)
    #     self.sear.dele_stu()

    def test_manage16(self):
        '''修改学生信息'''
        self.driver.get(self.url)
        self.sear.manage_basic(2)
        self.mana.update_all_stu('nihao','888888888888888','9923838@qq.com','国贸2班','赴大陆','看框架')
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())

    def test_manage17(self):
        '''修改毕业信息'''
        self.driver.get(self.url)
        self.sear.manage_basic(3)
        self.mana.update_all_bs('毕业设计题目','昆西','优秀','墨迹墨迹墨迹门口思考思考思考')
        sleep(2)
        self.assertEqual('success', self.mana.get_txt())







