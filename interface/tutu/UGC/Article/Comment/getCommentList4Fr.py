#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 16:46
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : getCommentList4Fr.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class getCommentList4Fr:

    def __init__(self):
        self.logger = Logger(logger="getCommentList4Fr").getlog()

    def get_getCommentList4FrURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_getCommentList4Fr(self,url,articleId,currentPage,pageSize):
        '''

        :param url:
        :param articleId:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "articleId":articleId,
                "currentPage":currentPage,
                "pageSize":pageSize
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

