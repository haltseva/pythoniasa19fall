"""
Assignment 1-A
==============

Update the Python script below to make it more compact and readable; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

"""

poem = '''
This is the house that Jack built.

This is the malt 
That lay in the house that Jack built.

This is the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cow with the crumpled horn, 
That toss'd the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milked the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the cock that crow'd in the morn, 
That waked the priest all shaven and shorn, 
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn, 
That tossed the dog, 
That worried the cat, 
That kill'd the rat, 
That ate the malt 
That lay in the house that Jack built.

This is the farmer sowing his corn, 
That kept the cock that crow'd in the morn, 
That waked the priest all shaven and shorn,
That married the man all tatter'd and torn, 
That kissed the maiden all forlorn, 
That milk'd the cow with the crumpled horn,
That tossed the dog, 
That worried the cat, 
That killed the rat, 
That ate the malt 
That lay in the house that Jack built.
'''
array1=['This is ','That kept ','That waked ','That married ','That kissed ','That milk\'d ','That tossed ','That worried ','That killed ','That ate ','That lay in ']
array2=['the farmer sowing his corn,','the cock that crow\'d in the morn,','the priest all shaven and shorn,',
'the man all tatter\'d and torn,','the maiden all forlorn,','the cow with the crumpled horn,','the dog, ','the cat, ','the rat,',
'the malt ','the house that Jack built.']
i=0
while i< len(array1):
    print(array1[i]+array2[len(array2)-i]+'\n')
    print('\n')
    i+=1


