def compressed(string):
    if len(string) == 0:
        return string

    compressed_string_list = []
    curr_char = string[0]
    curr_char_count = 1
    for i in range(1, len(string)):
        if string[i] == curr_char:
            curr_char_count += 1
        else:
            compressed_string_list.append(curr_char + str(curr_char_count))
            curr_char = string[i]
            curr_char_count = 1
    compressed_string_list.append(curr_char + str(curr_char_count))

    compressed_string = ''.join(compressed_string_list)
    return min(string, compressed_string, key=len)


def test_compressed():
    test_cases = [
        ('', ''),
        ('a', 'a'),
        ('aa', 'aa'),
        ('aaa', 'a3'),
        ('abba', 'abba'),
        ('abbbbba', 'a1b5a1'),
        ('aabcccccaaa', 'a2b1c5a3'),
        ('aaaaaaaaaaa', 'a11'),
    ]
    for case, expected in test_cases:
        assert compressed(case) == expected
