===============
WelcomeToPython
===============

.. image:: https://travis-ci.org/laysakura/WelcomeToPython.png?branch=master
   :target: https://travis-ci.org/laysakura/WelcomeToPython

PyPIに上げることのできるPythonパッケージの作り方を示したレポジトリです。
構成的にはこのレポジトリ自体PyPIに上げることができます(内容的にはやめたほうが良いでしょう)。

.. contents:: :local:


最低限のファイル構成
====================

パッケージをPyPIに上げるための最低限のファイル構成を説明します。
ここでいう最低限とはシステム的な意味ではなく、利用者から見て「最低限これくらいないと安心して使えない」という意味です。
従ってやや主観が入りますが、ご了承ください。

.. code-block:: bash

    $ tree -a -I .git
    .
    ├── .gitignore
    ├── CHANGES.rst  # いわゆるCHANGELOG
    ├── LICENSE.txt
    ├── MANIFEST.in  # PyPIに特別に登録したいファイルを記述
    ├── README.rst
    ├── setup.cfg    # setup.py スクリプトの動作設定
    ├── setup.py     # パッケージのインストール、テストなどを提供するためのスクリプト
    ├── test
    │   ├── __init__.py  # テストケースを入れるディレクトリ
    │   └── test_fib.py  # welcometopython.calc.fib モジュールのテスト
    └── welcometopython  # こういう名前のパッケージを今回作る。小文字かアンダースコア使おう
        ├── __init__.py
        └── calc
            ├── __init__.py
            └── fib.py   # welcometopython.calc.fib モジュール


TODO
====
- python っぽいもの
  - list, generator, dict comprehension

- test, coverage まで含めたもの

- travis

- sphinxまで含めて


- その他ポインタ
  - pep8, pyflakes
  - fullrelease コマンド
  - debug: pudb
  - prof: plop


Author
======

Sho Nakatani <lay.sakura@gmail.com>

License
=======

This is free and unencumbered public domain software. For more information,
see <http://unlicense.org/> or the accompanying `LICENSE.txt` file.
