#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 9:54
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : deleteAlbumsComment.py
# @Software: PyCharm


import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class deleteAlbumsComment:

    def __init__(self):
        self.logger = Logger(logger="deleteAlbumsComment").getlog()

    def get_deleteAlbumsCommentURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:删除专辑评论
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_deleteAlbumsComment(self,url,commentId,completeDel):
        '''

        :param url:
        :param commentId:
        :param completeDel:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "commentId":commentId,
                "completeDel":completeDel
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

