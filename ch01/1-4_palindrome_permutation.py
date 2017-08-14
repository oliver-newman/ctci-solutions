def palindrome_permutation(string):
    seen = set()
    for c in string.replace(' ', '').lower():
        if c in seen:
            seen.remove(c)
        else:
            seen.add(c)
    return len(seen) <= 1


def test_palindrome_permutation():
    test_cases = [
        ('Tact Coa', True),
        ('hah', True),
        ('lion iol', True),
        ('lala', True),
        ('', True),
        ('hh', True),
        ('Tact Coal', False),
        ('had', False),
        ('la', False),
    ]
    for case, expected in test_cases:
        assert palindrome_permutation(case) == expected
