#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/03/17 14:15
# @Author  : Jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : test_case_getGoodsList.py
# @Software: PyCharm
import random
import sys, os

from interface.tutu.Merchant.address.addressList import addressList
from interface.tutu.PersonalRent.Goods.getGoodsList import getGoodsList
from interface.tutu.PersonalRent.Order.cancelOrder import cancelOrder
from interface.tutu.PersonalRent.Order.createOrder import createOrder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from common.excelUtil import excelUtil


class TestPersonalRentFunc(unittest.TestCase):
    """Test PersonalRentFunc.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.goodsListQuery = getGoodsList()
        self.addressList = addressList()
        self.createOrder = createOrder()
        self.ListQuery = cancelOrder()

    def test_getOrderList_tutu_Android_001(self):
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

        # 获取商品列表
        goodsListURL = self.goodsListQuery.get_getGoodsListURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                               self.config.get("PersonalRent", "getGoodsListURL"),
                                                               self.config.get("lang", "zh"),
                                                               self.base.getTimeStamp(),
                                                               self.config.get("clientVersionInfo",
                                                                               "clientVersionInfo_ch_Android"),
                                                               access_token)
        result_goodsList = self.goodsListQuery.send_request_getGoodsList(goodsListURL, currentPage, pageSize)

        self.assertEqual(result_goodsList["stateCode"], 200)
        self.assertEqual(result_goodsList["stateMsg"], "OK")

        # 获取地址列表
        addressListURL = self.addressList.get_addressListURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                             self.config.get("Merchant", "addressListURL"),
                                                             self.config.get("lang", "zh"),
                                                             self.base.getTimeStamp(),
                                                             access_token)

        result_addressList = self.addressList.send_request_addressList(addressListURL)

        self.assertEqual(result_addressList["stateCode"], 200)
        self.assertEqual(result_addressList["stateMsg"], "OK")

        # #下单
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
        print("订单号为：", result_createOrder["data"])

        # 第三步 取消订单接口
        # 请求URL
        ListQueryURL2 = self.ListQuery.get_getOrderListURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                           self.config.get("PersonalRent", "cancelOrderURL"),
                                                           self.config.get("lang", "zh"),
                                                           self.base.getTimeStamp(),
                                                           self.config.get("clientVersionInfo",
                                                                           "clientVersionInfo_ch_Android"),
                                                           access_token)

        # 请求参数
        result_ListQuery = self.ListQuery.send_request_cancelOrder(ListQueryURL2, result_createOrder["data"])

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
