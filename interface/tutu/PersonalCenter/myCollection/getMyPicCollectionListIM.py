#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 17:13
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getMyPicCollectionListIM.py
# @Software: PyCharm
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger

class getMyPicCollectionListIM:

    def __init__(self):
        self.logger = Logger(logger="getMyPicCollectionListIM").getlog()

    def get_getMyPicCollectionListIMURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:个人中心-我的收藏（单图列表）
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL



    def send_request_getMyPicCollectionListIM(self,url,currentPage,pageSize,collectVersion=None):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "currentPage":currentPage,
                "pageSize":pageSize,
                "collectVersion":collectVersion
        }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
