#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/06 16:37
# @Author  : zc
# @File    : test_quick_start.py


def function(string):

    return string[::-1]


def test_function():

    string1 = "hello"
    string2 = "world"

    assert function(string1) == 'olleh'
    assert function(string2) == 'dlrow'