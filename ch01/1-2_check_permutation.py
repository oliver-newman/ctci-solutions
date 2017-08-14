"""
1.3: Given two strings, write a method to determine if one is a permutation
of the other.
"""

def are_permutations(str1, str2):
    str1_char_counts = {}
    for c in str1:
        if c in str1_char_counts:
            str1_char_counts[c] += 1
        else:
            str1_char_counts[c] = 1

    for c in str2:
        if c in str1_char_counts:
            str1_char_counts[c] -= 1

            if str1_char_counts[c] == 0:
                str1_char_counts.pop(c)
        else:
            str1_char_counts[c] = 0

    return not str1_char_counts


def test_are_permutations():
    test_cases = [
        (('hello', 'lhleo'), True),
        (('adsfh', 'kljfh'), False),
    ]
    for case, expected in test_cases:
        assert are_permutations(*case) == expected
