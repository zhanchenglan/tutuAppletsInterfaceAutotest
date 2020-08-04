#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 15:27
# @Author  : jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : createOrder.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger

class createOrder:

    def __init__(self):
        self.logger = Logger(logger="createOrder").getlog()

    def get_createOrderURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_createOrder(self,url,source,receivedId,orderGoodsList,remark=None):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "source":source,
                "receivedId":receivedId,
                "orderGoodsList":orderGoodsList,
                "remark":remark
        }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)