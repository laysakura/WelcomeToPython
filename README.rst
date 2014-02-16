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
docstring があれば、それを元に `ドキュメントを自動生成 <#ドキュメント生成>`_ できます。


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

次は、カバレッジの計測をできるようにします。
カバレッジとは、テストケースがテスト対象のコードをどの程度テストできているかを示す指標です。
テストを書いてもカバレッジが極端に低ければ不十分と言えます。

カバレッジ計測
--------------

Ver 1.1 にする前に、Ver 1.0 の状態でカバレッジを計測してみましょう。
カバレッジを計測するために、以下のコマンドで必要なパッケージを追加してください。

.. code-block:: bash

    $ pip install coverage nose-cov


次に、 ``setup.cfg`` を以下のように編集してください。
これで、 ``welcometopython`` パッケージのカバレッジが計測され、計測結果がHTMLで確認できるようになります。

.. code-block:: python

    [nosetests]
    with-cov   = 1
    cov        = welcometopython
    cov-report = html


この状態で ``./setup.py nosetests`` コマンドによりテストを実行すると、 ``htmlcov/index.html`` から
カバレッジ計測結果が確認できるようになります。ブラウザで開いて確認してみてください。
``welcometopython/calc/fib.py`` を含む3つのファイルがカバレッジ100%を達成していることが確認できるかと思います。


ブランチカバレッジ計測
----------------------

しかし、この設定では計測できていないカバレッジがあります。
ブランチカバレッジ(或いはC1カバレッジ)というものです。

テストケースでは、負の数を引数に与えてテストしていなかったために、
``welcometopython/calc/fib.py`` の一部コードパスは実行されません。

.. code-block:: python

    def fibonacci(n):
        """フィボナッチ数を求める関数
    
        :param n: ``n`` 番目のフィボナッチ数を求める
        :returns: n番目のフィボナッチ数
        :raises: ``ValueError`` when ``n`` is less than 0
        """
        if n < 0:
            raise ValueError('nは0以上を指定してください')  # 実行されない!!
    
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


今回実行されないパスは1行だけの単純なものですが、分岐先により複雑なコードが書いてある場合もあり、
全ての分岐を漏らさずテストすることは重要です。

そのために、 ``setup.cfg`` の末尾に ``cov-config = .coveragerc`` の行を加え、
``.coveragerc`` ファイルを以下の内容で作成してください。

.. code-block:: python

    [run]
    branch = True
    
    [report]
    show_missing = True


この状態で ``./setup.py nosetests`` コマンドによりテストを実行すると、 ``htmlcov/index.html`` のカバレッジ表示が変わり、
``welcometopython/calc/fib.py`` のカバレッジが82%に落ちたことが確認できます。
カバレッジを100%に回復させるには、 ``n < 0`` の場合も含めたテストケースを記述します。


Ver 1.1 状態にする
------------------

カバレッジ計測により潜在的なバグを減らす重要性が分かったところで、レポジトリをカバレッジ計測をするようにしたバージョンにしてください。
このレポジトリは、上に挙げた全ての作業結果を含んでいます。

.. code-block:: bash

    $ git reset --hard
    $ git checkout 1.1


``git diff 1.0`` で、追加されたファイルや追記された内容が確認できます。


Ver 1.2: 継続的インテグレーション
=================================

モジュールを作成するときの手順は、基本的には次のようなものです。

1. 追加機能用のテストケースを記述
2. 追加機能モジュールを作成
3. テストを実行し、通らなければデバッグ
4. デプロイ

時として、この3番目の工程を時として忘れてデプロイしてしまうようなことがあります。
コードにバグが含まれていた場合、一刻も早くバグを解消し、修正版をデプロイしなければなりません。
そのためには、デプロイ時に自動的にテストが走るようにし、テストが失敗したら通知をしてくれるような仕組みが有効であり、
これを一般的に継続的インテグレーション(以下、CI)と呼びます。

CI用のツールは世の中に沢山ありますが、無料で使えて GitHub との親和性も高い Travis CI を使用しましょう。
Travis CIをGitHubと連携して使う方法は・・・すみません、ググってください。

ここでは、Travis CI の使用に必須である ``.travis.yml`` の記述方法を説明します。


Ver 1.2 状態にする
------------------

.. code-block:: bash

    $ git checkout 1.2


.travis.yml の記述
------------------

``.travis.yml`` を確認すると、以下のような記述になっています。

.. code-block:: yaml

    language: python
    python:
      - "2.7"
      - "3.3"
    
    branches:
      only:
        - master
    
    install:
      - "pip install ."
      - "pip install -e .[testing]"  # for installing `tests_require`
    
    script:
      - "./setup.py nosetests"


この記述により、GitHub の ``master`` ブランチにpushをする度に、Python 2.7 と Python 3.3 でテストケースが走ります。
テストが失敗した場合には GitHub に登録しているメールアドレスにメール通知が着ます。

また、Travis CIのテスト結果を、パッケージのユーザに示すこともできます。
このREADMEの先頭にもついているバッチがそれです。


補遺
====

これから素晴らしいパッケージをPyPIに登録するあなたのために、詳しく書きそびれた事項を簡単に記しておきます。

リリースサイクル自動化
----------------------

PyPIへの登録は楽な作業ではありません。
特にパッケージをバグフィックスなどで少しだけ修正した場合には、PyPIへの更新作業が面倒に感じる場合があります。

``$ pip install zest.releaser`` で手に入る ``fullrelease`` コマンドを用いると、
ほとんどエンターキーを押すだけでPyPIへの登録・更新作業が完了します。
PyPI Author にとって必携とも言えるツールでしょう。


ドキュメント生成
----------------

多くのユーザを獲得しているパッケージは、十分なドキュメントを備えているものです。
しかし、ドキュメントをコードに合わせてアップデートしていくのは非常に骨が折れるばかりか忘れがちな作業と言えます。

Pythonコミュニティでは、 **Sphinx** というドキュメントビルダを用いて、
コードからドキュメントを(ある程度)自動的に生成することが一般的に行われます。
モジュール、関数、変数などに docstring を記述しておくことで、簡易的なAPIリファレンスは自動的に生成可能です。

更に、ドキュメントページのテンプレートを作成することで、よりユーザフレンドリーなドキュメントを作成することも可能です。

PyPIパッケージでは、docstringやREADMEをReST(ReStructured Text)形式で記述することが求められます。
早いうちにReST形式に慣れておきましょう。


美しいコードを書く
-----------------

素晴らしいコードを書くことは難しくても、美しいコードは基本を抑えれば書けてしまいます(程度問題ですが :P )。
特にPythonでは、美しさの基準が **PEP 8** という定義書によって明文化されています。
更に、あなたの書いたコードが PEP 8 を尊守しているかどうか、それを自動で確かめるためのツールがあります。

``$ pip install pep8`` で今すぐに ``pep8`` コマンドを入手してください。
そして試しに、 ``$ pep8 setup.py`` コマンドで、このレポジトリの唯一のPEP 8違反を見つけてみてください。

この手のツールは、エディタと統合して最大限の力を発揮します。
``pep8`` コマンドをお使いのエディタと統合して、インタラクティブにコーディング規約違反を見つける環境をセットしてみてください。

またその際、 ``$ pip install pyflakes`` で手に入る ``pyflakes`` もエディタに統合し、
文法エラーもインタラクティブに発見できるようにすることをおすすめします。


デバッグ・プロファイリング
--------------------------

筆者はデバッグには ``pudb`` を、プロファイリングには ``plop`` を使用しています。
必要になった場合はこちらの使用を検討してみてはいかがでしょうか。
どちらもグラフィカルな素晴らしいツールです。


Author
======

Sho Nakatani <lay.sakura@gmail.com>

License
=======

This is free and unencumbered public domain software. For more information,
see <http://unlicense.org/> or the accompanying `LICENSE.txt` file.
