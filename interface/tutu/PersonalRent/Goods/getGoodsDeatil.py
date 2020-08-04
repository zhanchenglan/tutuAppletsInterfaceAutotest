#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 11:00
# @Author  : jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : getGoodsDeatil.py
# @Software: PyCharm
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class getGoodsDeatil:

    def __init__(self):
        self.logger = Logger(logger="getGoodsDeatil").getlog()

    def get_getGoodsDeatilURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:个人租赁-商品详情
        '''
        getGoodsDeatil = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
        lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("url为:%s" % getGoodsDeatil)
        return getGoodsDeatil

    def send_request_getGoodsDeatil(self, url, goodsId):
        '''
        :param url:
        :param goodsId:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
            "goodsId": goodsId
        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    imi = getGoodsDeatil()
    goodsId = "689067843362226176"
    url = "https://mi-api.nailtutu.com/imi/pay/personal/rent/goods/mi/detail?lang=zh&timeStamp=20190911090313&clientVersionInfo=android_app_ch_1.0.4&access_token=f3235564-4d37-48a3-a9a7-73c01501eeff"
    imi.send_request_getGoodsDeatil(url, goodsId)
