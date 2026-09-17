from app import add

def test_add_func():
    result = add(10, 22)
    assert result == 32
