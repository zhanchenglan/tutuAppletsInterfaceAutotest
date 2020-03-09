#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 9:57
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : common.py
# @Software: PyCharm

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger
import warnings


class common:


    def __init__(self):
        self.logger = Logger(logger="common").getlog()
        warnings.simplefilter("ignore",ResourceWarning)


    def get_commonURL(self,baseURL,URL,lang,timeStamp,clientVersionInfo,access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :return:单图片上传（通用版）
        '''
        reallyURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (lang, timeStamp, clientVersionInfo,access_token)
        self.logger.info("url为:%s" %reallyURL)
        return reallyURL

    def send_request_common(self,url,file,directory):
        '''
        :param url:
        :param content:
        :return:
        '''
        # headers = {"Content-Type": "multipart/form-data"}
        # parameters = {
        #     "file": file,
        #     "directory":directory
        #          }
        files = {"file": (file, open(directory, "rb"), "multipart/form-data", {})}

        self.logger.info("请求的参数为:%s" %files)
        r = requests.post(url, files=files,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)













