#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 11:20
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_getPicList4MiByidOrTag.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.gallery.getPicList4MiByidOrTag import getPicList4MiByidOrTag
from interface.tutu.gallery.getPicList4HotMi import getPicList4HotMi
from interface.tutu.gallery.getPicDetailForMi import getPicDetailForMi

from common.excelUtil import excelUtil


class TestgetPicList4MiByidOrTagFunc(unittest.TestCase):
    """Test getPicList4MiByidOrTag.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.search = getPicList4MiByidOrTag()
        self.Recommendations = getPicList4HotMi()
        self.getPicDetail = getPicDetailForMi()


    def test_getPicList4MiByidOrTag_tutu_Applets_001(self):
        '''美甲涂涂Applets端_彩绘图库搜索_标签名查询_手机号密码登录_001'''
        # 第一步，获取excel中的测试数据
        TestData = self.ex.getDict(2, 5, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]
        name = TestData["name"]

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
        searchURL = self.search.get_getPicList4MiByidOrTagURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicList4MiByidOrTagURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第七步，发送请求
        result = self.search.send_request_getPicList4MiByidOrTag(searchURL,currentPage,pageSize,name)

        # 第八步，断言返回的数据是否正确
        self.assertEqual(result["stateCode"], 200)
        self.assertEqual(result["stateMsg"], "OK")



    def test_getPicList4MiByidOrTag_tutu_Applets_002(self):
        '''美甲涂涂Applets端_彩绘图库搜索_ID查询_手机号密码登录_002'''
        TestData = self.ex.getDict(2, 17, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        #安卓登录
        phone = "13536764015"
        password = TestData["password"]
        data = self.AC.get_Applets_ordinary_logged_in(phone, password)
        pad_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(pad_login_url_ch,data)

        self.assertIsNotNone(access_token)

        #热门推荐
        RecommendationsURL = self.Recommendations.get_getPicList4HotMiURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicList4HotMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_Recommendations = self.Recommendations.send_request_getPicList4HotMi(RecommendationsURL,currentPage,pageSize)

        self.assertEqual(result_Recommendations["stateCode"], 200)
        self.assertEqual(result_Recommendations["stateMsg"], "OK")

        # #取热门推荐返回的第一张图片的ID
        ID = result_Recommendations["data"][0]["id"]
        #定义为系统图库类型
        collectionType = "系统图库"

        #取单张图片详情
        getPicDetailURL = self.getPicDetail.get_getPicDetailForMiURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicDetailForMiURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        result_getPicDetail = self.getPicDetail.send_request_getPicDetailForMi(getPicDetailURL,ID,collectionType)

        self.assertEqual(result_getPicDetail["stateCode"], 200)
        self.assertEqual(result_getPicDetail["stateMsg"], "OK")




        #彩绘图库搜索
        galleryOutId = result_getPicDetail["data"]["galleryOutId"]
        searchURL = self.search.get_getPicList4MiByidOrTagURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getPicList4MiByidOrTagURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        # 第七步，发送请求
        result_search = self.search.send_request_getPicList4MiByidOrTag(searchURL,currentPage,pageSize,galleryOutId)

        # 第八步，断言返回的数据是否正确
        self.assertEqual(result_search["stateCode"], 200)
        self.assertEqual(result_search["stateMsg"], "OK")
        self.assertEqual(result_search["totalNum"], 1)



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


