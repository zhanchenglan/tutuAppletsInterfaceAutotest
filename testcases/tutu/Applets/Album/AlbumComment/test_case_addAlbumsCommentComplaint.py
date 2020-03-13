#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 19:06
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_addAlbumsCommentComplaint.py
# @Software: PyCharm


import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
import random
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.Album.getAlbumsList4Front import getAlbumsList4Front
from interface.tutu.Album.getAlbumsDeatil4Front import getAlbumsDeatil4Front
from interface.tutu.Album.AlbumComment.getAlbumsCommentList import getAlbumsCommentList
from interface.tutu.Album.AlbumComment.addAlbumsComment import addAlbumsComment
from interface.tutu.Album.AlbumComment.addAlbumsCommentComplaint import addAlbumsCommentComplaint
from interface.tutu.Album.AlbumComment.deleteAlbumsComment import deleteAlbumsComment
from common.excelUtil import excelUtil


class TestaddAlbumsCommentComplaintFunc(unittest.TestCase):
    """Test addAlbumsCommentComplaint.py"""

    def setUp(self):
        self.base = baseUtils()
        self.projectPath = self.base.getProjectPath() + os.sep + "config" + os.sep + "config.ini"
        self.testData = self.base.getProjectPath() + os.sep + "config" + os.sep + "AnjouTestCase.xls"
        self.config = FileParser(self.projectPath)
        self.AC = Authentication()
        self.ex = excelUtil()
        self.ListQuery = getAlbumsList4Front()
        self.AlbumsDeatil = getAlbumsDeatil4Front()
        self.getAlbumsCommentList = getAlbumsCommentList()
        self.addAlbumsComment = addAlbumsComment()
        self.deleteAlbumsComment = deleteAlbumsComment()
        self.addAlbumsCommentComplaint = addAlbumsCommentComplaint()

    @unittest.skip("暂时遮蔽")
    def test_addAlbumsCommentComplaint_tutu_Applets_001(self):
        '''美甲涂涂Applets端_评论投诉_正常投诉_手机号密码登录_001'''
        #安卓登录
        TestData = self.ex.getDict(2, 27, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = "13536764015"
        password = TestData["password"]
        data = self.AC.get_Applets_ordinary_logged_in(phone, password)

        app_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),self.config.get("imi_login_url","login_url"),self.config.get("lang", "zh"),self.base.getTimeStamp(),self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(app_login_url_ch,data)
        self.assertIsNotNone(access_token)


        #专辑列表
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getAlbumsList4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL,currentPage,pageSize)

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # 获取最后一个特辑ID，作为特辑详情的参数
        albumsId = result_ListQuery["data"][-1]["albumsId"]

        #专辑详情
        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL,albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"],albumsId)

        #专辑评论列表查询
        getAlbumsCommentListURL = self.getAlbumsCommentList.get_getAlbumsCommentListURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AlbumsComment", "getAlbumsCommentListURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_getAlbumsCommentList = self.getAlbumsCommentList.send_request_getAlbumsCommentList(getAlbumsCommentListURL,albumsId,currentPage,pageSize)

        self.assertEqual(result_getAlbumsCommentList["stateCode"], 200)
        self.assertEqual(result_getAlbumsCommentList["stateMsg"], "OK")

        #发表专辑评论
        addAlbumsCommentURL = self.addAlbumsComment.get_addAlbumsCommentURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AlbumsComment", "addAlbumsCommentURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)
        content = self.base.get_random_content()
        result_addAlbumsComment = self.addAlbumsComment.send_request_addAlbumsComment(addAlbumsCommentURL,albumsId,content)

        self.assertEqual(result_addAlbumsComment["stateCode"], 200)
        self.assertEqual(result_addAlbumsComment["stateMsg"], "OK")


        #专辑评论列表查询
        getAlbumsCommentListURL = self.getAlbumsCommentList.get_getAlbumsCommentListURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AlbumsComment", "getAlbumsCommentListURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        result_getAlbumsCommentList = self.getAlbumsCommentList.send_request_getAlbumsCommentList(getAlbumsCommentListURL,albumsId,currentPage,pageSize)

        self.assertEqual(result_getAlbumsCommentList["stateCode"], 200)
        self.assertEqual(result_getAlbumsCommentList["stateMsg"], "OK")



        #评论投诉
        addAlbumsCommentComplaintURL = self.addAlbumsCommentComplaint.get_addAlbumsCommentComplaintURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AlbumsComment", "addAlbumsCommentComplaintURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        albumsId = albumsId
        commentId = self.base.get_commentIDORreplyID(result_getAlbumsCommentList,content)
        replyType = 1
        uid = self.base.get_commentUID(result_getAlbumsCommentList,content)
        content = content
        complaintType = [1,2,3,4]
        really_complaintType = random.choice(complaintType)
        result_addAlbumsCommentComplaint = self.addAlbumsCommentComplaint.send_request_addAlbumsCommentComplaint(addAlbumsCommentComplaintURL,albumsId,commentId,replyType,uid,content,really_complaintType)

        self.assertEqual(result_addAlbumsCommentComplaint["stateCode"], 200)
        self.assertEqual(result_addAlbumsCommentComplaint["stateMsg"], "OK")


        #删除专辑评论
        deleteAlbumsCommentURL = self.deleteAlbumsComment.get_deleteAlbumsCommentURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                  self.config.get("AlbumsComment", "deleteAlbumsCommentURL"), self.config.get("lang", "zh"),
                                                  self.base.getTimeStamp(),
                                                  self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),access_token)

        commentId = self.base.get_commentIDORreplyID(result_getAlbumsCommentList,content)
        completeDel = True
        result_addAlbumsComment = self.deleteAlbumsComment.send_request_deleteAlbumsComment(deleteAlbumsCommentURL,commentId,completeDel)

        self.assertEqual(result_addAlbumsComment["stateCode"], 200)
        self.assertEqual(result_addAlbumsComment["stateMsg"], "OK")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()