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


class updateDeviceName:

    def __init__(self):
        self.logger = Logger(logger="updateDeviceName").getlog()

    def get_updateDeviceNameURL(self, baseURL, URL, lang, timeStamp, clientVersionInfo, access_token):
        '''
            :param baseURL:
            :param lang:
            :param timeStamp:
            :param clientVersionInfo:
            :param access_token:
            :return:个人租赁--修改设备名称
            '''
        updateDeviceNameURL = baseURL + URL + "?lang=%s&timeStamp=%s&clientVersionInfo=%s&access_token=%s" % (
            lang, timeStamp, clientVersionInfo, access_token)
        self.logger.info("url为:%s" % updateDeviceNameURL)
        return updateDeviceNameURL

    def send_request_updateDeviceName(self, url, id, sn, deviceName):
        '''
        :param url:
        :param id:
        :param sn:
        :param deviceName:
        :return:
        '''
        headers = {"Content-Type": "application/json"}
        parameters = {
            "id": id,
            "sn": sn,
            "deviceName": deviceName,
        }
        self.logger.info("请求的参数为:%s" % parameters)
        r = requests.post(url, data=json.dumps(parameters), headers=headers, timeout=30)
        self.logger.info("返回的参数为:%s" % json.loads(r.text))
        return json.loads(r.text)


if __name__ == "__main__":
    imi = updateDeviceName()
