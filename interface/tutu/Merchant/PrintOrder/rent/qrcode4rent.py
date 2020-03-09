#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 11:21
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : qrcode4rent.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class qrcode4rent:


    def __init__(self):
        self.logger = Logger(logger="qrcode4rent").getlog()


    def get_qrcode4rentURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:生成二维码-租赁
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_qrcode4rent(self,url,sn):
        '''
        :param url:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
            "sn": sn
                 }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
