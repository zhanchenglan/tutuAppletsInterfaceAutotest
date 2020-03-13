#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 11:19
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : test_case_addAlbumsCommentReply.py
# @Software: PyCharm

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import unittest
from common.FileParsing import FileParser
from common.baseUtil import baseUtils
from interface.base.login.authentication import Authentication
from interface.tutu.Album.getAlbumsList4Front import getAlbumsList4Front
from interface.tutu.Album.getAlbumsDeatil4Front import getAlbumsDeatil4Front
from interface.tutu.Album.AlbumComment.getAlbumsCommentList import getAlbumsCommentList
from interface.tutu.Album.AlbumComment.addAlbumsComment import addAlbumsComment
from interface.tutu.Album.AlbumComment.deleteAlbumsComment import deleteAlbumsComment
from interface.tutu.Album.AlbumComment.addAlbumsCommentReply import addAlbumsCommentReply
from interface.tutu.Album.AlbumComment.getAlbumsCommentReplySimpleList import getAlbumsCommentReplySimpleList
from interface.tutu.Album.AlbumComment.deleteAlbumsCommentReply import deleteAlbumsCommentReply
from common.excelUtil import excelUtil


class TestaddAlbumsCommentReplyFunc(unittest.TestCase):
    """Test addAlbumsCommentReply.py"""

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
        self.addAlbumsCommentReply = addAlbumsCommentReply()
        self.getAlbumsCommentReplySimpleList = getAlbumsCommentReplySimpleList()
        self.deleteAlbumsCommentReply = deleteAlbumsCommentReply()

    @unittest.skip("暂时遮蔽")
    def test_addAlbumsCommentReply_tutu_Applets_001(self):
        '''美甲涂涂Applets端_回复专辑评论_正常回复_手机号密码登录_001'''
        #安卓登录
        TestData = self.ex.getDict(2, 27, 7, self.testData)
        currentPage = TestData["currentPage"]
        pageSize = TestData["pageSize"]

        phone = "13536764015"
        password = TestData["password"]
        data = self.AC.get_Applets_ordinary_logged_in(phone, password)

        app_login_url_ch = self.AC.get_AuthenticationURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                         self.config.get("imi_login_url", "login_url"),
                                                         self.config.get("lang", "zh"), self.base.getTimeStamp(),
                                                         self.config.get("clientVersionInfo",
                                                                         "clientVersionInfo_ch_Android"))
        access_token = self.AC.get_Access_token(app_login_url_ch, data)
        self.assertIsNotNone(access_token)

        # 专辑列表
        ListQueryURL = self.ListQuery.get_getAlbumsList4FrontURL(self.config.get('imi_base_url_ch', 'base_url_prod'),
                                                                 self.config.get("imi_cms_url",
                                                                                 "getAlbumsList4FrontURL"),
                                                                 self.config.get("lang", "zh"),
                                                                 self.base.getTimeStamp(),
                                                                 self.config.get("clientVersionInfo",
                                                                                 "clientVersionInfo_ch_Android"),
                                                                 access_token)

        result_ListQuery = self.ListQuery.send_request_getAlbumsList4Front(ListQueryURL, currentPage, pageSize)

        self.assertEqual(result_ListQuery["stateCode"], 200)
        self.assertEqual(result_ListQuery["stateMsg"], "OK")
        self.assertIsNotNone(result_ListQuery["data"])

        # 获取最后一个特辑ID，作为特辑详情的参数
        albumsId = result_ListQuery["data"][-1]["albumsId"]

        # 专辑详情
        AlbumsDeatilURL = self.AlbumsDeatil.get_getAlbumsDeatil4FrontURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("imi_cms_url", "getAlbumsDeatil4FrontURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(),
            self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"), access_token)

        result_AlbumsDeatil = self.AlbumsDeatil.send_request_getAlbumsDeatil4Front(AlbumsDeatilURL, albumsId)

        self.assertEqual(result_AlbumsDeatil["stateCode"], 200)
        self.assertEqual(result_AlbumsDeatil["stateMsg"], "OK")
        self.assertEqual(result_AlbumsDeatil["data"]["albumsId"], albumsId)

        # 发表专辑评论
        addAlbumsCommentURL = self.addAlbumsComment.get_addAlbumsCommentURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("AlbumsComment", "addAlbumsCommentURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(),
            self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"), access_token)
        comment_content = self.base.get_random_content()
        result_addAlbumsComment = self.addAlbumsComment.send_request_addAlbumsComment(addAlbumsCommentURL, albumsId,
                                                                                      comment_content)

        self.assertEqual(result_addAlbumsComment["stateCode"], 200)
        self.assertEqual(result_addAlbumsComment["stateMsg"], "OK")

        # 专辑评论列表查询
        getAlbumsCommentListURL = self.getAlbumsCommentList.get_getAlbumsCommentListURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("AlbumsComment", "getAlbumsCommentListURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(),
            self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"), access_token)

        result_getAlbumsCommentList = self.getAlbumsCommentList.send_request_getAlbumsCommentList(
            getAlbumsCommentListURL, albumsId, currentPage, pageSize)

        self.assertEqual(result_getAlbumsCommentList["stateCode"], 200)
        self.assertEqual(result_getAlbumsCommentList["stateMsg"], "OK")

        # 回复专辑评论
        addAlbumsCommentReplyURL = self.addAlbumsCommentReply.get_addAlbumsCommentReplyURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("AlbumsComment", "addAlbumsCommentReplyURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(), self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),
            access_token)

        commentId = self.base.get_commentIDORreplyID(result_getAlbumsCommentList, comment_content)
        replyId = commentId
        replyType = "2"
        toUid = result_getAlbumsCommentList["data"][0]["uid"]
        toUidNickname = result_getAlbumsCommentList["data"][0]["nickname"]
        toUidHeadPortrait = result_getAlbumsCommentList["data"][0]["headPortrait"]
        reply_content = "回复" + self.base.get_random_content()
        result_addAlbumsCommentReply = self.addAlbumsCommentReply.send_request_addAlbumsCommentReply(
            addAlbumsCommentReplyURL, commentId, reply_content, replyId, replyType, toUid, toUidNickname,
            toUidHeadPortrait)

        self.assertEqual(result_addAlbumsCommentReply["stateCode"], 200)
        self.assertEqual(result_addAlbumsCommentReply["stateMsg"], "OK")

        # 回复—列表查询(简单形)
        getAlbumsCommentReplySimpleListURL = self.getAlbumsCommentReplySimpleList.get_getAlbumsCommentReplySimpleListURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("AlbumsComment", "getAlbumsCommentReplySimpleListURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(), self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"),
            access_token)

        commentId = commentId
        result_getAlbumsCommentReplySimpleList = self.getAlbumsCommentReplySimpleList.send_request_getAlbumsCommentReplySimpleList(
            getAlbumsCommentReplySimpleListURL, commentId, currentPage, pageSize)

        self.assertEqual(result_getAlbumsCommentReplySimpleList["stateCode"], 200)
        self.assertEqual(result_getAlbumsCommentReplySimpleList["stateMsg"], "OK")

        # 删除专辑回复评论
        deleteAlbumsCommentReplyURL = self.deleteAlbumsCommentReply.get_deleteAlbumsCommentReplyURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("AlbumsComment", "deleteAlbumsCommentReplyURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(),
            self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"), access_token)

        replyId = self.base.get_commentIDORreplyID(result_getAlbumsCommentReplySimpleList, reply_content)
        completeDel = True
        result_deleteAlbumsCommentReply = self.deleteAlbumsCommentReply.send_request_deleteAlbumsCommentReply(
            deleteAlbumsCommentReplyURL, replyId, completeDel)

        self.assertEqual(result_deleteAlbumsCommentReply["stateCode"], 200)
        self.assertEqual(result_deleteAlbumsCommentReply["stateMsg"], "OK")

        # 删除专辑评论
        deleteAlbumsCommentURL = self.deleteAlbumsComment.get_deleteAlbumsCommentURL(
            self.config.get('imi_base_url_ch', 'base_url_prod'),
            self.config.get("AlbumsComment", "deleteAlbumsCommentURL"), self.config.get("lang", "zh"),
            self.base.getTimeStamp(),
            self.config.get("clientVersionInfo", "clientVersionInfo_ch_Android"), access_token)

        commentId = self.base.get_commentIDORreplyID(result_getAlbumsCommentList, comment_content)
        completeDel = True
        result_addAlbumsComment = self.deleteAlbumsComment.send_request_deleteAlbumsComment(deleteAlbumsCommentURL,
                                                                                            commentId, completeDel)

        self.assertEqual(result_addAlbumsComment["stateCode"], 200)
        self.assertEqual(result_addAlbumsComment["stateMsg"], "OK")

    def tearDown(self):
        pass

    if __name__ == '__main__':
        unittest.main()