#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 09:44
# @Author  : zc
# @File    : test_v2ex_api.py


import yaml
import requests


class TestV2exApi(object):

    with open("./data/request.yaml",'r',encoding='utf-8') as file:
        data = yaml.load(file)


    def test_node(self):
        yamlData = self.data['request']
        url = yamlData['url']
        payload = yamlData['payload']

        r = requests.get(url,params=payload).json()
        assert r['id'] == 90
        assert r['name'] == 'python'
