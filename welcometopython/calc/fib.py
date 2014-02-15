# -*- coding: utf-8 -*-
"""
    welcometopython.calc.fib
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :synopsis: フィボナッチ数を求める関数を提供するモジュール
"""


def fibonacci(n):
    """フィボナッチ数を求める関数

    :param n: ``n`` 番目のフィボナッチ数を求める
    :returns: n番目のフィボナッチ数
    :raises: ``ValueError`` when ``n`` is less than 0
    """
    if n < 0:
        raise ValueError('nは0以上を指定してください')

    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
