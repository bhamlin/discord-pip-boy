#!env/bin/python3

import os

from pydblite import Base

class AbstractChar:
    def __init__(self, level=0):
        self.level = level

class D20Char(AbstractChar):
    def __init__(self, level=0, stats=None):
        super().__init__(level)
        if not stats:
            stats = dict()
        self.stats = stats

db = Base('test.pdl')

db.create('owner', 'name', 'game', 'char', mode='override')

c = D20Char(1, {
    'str': 
