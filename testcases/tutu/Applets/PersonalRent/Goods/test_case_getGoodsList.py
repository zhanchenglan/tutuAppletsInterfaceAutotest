#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/03/15 12:12
# @Author  : Jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : test_case_getGoodsList.py
# @Software: PyCharm

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from common.excelUtil import excelUtil
from interface.tutu.PersonalRent.Goods.getGoodsList import getGoodsList


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

    def test_getGoodsList_tutu_Android_001(self):
        '''美甲涂涂小程序移动Android端_个人租赁_获取商品列表_不登录可以查看列表_001'''
        # 第一步 鉴权登录接口美甲涂涂小程序登录请求参数
        data = self.AC.get_WX_Not_logged_in()
        # 请求URL
        WX_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                        self.config.get("imi_login_url", "login_url"),
                                                        self.config.get("lang", "zh"), self.base.getTimeStamp(),
                                                        self.config.get("clientVersionInfo",
                                                                        "clientVersionInfo_ch_pad_1.0.34"))
        access_token = self.AC.get_Access_token_not_login(WX_login_url_ch, data)
        self.assertIsNotNone(access_token)

        # 第二步 获得测试用例里的参数
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

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
