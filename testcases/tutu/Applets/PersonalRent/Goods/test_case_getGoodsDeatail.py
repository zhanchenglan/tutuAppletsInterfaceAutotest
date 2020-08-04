#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/03/16 10:30
# @Author  : Jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : test_case_getGoodsDeatil.py
# @Software: PyCharm

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from common.excelUtil import excelUtil
from interface.tutu.PersonalRent.Goods.getGoodsList import getGoodsList
import random
from interface.tutu.PersonalRent.Goods.getGoodsDeatil import getGoodsDeatil


class TestPersonalRentFunc(unittest.TestCase):
    """Test PersonalRentFunc.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.ListQuery = getGoodsList()
        self.GoodsDeatil = getGoodsDeatil()

    def test_getGoodsDeatail_tutu_Android_001(self):
        '''美甲涂涂小程序移动Android端_个人租赁_获取商品详情_不登录_001'''
        # 第一步 客户端认证鉴权登录
        # 请求参数
        data = self.AC.get_WX_Not_logged_in()
        # 请求URL
        WX_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                        self.config.get("imi_login_url", "login_url"),
                                                        self.config.get("lang", "zh"), self.base.getTimeStamp(),
                                                        self.config.get("clientVersionInfo",
                                                                        "clientVersionInfo_ch_pad_1.0.34"))
        access_token = self.AC.get_Access_token_not_login(WX_login_url_ch, data)
        self.assertIsNotNone(access_token)

        # 第二步 获得测试用例里的参数，调商品列表接口
        TestData = self.ex.getDict(2, 36, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        # 获取商品列表接口请求URL
        ListQueryURL = self.ListQuery.get_getGoodsListURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                          self.config.get("PersonalRent", "getGoodsListURL"),
                                                          self.config.get("lang", "zh"),
                                                          self.base.getTimeStamp(),
                                                          self.config.get("clientVersionInfo",
                                                                          "clientVersionInfo_ch_Android"), access_token)

        result_ListQuery = self.ListQuery.send_request_getGoodsList(ListQueryURL, currentPage, pageSize)

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # print(result_ListQuery["data"])
        # 随机获取一个商品ID，作为商品详情的参数
        goodsId = random.choice(result_ListQuery["data"])["id"]
        #print(goodsId)
        #获取商品详情接口
        GoodsDeatilURL = self.GoodsDeatil.get_getGoodsDeatilURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("PersonalRent", "getGoodsDeatilURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(),
            self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),
            access_token)

        result_GoodsDeatil = self.GoodsDeatil.send_request_getGoodsDeatil(GoodsDeatilURL, goodsId)

        self.assertEqual(result_GoodsDeatil["stateCode"], 200)
        self.assertEqual(result_GoodsDeatil["stateMsg"], "OK")
        self.assertEqual(result_GoodsDeatil["data"]["id"], goodsId)

    def test_getGoodsDeatail_tutu_Android_002(self):
            '''美甲涂涂移动Android端_个人租赁商品详情_正常查询_手机号密码登录_002'''
            # 第一步，获取excel中的测试数据，调登录接口获取access_token
            TestData = self.ex.getDict(2, 37, 7, self.testData)
            currentPage = TestData["currentPage"]
            pageSize = TestData["pageSize"]

            phone = TestData["phone"]
            password = TestData["password"]
            data = self.AC.get_Android_CN_logged_in(phone, password)

            pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                             self.config.get("imi_login_url", "login_url"),
                                                             self.config.get("lang", "zh"), self.base.getTimeStamp(),
                                                             self.config.get("clientVersionInfo",
                                                                             "clientVersionInfo_ch_Android"))
            access_token = self.AC.get_Access_token(pad_login_url_ch, data)

            self.assertIsNotNone(access_token)

            # 第二步，调商品列表接口，获取商品id
            ListQueryURL = self.ListQuery.get_getGoodsListURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                              self.config.get("PersonalRent", "getGoodsListURL"),
                                                              self.config.get("lang", "zh"),
                                                              self.base.getTimeStamp(),
                                                              self.config.get("clientVersionInfo",
                                                                              "clientVersionInfo_ch_Android"),
                                                              access_token)

            result_ListQuery = self.ListQuery.send_request_getGoodsList(ListQueryURL, currentPage, pageSize)

            self.assertEqual(result_ListQuery["stateCode"], 200)
            self.assertEqual(result_ListQuery["stateMsg"], "OK")
            self.assertIsNotNone(result_ListQuery["data"])

            # 随机获取一个商品ID，作为商品详情的参数
            goodsId = random.choice(result_ListQuery["data"])["id"]
            # print(goodsId)
            # 获取商品详情接口
            GoodsDeatilURL = self.GoodsDeatil.get_getGoodsDeatilURL(
                self.config.get('imi_base_url_ch', 'base_url_prod'),
                self.config.get("PersonalRent", "getGoodsDeatilURL"), self.config.get("lang", "zh"),
                self.base.getTimeStamp(),
                self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),
                access_token)

            result_GoodsDeatil = self.GoodsDeatil.send_request_getGoodsDeatil(GoodsDeatilURL, goodsId)

            self.assertEqual(result_GoodsDeatil["stateCode"], 200)
            self.assertEqual(result_GoodsDeatil["stateMsg"], "OK")
            self.assertEqual(result_GoodsDeatil["data"]["id"], goodsId)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
