import pytest
from src.edinet_label.zip_util import ZipUtil


class TestZipUtil:
    @pytest.fixture(scope="class")
    def zf(self):
        dir_ = '/Users/atu/Library/Mobile Documents/com~apple~CloudDocs/data/taxonomy_edinet_zip/'
        path = dir_ + '2014.zip'
        return ZipUtil(path)

    def test_namelist(self, zf):
        assert len(list(zf.namelist())) == 16

    def test_each_soup(self, zf):
        soup, place = next(zf.each_soup())
        labels = soup.find_all('link:label')
        assert len(labels) == 3267
        assert place == 'taxonomy/jpcrp/2013-08-31/label/jpcrp_2013-08-31_lab.xml'

    def test_each_soup_2(self, zf):
        for soup, place in zf.each_soup():
            assert place.endswith('lab.xml')
