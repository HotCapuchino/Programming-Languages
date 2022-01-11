import pytest
from HashMap import ModifiedDict
from HashMap import InvalidDictIndexException, KeyDoesNotExist, LexerException, InvalidMathSignException, ParserException

@pytest.fixture
def modDict() -> ModifiedDict:
    modDict = ModifiedDict()
    modDict['1.0'] = 2
    modDict['2'] = 3
    return modDict

class TestDictionary:
    
    def test_creation(self): 
        modDict = ModifiedDict()
        assert str(modDict.iloc) == str([]) and str(modDict.ploc) == str([])

    # Updating    
    def test_update(self, modDict: ModifiedDict):
        d = modDict
        d.update({'3': 4})
        assert d['1.0'] == 2 and d['2'] == 3 and d['3'] == 4

    def test_update_iloc_ploc(self, modDict):
        assert str(modDict.iloc) == str([('1.0', 2), ('2', 3)]) and str(modDict.ploc) == str([('1.0', 2), ('2', 3)])

    def test_update_wrong_key(self, modDict):
        with pytest.raises(InvalidDictIndexException):
            modDict[1] = 90

    def test_update_first_item(self, modDict):
        modDict['1.0'] = 22
        assert str(modDict.iloc) == str([('1.0', 22), ('2', 3)]) and str(modDict.ploc) == str([('1.0', 22), ('2', 3)])

    def test_update_not_first_item(self, modDict):
        modDict['2'] = 33
        assert str(modDict.iloc) == str([('1.0', 2), ('2', 33)]) and str(modDict.ploc) == str([('1.0', 2), ('2', 33)])

    def test_update_with_sort(self, modDict):
        modDict['4'] = 5
        modDict['3'] = 4
        assert modDict.iloc[2] == 4

    # Deleting
    def test_del(self, modDict):
        del modDict['2']

        with pytest.raises(KeyError):
            modDict['2']

    def test_del_first_item(self, modDict):
        del modDict['1.0']

        assert str(modDict.iloc) == str([('2', 3)]) and str(modDict.ploc) == str([('2', 3)])

    def test_del_wrong_key(self, modDict):
        with pytest.raises(InvalidDictIndexException):
            del modDict[1]
    
    def test_del_unexisting_key(self, modDict):
        with pytest.raises(KeyDoesNotExist):
            del modDict['90']
    
    # Selecting
    def test_selecting_ge(self, modDict):
        assert modDict.ploc['(>=2)'] == {'2': 3}

    def test_selecting_g(self, modDict):
        assert modDict.ploc['>1.0'] == {'2': 3}

    def test_selecting_le(self, modDict):
        assert modDict.ploc['<=1.0'] == {'1.0': 2}

    def test_selecting_l(self, modDict):
        assert modDict.ploc['<2'] == {'1.0': 2}

    def test_selecting_e(self, modDict): 
        assert modDict.ploc['=2'] == {'2': 3}

    def test_selecting_ne(self, modDict):
        assert modDict.ploc['<>2'] == {'1.0': 2}

    def test_wrong_condition(self, modDict):
        with pytest.raises(LexerException):
            modDict.ploc['nuh 2']

    def test_wrong_math_sign(self, modDict):
        with pytest.raises(InvalidMathSignException):
            modDict.ploc['=<2']

    def test_wrong_tokens_order1(self, modDict):
        with pytest.raises(ParserException):
            modDict.ploc['>,2']

    def test_wrong_tokens_order2(self, modDict):
        with pytest.raises(ParserException):
            modDict.ploc['2<']

    def test_selecting_several_conditions(self, modDict):
        modDict['(2, 1)'] = 90
        assert modDict.ploc['>1, >0'] == {'(2, 1)': 90}

    def test_selecting_several_conditions2(self, modDict):
        with pytest.raises(ParserException):
            modDict.ploc['>1, >,9']
