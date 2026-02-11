def is_leap(year):
    if year%400 == 0:
        return True
    elif year%100 ==0:
        return False
    elif year %4==0:
        return True
    else:
        return False

def test_is_leap():
    assert is_leap(2000) is True
