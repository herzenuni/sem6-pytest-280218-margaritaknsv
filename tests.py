import pytest
from hypothesis import given
import hypothesis.strategies as st

def dict_main(keys, values):
    if not isinstance(keys, list) or not isinstance(values, list):
        raise TypeError('It is not a list')

    if len(keys) > len(values):
        difference = len(keys) - len(values)
        values = values + ([None] * difference)

    return dict(zip(keys, values))

def test():
    keys = ['1', '2', '3', '4']
    values = ['a', 'b', 'c', 'd']
    expected = { '1': 'a', '2': 'b', '3': 'c', '4': 'd'}

    assert dict_main(keys, values) == expected

def test2():
    keys = ['1', '2', '3', '4', '5']
    values = ['a', 'b', 'c', 'd']
    expected = { '1': 'a', '2': 'b', '3':'c', '4': 'd', '5': None }

    assert dict_main(keys, values) == expected

@pytest.mark.parametrize('keys, values', [
    (['1'], 'hello'),
    ('2', ['goodbye'])])

def test3(keys, values):
    with pytest.raises(TypeError):
        dict_main(keys, values)

@given(st.lists(st.text()))
def test4(extra_values):
    keys = ['1', '2', '3', '4']
    values = ['a', 'b', 'c', 'd']
    expected = { '1': 'a', '2': 'b', '3': 'c', '4': 'd'}

    assert dict_main(keys, values) == expected
