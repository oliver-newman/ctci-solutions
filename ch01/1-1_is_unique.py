"""
1.1: Implement an algorithm to determine if a string has all unique
characters.  What if you cannot use additional data structures?
"""

def all_unique_with_set(string):
    present_characters = set()
    for c in string:
        if c in present_characters:
            return False
        else:
            present_characters.add(c)

    return True


def all_unique_without_set(string):
    sorted_string = sorted(string)

    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False

    return True


TEST_CASES = [
    ('hello', False),
    ('helo ward', True),
]


def test_all_unique_with_set():
    for case, expected in TEST_CASES:
        assert all_unique_with_set(case) == expected


def test_all_unique_without_set():
    for case, expected in TEST_CASES:
        assert all_unique_without_set(case) == expected
