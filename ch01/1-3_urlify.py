def urlify(string, length):
    urlified_string = list(string)
    for i in range(length):
        if urlified_string[i] == ' ':
            for j in reversed(range(i, len(urlified_string))):
                urlified_string[j] = urlified_string[j - 2]
            urlified_string[i] = '%'
            urlified_string[i + 1] = '2'
            urlified_string[i + 2] = '0'
    return ''.join(urlified_string)


def test_urlify():
    test_cases = [
        ((list('Mr John Smith    '), 13), 'Mr John Smith'.replace(' ', '%20')),
    ]
    for case, expected in test_cases:
        assert urlify(*case) == expected
