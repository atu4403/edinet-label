############
edinet-label
############

EDINETの日本語ラベルを取得します。redisが必要です。

useit
=====

.. code-block:: python

    from edinet_label import get_label
    def test_get_label():
        place = 'taxonomy/jpdei/2013-08-31/label/jpdei_2013-08-31_lab.xml'
        name = 'EntityInformationDEIAbstract'
        assert get_label(place, name) == '提出者情報'

setup
=====

redisサーバーを建てます::

    host='192.168.0.143'
    port=6378

skip行をコメントアウトしてtestを実行するとredisにstoreされます::

    # @pytest.mark.skip(reason="このtestを行うとzipファイル内の全ラベルをredisに保存する")
    def test_version():
        dir_ = '/Users/atu/Library/Mobile Documents/com~apple~CloudDocs/data/taxonomy_edinet_zip'
        set_redis(dir_)

この時に指定したディレクトリにzipファイルを置いておく必要があります。

