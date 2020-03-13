#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 20:50
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test.py
# @Software: PyCharm

import hashlib
import time
import datetime
import random
import string
import sys, os
from faker import Faker

class baseUtils:
    def __init__(self):
        pass

    @classmethod
    def MD5(self,str):
        '''
        :param str:
        :return: MD5 encryption
        '''
        m = hashlib.md5()
        b = str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    @classmethod
    def getTimeStamp(self):
        '''
        :return: str
        '''
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tempList = now.split(" ")
        return ("".join(tempList[0].split("-")) + "".join(tempList[1].split(":")))


    def timestamp_to_str(self,timeStamp=None, format='%Y-%m-%d %H:%M:%S'):
        if timeStamp:
            time_tuple = time.localtime(timeStamp)  # 把时间戳转换成时间元祖
            result = time.strftime(format, time_tuple)  # 把时间元祖转换成格式化好的时间
            return result
        else:
            return time.strptime(format)


    def str_to_timestamp(self,str_time=None, format='%Y-%m-%d %H:%M:%S'):
        if str_time:
            time_tuple = time.strptime(str_time, format)  # 把格式化好的时间转换成元祖
            result = time.mktime(time_tuple)  # 把时间元祖转换成时间戳
            return int(result)
        return int(time.time())



    def get_random_string(self,number):
        '''只能产生最多50'''
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, number))
        return  ran_str


    def get_millisecond(self):
        millis = int(round(time.time() * 1000))
        return millis

    def get_miniRectWidth(self):
        number = random.randint(100,130)
        return number


    def str2int(self,str):
        return int(str)


    def getToDay(self):
        return datetime.date.today()


    def chooseTwoAgentId(self,dict):
        if dict["supplierCompanyName"] == "深圳市丹芽科技":
            return dict["twoAgentId"]
        else:
            return None

    def choosePlan(self,dict):
        if dict["title"] == "美甲机租赁":
            return dict["id"]
        else:
            return None

    def get_random_content(self):
        Myfake = Faker(locale='zh_CN')
        content = Myfake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        return content


    def getProjectPath(self):
        #projectName = "AnjouAutotest"
        projectName = "tutuAppletsAutoTest"
        projectPath = os.path.dirname(os.path.abspath('.'))
        aList = projectPath.split(projectName)
        bList = aList[0].split(os.sep)
        reallyProject = os.sep.join(bList[0:-1])+os.sep+projectName
        return reallyProject


    def get_deviceID(self,dict):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get('sn')
                if res != None:
                    result.append(lst.get('id'))
        except:
            raise Exception('error')
        finally:
            return result


    def get_commentIDORreplyID(self,dict,content):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get("content")
                if res == content:
                    result.append(lst.get('id'))
        except:
            raise Exception('error')
        finally:
            return result[0]

    def get_commentUID(self,dict,content):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get("content")
                if res == content:
                    result.append(lst.get('uid'))
        except:
            raise Exception('error')
        finally:
            return result[0]



    def get_nailSuitStatus_for_1(self,dict):
        result = []
        try:
            data = dict.get('data')
            for lst in data:
                res = lst.get('nailSuitStatus')
                if res == 1:
                    result.append(lst.get('albumsId'))
        except:
            raise Exception('error')
        finally:
            return result


#     def get_end_time(self,start_time,duration_time)：
#          pass
#
#
#
if __name__ == "__main__":
    BU = baseUtils()
    print(BU.getTimeStamp())

#     str = "123456"
#
#     print('MD5加密前为 ：' + str)
#     print('MD5加密后为 ：' + BU.MD5(str))
#
#     re = BU.get_random_string(50)
#     print(re*10)
#
#
#     print(BU.get_millisecond())
#
#     test = BU.get_miniRectWidth()
#     print(test)
#
#     print(BU.getProjectPath())

    # print(BU.getToDay())
    # print(type(BU.getToDay()))


test_dict = {
	'stateCode': 200,
	'stateMsg': 'OK',
	'currentPage': 1,
	'pageSize': 15,
	'totalNum': 6,
	'totalPage': 1,
	'data': [{
		'id': '345d72cb41154e1a8e1ec66bcda28c26',
		'albumsId': '1f54943239854c8a8225c6a4e9c5b37b',
		'uid': '99d50784ad6b413180e180ef26cc83f8',
		'nickname': '涂涂6714',
		'headPortrait': 'https://cdn-dev.nailtutu.com/tutu/anjou/headportrait/20191226153320705_559222.png_th_132x132.png',
		'contentStatus': 1,
		'content': '标题情况时间北京.',
		'replyCount': 0,
		'nextGradeReplyCount': 0,
		'createTime': '2020-03-12 10:10:22'
	}, {
		'id': '5b082af02a00488e9f31df1cd2aff210',
		'albumsId': '1f54943239854c8a8225c6a4e9c5b37b',
		'uid': '99d50784ad6b413180e180ef26cc83f8',
		'nickname': '涂涂6714',
		'headPortrait': 'https://cdn-dev.nailtutu.com/tutu/anjou/headportrait/20191226153320705_559222.png_th_132x132.png',
		'contentStatus': 1,
		'content': '商品社区成功对于产品通过.',
		'replyCount': 0,
		'nextGradeReplyCount': 0,
		'createTime': '2020-03-12 10:09:35'
	}, {
		'id': 'b52ef8b867cc4d7c9dbbe5aaa5aa2360',
		'albumsId': '1f54943239854c8a8225c6a4e9c5b37b',
		'uid': '99d50784ad6b413180e180ef26cc83f8',
		'nickname': '涂涂6714',
		'headPortrait': 'https://cdn-dev.nailtutu.com/tutu/anjou/headportrait/20191226153320705_559222.png_th_132x132.png',
		'contentStatus': 1,
		'content': '科技首页作品电脑您的工具.',
		'replyCount': 0,
		'nextGradeReplyCount': 0,
		'createTime': '2020-03-12 10:06:32'
	}, {
		'id': 'f9ac2f49b8904e83971c7aaa8abc1654',
		'albumsId': '1f54943239854c8a8225c6a4e9c5b37b',
		'uid': '368e2306b72b41b7a88bf784d98da59a',
		'nickname': '文',
		'headPortrait': 'https://cdn-dev.nailtutu.com/tutu/anjou/headportrait/20190916150201203_629345.png',
		'contentStatus': 1,
		'content': '我分',
		'replyCount': 0,
		'nextGradeReplyCount': 0,
		'createTime': '2019-12-05 14:46:54'
	}, {
		'id': 'd4e76527b4ef4a769165d1ba1c7b5829',
		'albumsId': '1f54943239854c8a8225c6a4e9c5b37b',
		'uid': '368e2306b72b41b7a88bf784d98da59a',
		'nickname': '文',
		'headPortrait': 'https://cdn-dev.nailtutu.com/tutu/anjou/headportrait/20190916150201203_629345.png',
		'contentStatus': 1,
		'content': '我的',
		'replyCount': 0,
		'nextGradeReplyCount': 0,
		'createTime': '2019-12-05 14:46:48'
	}, {
		'id': 'd81df9af96e8422aa41dc0484e3269ce',
		'albumsId': '1f54943239854c8a8225c6a4e9c5b37b',
		'uid': '368e2306b72b41b7a88bf784d98da59a',
		'nickname': '文',
		'headPortrait': 'https://cdn-dev.nailtutu.com/tutu/anjou/headportrait/20190916150201203_629345.png',
		'contentStatus': 1,
		'content': '我们',
		'replyCount': 0,
		'nextGradeReplyCount': 0,
		'createTime': '2019-12-05 14:46:42'
	}]
}
# content = "科技首页作品电脑您的工具."
#
# ret = BU.get_commentID(test_dict,content)
# print(ret)
#
# # print(new_list)
#
#
#
#
# # result = BU.get_commentID(test_dict["data"],content)
# # print(result)



