#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 10:07
# @Author  : jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : getGoodsList.py
# @Software: PyCharm
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.baseUtil import baseUtils
from common.Logger import Logger
from common.FileParsing import FileParser


class getDeviceList:

    def __init__(self):
        self.logger = Logger(logger="getDeviceList").getlog()

    def get_getDeviceListURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
            :param baseURL:
            :param lang:
            :param timeStamp:
            :param clientVersionInfo:
            :param access_token:
            :return:个人租赁设备-列表查询
            '''
        getDeviceListURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
            lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("url为:%s" % getDeviceListURL)
        return getDeviceListURL

    def send_request_getDeviceList(self, url, currentPage, pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
            "pageSize": pageSize,
            "currentPage": currentPage,
        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    imi = getDeviceList()
    url = "https://mi-api-uat.nailtutu.com/imi/pay/personal/rent/device/mi/list?lang=zh&timeStamp=20190911090313&clientVersionInfo=android_app_ch_1.0.4&access_token=6b9e94e4-feb7-481a-a4c3-3aaabdf0b304"
    imi.send_request_getDeviceList(url, 1, 10)
