#!env/bin/python3

import pipboy

entries = {
    'General rolls': [
        '4d6k3',
        '4d6k3x6',
        'fate',
        '10d6!',
        '2d1!',
        '1d1',
        'd4',
        '1 d 2',
        '111d44',
        '1d💯',
        '1d8+5',
        '1d20-2',
        '+5',
        '-4',
        '4d6>=4',
        '10df',
    ]
}

for entry, tests in entries.items():
    print(entry, ':')
    for test in tests:
        print(' ', test)
        print(' --', pipboy.parse(test))
