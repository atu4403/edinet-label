import pytest
from src.edinet_label.taxonomy_set import set_redis
from src.edinet_label import get_label


@pytest.mark.skip(reason="このtestを行うとzipファイル内の全ラベルをredisに保存する")
def test_version():
    dir_ = '/Users/atu/Library/Mobile Documents/com~apple~CloudDocs/data/taxonomy_edinet_zip'
    set_redis(dir_)


def test_get_label():
    place = 'taxonomy/jpdei/2013-08-31/label/jpdei_2013-08-31_lab.xml'
    name = 'EntityInformationDEIAbstract'
    assert get_label(place, name) == '提出者情報'


def test_get_label_invalid_1():
    place = '2013-08-31/label/jpdei_2013-08-31_lab.xml'
    name = 'EntityInformationDEIAbstract'
    assert get_label(place, name) is None


def test_get_label_invalid_2():
    place = 'test/taxonomy/jpdei/2013-08-31/label/jpdei_2013-08-31_lab.xml'
    name = 'EntityInformationDEIAbstract'
    assert get_label(place, name) == '提出者情報'
