#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 14:59
# @Author  : zc
# @File    : test_user_password.py


import json
import pytest


class TestUserPassword():

    @pytest.fixture()
    def users(self):

        return json.loads(open('./users.json','r').read())

    # @pytest.fixture()
    def test(self):
        print("111")


    def test_user_password(self,users):

        for user in users:
            password = user['password']
            assert len(password)>=6

            msg = "user %s has a weak password"%(user['name'])

            assert password != "password123", msg
            assert password != "password", msg