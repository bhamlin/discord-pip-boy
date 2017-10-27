
from operator import add, sub, mul, truediv as div

__NUMBER = int('0').__class__

__NUMBERS = '0123456789'

__OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def parse(content):
    # Now, the hard part.
    parts = lex(content)
    return collect(parts)

def collect(parts):
    stack = list()
    n = len(parts)
    i = 0

    while i < n:
        if parts[i] == 'd':
            u, v = parts[i-1], parts[i+1]
            print('?', u, 'd', v)
        i += 1
    return parts

def lex(content):
    # Attempt to comprehend what we've been given.
    content = content.replace(' ', '').lower()

    actions = list()
    appending = False
    value = 0

    for symbol in content:
        if symbol in __NUMBERS:
            if not appending:
                value = 0
                appending = True
            value *= 10
            value += int(symbol)
        else:
            appending = False
            actions.append(value)

            if symbol == 'd':
                if actions[-1] == 0:
                    actions[-1] = 1
                actions.append('d')
            elif symbol in __OPERATORS:
                actions.append(__OPERATORS[symbol])
            else:
                print('!!', 'Unknown symbol:', symbol)

    if appending:
        actions.append(value)
    print('=', actions)

    return actions

