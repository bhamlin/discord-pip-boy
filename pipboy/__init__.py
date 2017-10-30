
from functools import reduce
from operator import add, sub, mul, truediv as div, ge, le, eq
from random import randrange, choice

__EXPLODE_LIMIT = 100

__NUMBER = int('0').__class__

__NUMBERS = '0123456789f'

__OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

__TEST_OPS = {
    '>=': ge,
    '<=': le,
    '==': eq
}

#         +          -        ' '
__FATE = ('\uff0b', '\u2212', '\u2610')

def roll(count, sides, per_die=0):
    result = list()
    if sides == 'f':
        for _ in range(count):
            result.append(choice(__FATE))
    else:
        for _ in range(count):
            result.append(randrange(sides) + per_die + 1)
    return result

def parse(content):
    # Now, the hard part.
    parts = lex(content)
    stack = list()
    DO_SUM = True

    last_rolled_sides = 1
    result = 0
    n = len(parts)
    i = 0

    # Assuming all operator fns are in g(u, v) form
    # And all test operator fns use the whole stack
    while i < n:
        part = parts[i]
        if part == 'd':
            u, v = parts[i-1], parts[i+1]
            stack += roll(u, v)
            last_rolled_sides = v
            i += 1
        elif part in __OPERATORS:
            i += 1
            result = __OPERATORS[part](result, parts[i])
        elif part == '!' and last_rolled_sides > 1:
            explode_limit = __EXPLODE_LIMIT
            explode_list = list(stack)
            exploding = True
            while exploding and explode_limit > 0:
                explode_count = len([x for x in explode_list if x == last_rolled_sides])
                if explode_count > 0:
                    explode_roll = [roll(1, last_rolled_sides) for x in explode_list if x == last_rolled_sides]
                    explode_roll = reduce(add, explode_roll)
                    explode_list = list(explode_roll)
                    stack += explode_roll
                else:
                    exploding = False
                explode_limit -= 1
        elif part in __TEST_OPS:
            DO_SUM = False
            op = __TEST_OPS[part]
            value = parts[i + 1]
            output = [x for x in stack if op(x, value)]
            if output:
                result = output
            else:
                result = None

        i += 1

    if sum([1 for i in stack if i in __FATE]) > 0:
        result = {
            __FATE[0]: stack.count(__FATE[0]),
            __FATE[1]: stack.count(__FATE[1]),
            'total': stack.count(__FATE[0]) - stack.count(__FATE[1])
        }
    else:
        if DO_SUM:
            result += sum(stack)
    return (stack, result)

def deunicode(content):
    output = content

    output = output.replace('\u20e3', '')
    output = output.replace('\U0001f51f', '10')
    output = output.replace('\U0001f522', '4')
    output = output.replace('\U0001f4af', '100')

    return output

def lex(content):
    # Attempt to comprehend what we've been given.
    content = content.replace(' ', '').lower().strip()
    content = deunicode(content)

    actions = list()
    appending = False
    value = 0
    i = 0
    n = len(content)

    if content == 'fate':
        actions += [4, 'd', 'f']
    else:
        while i < n:
            symbol = content[i]
            symbol_p = str(content[i:i+2])
            if symbol in __NUMBERS:
                if symbol == 'f':
                    actions.append(symbol)
                    appending = False
                    value = 0
                else:
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
                    actions.append(symbol)
                elif symbol_p in __TEST_OPS:
                    actions.append(symbol_p)
                    i += 1
                elif symbol == '!':
                    actions.append(symbol)
                else:
                    return (None, None)
            i += 1
    
        if appending:
            actions.append(value)

    return actions

