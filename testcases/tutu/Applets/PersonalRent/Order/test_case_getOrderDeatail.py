#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/03/16 15:53
# @Author  : Jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : test_case_getOrderDeatil.py
# @Software: PyCharm

import os
import sys

from interface.tutu.PersonalRent.Order.getOrderDeatil import getOrderDeatil
from interface.tutu.PersonalRent.Order.getOrderList import getOrderList

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from common.excelUtil import excelUtil
import random


class TestPersonalRentFunc(unittest.TestCase):
    """Test PersonalRentFunc.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.ListQuery = getOrderList()
        self.OrderDeatil = getOrderDeatil()

    def test_getGoodsDeatail_tutu_Android_001(self):
            '''美甲涂涂移动Android端_个人租赁订单详情_正常查询_手机号密码登录_002'''
            # 第一步，获取excel中的测试数据，调登录接口获取access_token
            TestData = self.ex.getDict(2, 37, 7, self.testData)
            currentPage = TestData["currentPage"]
            pageSize = TestData["pageSize"]

            phone = TestData["phone"]
            password = TestData["password"]
            data = self.AC.get_Android_CN_logged_in(phone, password)

            pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                             self.config.get("imi_login_url", "login_url"),
                                                             self.config.get("lang", "zh"), self.base.getTimeStamp(),
                                                             self.config.get("clientVersionInfo",
                                                                             "clientVersionInfo_ch_Android"))
            access_token = self.AC.get_Access_token(pad_login_url_ch, data)

            self.assertIsNotNone(access_token)

            # 获取订单列表接口请求URL
            ListQueryURL = self.ListQuery.get_getOrderListURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                              self.config.get("PersonalRent", "getOrderListURL"),
                                                              self.config.get("lang", "zh"),
                                                              self.base.getTimeStamp(),
                                                              self.config.get("clientVersionInfo",
                                                                              "clientVersionInfo_ch_Android"),
                                                              access_token)

            result_ListQuery = self.ListQuery.send_request_getOrderList(ListQueryURL, currentPage, pageSize)

            self.assertEqual(result_ListQuery["stateCode"], 200)
            self.assertEqual(result_ListQuery["stateMsg"], "OK")
            self.assertIsNotNone(result_ListQuery["data"])

            # 随机获取一个订单号，作为订单详情的参数
            orderNo = random.choice(result_ListQuery["data"])["orderNo"]
            # print(orderNo)
            # 获取订单详情接口
            OrderDeatilURL = self.OrderDeatil.get_getOrderDeatilURL(
                self.config.get('imi_base_url_ch', 'base_url_uat'),
                self.config.get("PersonalRent", "getOrderDeatilURL"), self.config.get("lang", "zh"),
                self.base.getTimeStamp(),
                self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),
                access_token)

            result_GoodsDeatil = self.OrderDeatil.send_request_getOrderDeatil(OrderDeatilURL, orderNo)

            self.assertEqual(result_GoodsDeatil["stateCode"], 200)
            self.assertEqual(result_GoodsDeatil["stateMsg"], "OK")
            self.assertEqual(result_GoodsDeatil["data"]["orderNo"], orderNo)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
