def one_away(str1, str2):
    i = 0
    j = 0
    difference_count = 0
    str1, str2 = sorted([str1, str2], key=len)
    while (i < len(str1) or j < len(str2)) and difference_count <= 1:
        if i >= len(str1) or j >= len(str2) or str1[i] != str2[j]:
            difference_count += 1	
            if len(str1) == len(str2):
                i += 1
            j += 1
        else:
            i += 1
            j += 1

    return difference_count <= 1


def test_one_away():
    test_cases = [
        (('pale', 'ple'), True),
        (('pales', 'pale'), True),
        (('pale', 'bale'), True),
        (('pale', 'bake'), False),
    ]
    for case, expected in test_cases:
        assert one_away(*case) == expected
