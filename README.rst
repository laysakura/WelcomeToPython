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
├── .coveragerc
├── .gitignore
├── .travis.yml
├── CHANGES.rst
├── MANIFEST.in
├── README.rst
├── setup.cfg
├── setup.py
├── test
└── welcometopython
    ├── __init__.py
    └── calc
        ├── __init__.py
        └── fib.py


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
