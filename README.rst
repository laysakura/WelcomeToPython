===============
WelcomeToPython
===============

.. image:: https://travis-ci.org/laysakura/WelcomeToPython.png?branch=master
   :target: https://travis-ci.org/laysakura/WelcomeToPython

PyPIに上げることのできるPythonパッケージの作り方を示したレポジトリです。
構成的にはこのレポジトリ自体PyPIに上げることができます(内容的にはやめたほうが良いでしょう)。

.. contents:: :local:


このレポジトリのインストール
============================

.. code-block:: bash

    $ git clone https://github.com/laysakura/WelcomeToPython.git
    $ cd WelcomeToPython



Ver 1.0: モジュール+テスト
=========================

まずはモジュールとそのテストを作成し、パッケージとします。
**テストのないモジュールは極力避けましょう。**

Ver 1.0 状態にする
------------------

.. code-block:: bash

    $ git checkout 1.0


ファイル構成
------------

Ver1.0が、パッケージをPyPIに上げるための最低限のファイル構成と言えます。
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


モジュールの解説
----------------

``welcometopython/calc/fib.py`` を見てください。
n番目のフィボナッチ数を求める ``fibonacci(n)`` 関数が定義されています。

.. code-block:: python

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


また、このように docstring を関数やモジュールに対して記述するのもマナーのひとつです。
docstring があれば、それを元にドキュメントを自動生成できます(Ver 1.3)。


テストの解説
------------

``test/test_fib.py`` が先ほどの ``fib.py`` に対するテストケースです。
``nose`` パッケージを使用してテストを行う場合、テストケースのファイル名は ``test_*`` で始めてください。

.. code-block:: python

    # -*- coding: utf-8 -*-
    import nose.tools as ns
    from welcometopython.calc.fib import fibonacci
    
    
    def test_fibonacci():
        """:func:`fibonacci` のテスト"""
        ns.eq_(fibonacci(2), 1)
        ns.eq_(fibonacci(10), 55)


ここでは、2番目と10番目のフィボナッチ数をテストするコードを書いています。

では、実際にテストを走らせてみましょう。
まずはテストに必要なパッケージをインストールします。

.. code-block:: bash

    $ pip install -e .[testing]


``nose`` パッケージがインストールされたでしょうか?
このコマンドで ``nose`` パッケージがインストールされるのは、 ``setup.py`` の次の記述によるものです。

.. code-block:: python

    # (前略)
    tests_require = [
        'nose',
    ]
    """テストの際使用するパッケージ"""
    
    setup(
        # (中略)
        extras_require={
            'testing': tests_require,
        },  # こうしておくと、 ``pip install -e .[testing]``
            # でテストに必要なパッケージが入る
    # (後略)


次のコマンドでテストが走ります。
ちゃんとパスしましたね。

.. code-block:: bash

    $ ./setup.py nosetests
    running nosetests
    running egg_info
    writing requirements to WelcomeToPython.egg-info/requires.txt
    writing WelcomeToPython.egg-info/PKG-INFO
    writing top-level names to WelcomeToPython.egg-info/top_level.txt
    writing dependency_links to WelcomeToPython.egg-info/dependency_links.txt
    reading manifest file 'WelcomeToPython.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'WelcomeToPython.egg-info/SOURCES.txt'
    running build_ext
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.003s
    
    OK


Ver 1.1: カバレッジ計測追加
===========================


Ver 1.2: 継続的インテグレーション
=================================


Ver 1.3: APIドキュメント追加
============================


Author
======

Sho Nakatani <lay.sakura@gmail.com>

License
=======

This is free and unencumbered public domain software. For more information,
see <http://unlicense.org/> or the accompanying `LICENSE.txt` file.
