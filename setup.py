#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


tests_require = [
    'nose',
]
"""テストの際使用するパッケージ"""

setup(
    name='WelcomeToPython',
    description='''Python初心者がPyPIライブラリを作れるように教育するためのパッケージ''',
    long_description=open('README.rst').read(),
    url='https://github.com/laysakura/WelcomeToPython',
    license='LICENSE.txt',
    version='1.0',
    author='Sho Nakatani',
    author_email='lay.sakura@gmail.com',
    test_suite='nose.collector',
    tests_require=tests_require,
    install_requires=[
        'rainbow_logging_handler',
    ],  # 依存パッケージ記述。 ``./setup.py install`` で自動インストールされる
    extras_require={
        'testing': tests_require,
    },  # こうしておくと、 ``pip install -e .[testing]``
        # でテストに必要なパッケージが入る
    packages=[
        'welcometopython',
        'welcometopython.calc',
    ],  # 提供パッケージ一覧。サブモジュールも忘れずに
    scripts=[
    ],  # 実行ファイル一覧。 ``./setup.py install`` で
        # ``/usr/bin/`` とかにコピーされる
    classifiers='''
Programming Language :: Python
Development Status :: 3 - Alpha
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.3
Environment :: Plugins
Intended Audience :: Developers
License :: Public Domain
Natural Language :: Japanese
'''.strip().splitlines()  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
)
