#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 13:55
# @Author  : zc
# @File    : test_calc.py


def add(x,y):

    return x + y


def test_calc():

    assert add(1,5) == 6
    assert add(2,9) == 11