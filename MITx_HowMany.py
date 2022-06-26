animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
 '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
 '''
 count = 0
 for v in aDict.values():
  for item in v:
   count += 1
 return count

print(how_many(animals))