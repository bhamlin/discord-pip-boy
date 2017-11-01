#!env/bin/python3

import json
import os

from pydblite import Base

db = Base('test.pdl')

db.create('owner', 'name', 'game', 'char', mode='override')
db.create_index('owner')
db.create_index('game')

c = {
    'name': 'Covfefe',
    'race': 'dwarf',
    'level': [1],
    'class': ['wizard#d20srd'],
    'class_features': [{'specialization': 'conjuration'}],
    'stats': { 
        'str': 10,
        'dex': 15,
        'con': 15,
        'int': 16,
        'wis': 11,
        'cha': 10  },
    'skills': {
        'spellcraft': {
            'class': True,
            'ranks': 1,
            'check': 'int'
        }
    },
    'feats': {
        'spell penetration': 1,
    }
}

if not db._owner['bhamlin#6283']:
    db.insert(owner='bhamlin#6283', name='Covfefe', game=None, char=c)
    db.commit()

for rec in db._owner['bhamlin#6283']:
    q = rec['char']
    q['level'][0] += 1
    db.update(rec, char=q)
    db.commit()

for rec in (db('owner') == 'bhamlin#6283'):
    #print(rec)
    #print(json.dumps(rec['char']))
    print(rec['char']['name'], rec['char']['level'])

print()

# for rec in [rec for rec in db if rec['owner'] == 'bhamlin#6283']:
#     print(rec)
#     print(rec['char'].__dict__)
