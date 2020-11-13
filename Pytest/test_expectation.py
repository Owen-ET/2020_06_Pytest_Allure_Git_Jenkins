#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 16:56
# @Author  : zc
# @File    : test_expectation.py



import pytest

@pytest.mark.parametrize("text_input,expected",
                         [
                             ("1+2",3),
                             ("3*5",15),
                             ("9/3",1)
                         ])
def test_eval(text_input,expected):
    assert eval(text_input) == expected