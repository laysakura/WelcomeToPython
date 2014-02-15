# -*- coding: utf-8 -*-
import nose.tools as ns
from welcometopython.calc.fib import fibonacci


def test_fibonacci():
    """:func:`fibonacci` のテスト"""
    ns.eq_(fibonacci(2), 1)
    ns.eq_(fibonacci(10), 55)

    with ns.assert_raises(ValueError):
        fibonacci(-1)
