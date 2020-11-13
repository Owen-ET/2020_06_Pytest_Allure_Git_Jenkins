#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 14:00
# @Author  : zc
# @File    : test_assert.py

import pytest


def test_zero():

    with pytest.raises(ZeroDivisionError):
        1/0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)