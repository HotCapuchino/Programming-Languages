import pytest
from HashMap import Iloc
from HashMap import InvalidDictIndexException

@pytest.fixture
def test_array():
    return [('1', 1), ('2', 2), ('3', [3, 4])]

class TestIloc:

    def test_creation(self, test_array):
        iloc = Iloc(test_array)
        assert str(iloc) == str(test_array)

    def test_getting_item(self, test_array):
        iloc = Iloc(test_array)
        assert iloc[0] == 1
        assert iloc[1] == 2
        assert iloc[2] == [3, 4]
        

    def test_getting_item_by_wrong_index(self, test_array):
        iloc = Iloc(test_array)
        with pytest.raises(InvalidDictIndexException):
            wrong_index = '1'
            iloc[wrong_index]
    