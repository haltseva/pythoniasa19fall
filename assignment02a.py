"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text(encoding='utf8')
True
"""

def poem():
    a='This is '
    b='That kept '
    c='That waked '
    d='That married '
    e='That kissed '
    f='That milked '
    g='That tossed '
    h='That worried '
    i='That killed '
    k='That ate '
    l='That lay in '

    a1='the farmer sowing his corn,'
    b1='the cock that crowed in the morn,'
    c1='the priest all shaven and shorn,'
    d1='the man all tattered and torn,'
    e1='the maiden all forlorn,'
    f1='the cow with the crumpled horn,'
    g1='the dog,'
    h1='the cat,'
    i1='the rat,'
    k1='the malt'
    l1='the house that Jack built.'
    
    return f"{a}{l1}\n\n{a}{k1}\n{l}{l1}\n\n{a}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{g1}\n{h}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{f1}\n{g}{g1}\n{h}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{e1}\n{f}{f1}\n{g}{g1}\n{h}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{d1}\n{e}{e1}\n{f}{f1}\n{g}{g1}\n{h}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{c1}\n{d}{d1}\n{e}{e1}\n{f}{f1}\n{g}{g1}\n{h}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{b1}\n{c}{c1}\n{d}{d1}\n{e}{e1}\n{f}{f1}\n{g}{g1}\n{h}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n\n{a}{a1}\n{b}{b1}\n{c}{c1}\n{d}{d1}\n{e}{e1}\n{f}{f1}\n{g}{g1}\n{h}{h1}\n{i}{i1}\n{k}{k1}\n{l}{l1}\n"
'''
with open('data/poem-en.txt') as inp:
    r = inp.read()
 
res = poem()
for i in range(1000, 1201):
    print(i, res[i], r[i])

'''
if __name__ == '__main__':
    import doctest
    doctest.testmod()
