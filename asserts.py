
@pytest.mark.parametrize("a,b,expected",[
    ([1,2,3],['A','B','C','D'], {1: 'A', 2: 'B', 3: 'C'}),
    ([1,2,3], 3, None),
    (3,['A','B','C'],None),
    ([],['A','B','C'],{})
])
def test_param(a, b, expected):
    assert diction(a,b)==expected
    assert diction([1,2,3], 3)==None
    assert diction(3,['A','B','C'])==None
    assert diction([],['A','B','C'])=={}

