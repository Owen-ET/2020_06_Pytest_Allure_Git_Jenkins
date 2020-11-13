#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 16:05
# @Author  : zc
# @File    : test_user_password_with_params.py


import pytest
import json
import yaml


with open('./users.yaml','r',encoding='utf-8') as file:
    users = yaml.load(file)


class TestUserPasswordWithParam(object):

    @pytest.fixture(params=users)
    def user(self,request):
        return request.param


    def test_user_password(self,user):

        msg1 = "user:%s passwd is not 6"%(user['name'])
        password = user['password']
        assert len(password) >=6,msg1

        msg = "user:%s is weak password"%(user['name'])
        assert password != "password", msg
        assert password != "password123", msg