def search(needle, haystack):
    left = 0
    right = len(haystack) - 1

    while left <= right:
        middle = left + (right - left) // 2
        middle_element = haystack[middle]
        if middle_element == needle:
            return middle
        elif middle_element < needle:
            left = middle + 1
        else:
            right = middle - 1
    raise ValueError("Value not in haystack")

def test_search():
    assert search(2, [1, 2, 3, 4]) == 1, \
        'found needle somewhere in the haystack'

def test_search_first_element():
    assert search(1, [1, 2, 3, 4]) == 0,  \
        'search first element'

def test_search_last_element():
    assert search(4, [1, 2, 3, 4]) == 3,  \
        'search last element'

def test_exception_not_found():
    from pytest import raises

    with raises(ValueError, message="left out of bound"):
        search(-1, [1, 2, 3, 4])

    with raises(ValueError, message="right out of bound"):
        search(5, [1, 2, 3, 4])

    with raises(ValueError, message="not found in middle"):
        search(2, [1, 3, 4])

