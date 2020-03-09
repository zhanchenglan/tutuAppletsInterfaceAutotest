#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 14:21
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : queryTopicList4Fr.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class queryTopicList4Fr:

    def __init__(self):
        self.logger = Logger(logger="queryTopicList4Fr").getlog()

    def get_queryTopicList4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:话题列表
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("接口的URL为:%s" %ReallyURL)
        return ReallyURL



    def send_request_queryTopicList4Fr(self,url,searchTitle=None):
        '''
        :param url:
        :param searchTitle:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
                "searchTitle":searchTitle
        }
        self.logger.info("请求的参数为%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)