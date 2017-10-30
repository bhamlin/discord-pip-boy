#!env/bin/python3

import pipboy

entries = {
    'General rolls': [
        '10d6>=4',
        '10d6<=2',
        '10d6==3',
    ]
}

print('------------------------------')
for entry, tests in entries.items():
    for test in tests:
        print(test)
        print('--', pipboy.parse(test))
