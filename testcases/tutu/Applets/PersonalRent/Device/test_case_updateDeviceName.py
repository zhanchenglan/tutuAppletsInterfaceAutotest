#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/03/18 10:12
# @Author  : Jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : test_case_getGoodsList.py
# @Software: PyCharm

import sys, os

from interface.tutu.PersonalRent.Device.getDeviceList import getDeviceList
from interface.tutu.PersonalRent.Device.updateDeviceName import updateDeviceName

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
        self.ListQuery = getDeviceList()
        self.updateQuery = updateDeviceName()

    def test_getOrderList_tutu_Android_001(self):
        '''美甲涂涂小程序移动Android端_个人租赁_获取订单列表_手机号密码登录查看列表_001'''
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

        # 获取设备列表接口请求URL
        ListQueryURL = self.ListQuery.get_getDeviceListURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                           self.config.get("PersonalRent", "getDeviceListURL"),
                                                           self.config.get("lang", "zh"),
                                                           self.base.getTimeStamp(),
                                                           self.config.get("clientVersionInfo",
                                                                           "clientVersionInfo_ch_Android"),
                                                           access_token)

        result_ListQuery = self.ListQuery.send_request_getDeviceList(ListQueryURL, currentPage, pageSize)

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # 选中其中一个设备的id,sn作为请求参数
        print(result_ListQuery["data"][0]["id"])
        print(result_ListQuery["data"][0]["sn"])
        id = result_ListQuery["data"][0]["id"]
        sn = result_ListQuery["data"][0]["sn"]
        devicesName = "myDevice"
        # 修改设备名称接口
        updateQueryURL = self.updateQuery.get_updateDeviceNameURL(self.config.get('imi_base_url_ch', 'base_url_uat'),
                                                                  self.config.get("PersonalRent",
                                                                                  "updateDeviceNameURL"),
                                                                  self.config.get("lang", "zh"),
                                                                  self.base.getTimeStamp(),
                                                                  self.config.get("clientVersionInfo",
                                                                                  "clientVersionInfo_ch_Android"),
                                                                  access_token)

        result_ListQuery = self.updateQuery.send_request_updateDeviceName(updateQueryURL, id, sn, devicesName)

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
