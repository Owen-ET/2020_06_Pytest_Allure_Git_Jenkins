#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 10:07
# @Author  : zc
# @File    : test_v2ex_api1.py



import yaml
import requests
import pytest


class TestV2exApi(object):

    with open("./data/request2.yaml",'r',encoding='utf-8') as file:
        data = yaml.load(file)

    yamlData = data['request']
    names = yamlData['payload']


    @pytest.fixture(params=names)
    def lang(self,request):
        return request.param


    def test_node(self,lang):

        url = self.yamlData['url'] + "?name=%s"%(lang['name'])

        r = requests.get(url).json()
        assert r['name'] == lang['name']
        assert r['id'] == lang['id']
        # assert 0


# if __name__ == '__main__':
#     pytest.main(["-s","-v",""])