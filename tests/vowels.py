def has_vowel(s):
    vowels = "aeiou"
    for char in s.lower():
        if char in vowels:
            return True
    return False

def test_has_vowel():
    assert has_vowel("world")     # True, has 'o'
    assert not has_vowel("sky")