#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 11:00
# @Author  : jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : getOrderDeatil.py
# @Software: PyCharm
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class getOrderDeatil:

    def __init__(self):
        self.logger = Logger(logger="getOrderDeatil").getlog()

    def get_getOrderDeatilURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
        :param baseURL:
        :param lang:
        :param timeStamp:
        :param clientVersionInfo:
        :param access_token:
        :return:个人租赁-订单详情
        '''
        getOrderDeatil = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
        lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("url为:%s" % getOrderDeatil)
        return getOrderDeatil

    def send_request_getOrderDeatil(self, url, orderNo):
        '''
        :param url:
        :param orderNo:
        :return:
        '''
        headers = {"Content-Type": "application/json"}

        parameters = {
            "orderNo": orderNo
        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    imi = getOrderDeatil()
    orderNo = "60688109297279696896"
    url = "https://mi-api-uat.nailtutu.com/imi/pay/personal/rent/order/mi/detail?lang=zh&timeStamp=20190911090313&clientVersionInfo=android_app_ch_1.0.4&access_token=6b9e94e4-feb7-481a-a4c3-3aaabdf0b304"
    imi.send_request_getOrderDeatil(url, orderNo)
