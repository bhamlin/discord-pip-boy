#!env/bin/python3

import pipboy

entries = {
    'General rolls': [
        '1d1',
        '1d2',
        '1d3',
        '1d4',
        '1d6',
        '1d8'
    ]
}

for entry, tests in entries.items():
    print(entry, ':')
    for test in tests:
        print('--', test, ':', pipboy.parse(test))
