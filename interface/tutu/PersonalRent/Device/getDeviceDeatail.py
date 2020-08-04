#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 10:07
# @Author  : jina
# @Email   : jina.zhan@sunvalley.com.cn
# @File    : getGoodsList.py
# @Software: PyCharm
import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import json
import requests
from common.Logger import Logger


class getDeviceDeatail:

    def __init__(self):
        self.logger = Logger(logger="getDeviceDeatail").getlog()

    def get_getDeviceDeatailURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
            :param baseURL:
            :param lang:
            :param timeStamp:
            :param clientVersionInfo:
            :param access_token:
            :return:个人租赁设备详情
            '''
        getDeviceDeatailURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
            lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("url为:%s" % getDeviceDeatailURL)
        return getDeviceDeatailURL

    def send_request_getDeviceDeatail(self, url, id):
        '''
        :param url:
        :param id:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
            "id": id,
        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    imi = getDeviceDeatail()
    url = "https://mi-api-uat.nailtutu.com/imi/pay/personal/rent/device/mi/detail?lang=zh&timeStamp=20190911090313&clientVersionInfo=android_app_ch_1.0.4&access_token=6b9e94e4-feb7-481a-a4c3-3aaabdf0b304"
    id = "688109549013434368"
    imi.send_request_getDeviceDeatail(url, id)
