#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 14:22
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_getPicDetailForMi.py
# @Software: PyCharm


import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.gallery.getPicList4HotMi import getPicList4HotMi
from interface.tutu.gallery.getPicDetailForMi import getPicDetailForMi
from common.excelUtil import excelUtil




class TestgetPicDetailForMiFunc(unittest.TestCase):
    """Test getPicDetailForMi.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.Recommendations = getPicList4HotMi()
        self.Detail = getPicDetailForMi()


    def test_getPicDetailForMi_tutu_Applets_001(self):
        '''美甲涂涂Applets端_取单张图片详情_系统图库_手机号密码登录_001'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 9, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        allNailSuitFlag = TestData["allNailSuitFlag"]

        # 第二步，组装要登录的数据
        phone = "13536764015"
        password = TestData["password"]
        data = self.AC.get_Applets_ordinary_logged_in(phone, password)

        # 第三步，组装登录的URL
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))


        # 第四步，登录
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        # 第五步，断言判断是否登录成功
        self.assertIsNotNone(access_token)

        # 第六步，组装接口的URL
        RecommendationsURL = self.Recommendations.get_getPicList4HotMiURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicList4HotMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第七步，发送请求
        result_Recommendations = self.Recommendations.send_request_getPicList4HotMi(RecommendationsURL,currentPage,pageSize,allNailSuitFlag)

        # 第八步，断言返回的数据是否正确
        self.assertEqual(result_Recommendations["stateCode"], 200)
        self.assertEqual(result_Recommendations["stateMsg"], "OK")

        #取热门推荐返回的第一张图片的ID
        ID = result_Recommendations["data"][0]["id"]

        #第九步，系统图库
        collectionType = TestData["collectionType"]
        DetailURL = self.Detail.get_getPicDetailForMiURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicDetailForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Detail = self.Detail.send_request_getPicDetailForMi(DetailURL,ID,collectionType)

        #第十步，断言返回的数据是否正确
        self.assertEqual(result_Detail["stateCode"],200)
        self.assertEqual(result_Detail["stateMsg"], "OK")
        self.assertEqual(result_Detail["data"]["id"],ID)

    @unittest.skip("跳过")
    def test_getPicDetailForMi_Android_ch_002(self):
        '''美甲涂涂端_取单张图片详情_zh_Android_系统图库_鉴权登录'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 10, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        allNailSuitFlag = TestData["allNailSuitFlag"]

        # 第二步，组装要登录的数据
        data = self.AC.get_Android_CN_Not_logged_in()

        # 第三步，组装登录的URL
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))


        # 第四步，登录
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        # 第五步，断言判断是否登录成功
        self.assertIsNotNone(access_token)

        # 第六步，组装接口的URL
        RecommendationsURL = self.Recommendations.get_getPicList4HotMiURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicList4HotMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第七步，发送请求
        result_Recommendations = self.Recommendations.send_request_getPicList4HotMi(RecommendationsURL,currentPage,pageSize,allNailSuitFlag)

        # 第八步，断言返回的数据是否正确
        self.assertEqual(result_Recommendations["stateCode"], 200)
        self.assertEqual(result_Recommendations["stateMsg"], "OK")

        #取热门推荐返回的第一张图片的ID
        ID = result_Recommendations["data"][0]["id"]

        #第九步，系统图库
        collectionType = TestData["collectionType"]
        DetailURL = self.Detail.get_getPicDetailForMiURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicDetailForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Detail = self.Detail.send_request_getPicDetailForMi(DetailURL,ID,collectionType)

        #第十步，断言返回的数据是否正确
        self.assertEqual(result_Detail["stateCode"],200)
        self.assertEqual(result_Detail["stateMsg"], "OK")
        self.assertEqual(result_Detail["data"]["id"],ID)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
