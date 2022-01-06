import pytest
from HashMap import Ploc
from HashMap import InvalidDictIndexException

@pytest.fixture
def test_array():
    return [('1', 1), ('2', 2), ('3', [3, 4]), ('2, 6', 8)]

class TestPloc:

    def test_creation(self, test_array):
        ploc = Ploc(test_array)
        assert str(ploc) == str(ploc)

    def test_getting_item(self, test_array):
        ploc = Ploc(test_array)
        assert ploc['>= 2'] == {'2': 2, '3': [3, 4]}

    def test_getting_item_by_wrong_key(self):
        ploc = Ploc([])
        
        with pytest.raises(InvalidDictIndexException):
            wrong_key = 1
            ploc[wrong_key]
        