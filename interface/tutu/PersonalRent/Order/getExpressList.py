#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 15:07
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


class getExpressList:

    def __init__(self):
        self.logger = Logger(logger="getExpressList").getlog()

    def get_getExpressListURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
            :param baseURL:
            :param lang:
            :param timeStamp:
            :param clientVersionInfo:
            :param access_token:
            :return:个人租赁-快递公司列表查询
            '''
        getExpressListURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
            lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("url为:%s" % getExpressListURL)
        return getExpressListURL

    def send_request_getExpressListURL(self, url):
        '''
        :param url:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {

        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    imi = getExpressList()
