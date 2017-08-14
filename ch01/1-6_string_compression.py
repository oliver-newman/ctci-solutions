def compressed_string(string):
    if len(string) == 0:
        return string
    compressed_string_list = []
    curr_char = string[0]
    curr_char_count = 1
    for i in range(1, len(string)):
        if string[i] != curr_char:
            compressed_string_list.append(curr_char + str(curr_char_count))
            curr_char = string[i]
            curr_char_count = 1
        else:
            curr_char_count += 1
    compressed_string_list.append(curr_char + str(curr_char_count))

    compressed_string = ''.join(compressed_string_list)
    return min(string, compressed_string, key=len)


def test_compress_string():
    test_cases = [
        ('', ''),
        ('a', 'a'),
        ('aa', 'aa'),
        ('aaa', 'a3'),
        ('aba', 'aba'),
        ('abbba', 'ab3a'),
        ('aabccccaaa', 'a2b1c5a3'),
    ]
    for case, expected in test_cases:
        assert compress_string(case) == expected
