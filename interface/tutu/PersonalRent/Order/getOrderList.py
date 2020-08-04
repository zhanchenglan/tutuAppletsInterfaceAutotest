#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 15:07
# @Author  : jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : getOrderList.py
# @Software: PyCharm
import sys,os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger

class getOrderList:

    def __init__(self):
        self.logger = Logger(logger="getOrderList").getlog()

    def get_getOrderListURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
            '''
            :param baseURL:
            :param lang:
            :param timeStamp:
            :param clientVersionInfo:
            :param access_token:
            :return:个人租赁--订单列表查询
            '''
            getGoodsListURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
            lang, timeStamp, clientVersionInfo, access_token)
            self.logger.info("url为:%s" % getGoodsListURL)
            return getGoodsListURL

    def send_request_getOrderList(self,url,currentPage,pageSize):
        '''
        :param url:
        :param currentPage:
        :param pageSize:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
                "pageSize":pageSize,
                "currentPage":currentPage,
            }
        self.logger.info("请求的参数为:%s" %parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers,timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)

if __name__ == "__main__":
    imi = getOrderList()
    url = "https://mi-api-uat.nailtutu.com/imi/pay/personal/rent/order/mi/list?lang=zh&timeStamp=20190911090313&clientVersionInfo=android_app_ch_1.0.4&access_token=6b9e94e4-feb7-481a-a4c3-3aaabdf0b304"
    imi.send_request_getOrderList(url,1,10)
