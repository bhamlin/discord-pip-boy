#!env/bin/python3

import pipboy

entries = {
    'General rolls': [
        '1d1',
        'd4',
        '1 d 2',
        '111d44',
        '1d8+5',
        '1d20-2'
    ]
}

for entry, tests in entries.items():
    print(entry, ':')
    for test in tests:
        print('--', test, ':', pipboy.parse(test))
