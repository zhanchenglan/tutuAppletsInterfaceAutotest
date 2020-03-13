#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 11:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : addAlbumsCommentComplaint.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger



class addAlbumsCommentComplaint:

    def __init__(self):
        self.logger = Logger(logger="addAlbumsCommentComplaint").getlog()

    def get_addAlbumsCommentComplaintURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:评论-投诉
        '''
        ReallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %ReallyURL)
        return ReallyURL



    def send_request_addAlbumsCommentComplaint(self,url,albumsId,commentId,replyType,uid,content,complaintType):
        '''
        :param url:
        :param albumsId:
        :param content:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "albumsId":albumsId,
                "commentId":commentId,
                "replyType":replyType,
                "uid":uid,
                "content":content,
                "complaintType":complaintType
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)
