def string_rotation(str1, str2):
    """
    Determine if str2 is a rotation of str1, using exactly one is_substring
    check
    sr('waterbottle', 'erbottlewat') == True
    sr('waterbottle', 'waterbottle') == True
    sr('waterbottle', 'waterbottla') == False
    """
    if len(str1) != len(str2):
        return False
    else:
        return str1 in str2 * 2


def test_string_rotation():
    test_cases = [
        (('waterbottle', 'erbottlewat'), True),
        (('waterbottle', 'waterbottle'), True),
        (('waterbottl', 'waterbottle'), False),
        (('waterbottle', 'waterbottla'), False),
        (('ab', 'ba'), True),
        (('', ''), True),
        (('a', 'a'), True)
    ]

    for case, expected in test_cases:
        assert string_rotation(*case) == expected
