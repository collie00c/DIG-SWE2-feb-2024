from increment_one import increment_one

def test_increment_one():
    assert increment_one(4) == 5
    assert increment_one(0) == 1
    assert increment_one(-5) == -4