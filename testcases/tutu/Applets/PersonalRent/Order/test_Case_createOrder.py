#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 15:37
# @Author  : jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : test_case_createOrder.py
# @Software: PyCharm


import sys, os

from interface.tutu.PersonalRent.Goods.getGoodsList import getGoodsList
from interface.tutu.PersonalRent.Order.createOrder import createOrder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import random
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.Merchant.address.addressList import addressList

from common.excelUtil import excelUtil


class TestcreateOrderFunc(unittest.TestCase):
    """Test createOrder.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.goodsList = getGoodsList()
        self.addressList = addressList()
        self.createOrder = createOrder()

    def test_createOrder_tutu_Applets_001(self):
        '''美甲涂涂Applets端_商品列表_正常查询_手机号密码登录_001'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 27, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        # 登录
        phone = "13417335080"
        password = TestData["password"]
        data = self.AC.get_Applets_ordinary_logged_in(phone, password)
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                         self.config.get("imi_login_url", "login_url"),
                                                         self.config.get("lang", "zh"), self.base.getTimeStamp(),
                                                         self.config.get("clientVersionInfo",
                                                                         "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(pad_login_url_ch, data)
        self.assertIsNotNone(access_token)

        # 第二步：调获取商品列表接口，获得商品id
        goodsListURL = self.goodsList.get_getGoodsListURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                          self.config.get("PersonalRent", "getGoodsListURL"),
                                                          self.config.get("lang", "zh"),
                                                          self.base.getTimeStamp(),
                                                          self.config.get("clientVersionInfo",
                                                                          "clientVersionInfo_ch_Android"), access_token)
        result_goodsList = self.goodsList.send_request_getGoodsList(goodsListURL, currentPage, pageSize)

        self.assertEqual(result_goodsList["stateCode"], 200)
        self.assertEqual(result_goodsList["stateMsg"], "OK")

        # 第三步：调获取地址列表接口，获得receivedId
        addressListURL = self.addressList.get_addressListURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                             self.config.get("Merchant", "addressListURL"),
                                                             self.config.get("lang", "zh"),
                                                             self.base.getTimeStamp(),
                                                             access_token)

        result_addressList = self.addressList.send_request_addressList(addressListURL)

        self.assertEqual(result_addressList["stateCode"], 200)
        self.assertEqual(result_addressList["stateMsg"], "OK")

        # 第四步：调下单接口
        createOrderURL = self.createOrder.get_createOrderURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                             self.config.get("PersonalRent", "createOrderURL"),
                                                             self.config.get("lang", "zh"),
                                                             self.base.getTimeStamp(),
                                                             self.config.get("clientVersionInfo",
                                                                             "clientVersionInfo_ch_Android"),
                                                             access_token)
        source = 1
        receivedId = result_addressList["data"][0]["id"]
        orderGoodsList = []
        orderGoodsDict = {"goodsId": random.choice(result_goodsList["data"])["id"],
                          "amount": 1}
        orderGoodsList.append(orderGoodsDict)

        result_createOrder = self.createOrder.send_request_createOrder(createOrderURL, source, receivedId,
                                                                       orderGoodsList)

        self.assertEqual(result_createOrder["stateCode"], 200)
        self.assertEqual(result_createOrder["stateMsg"], "OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
