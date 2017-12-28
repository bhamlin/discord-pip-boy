#!env/bin/python3

from pipboy import game

print(game.game_opt('bhamlin#6283', 'import {"name": "Covfefe", "race": "dwarf", "level": [1], "class": ["wizard#d20srd"], "class_features": [{"s12n": "conjuration"}], "stats": {"str": 10, "dex": 15, "con": 15, "int": 16, "wis": 11, "cha": 10}, "skills": {"spellcraft": {"class": true, "ranks": 1, "check": "int"}}, "feats": {"spell penetration": 1}}'))
print(game.game_opt('bhamlin#6283', 'export'))
