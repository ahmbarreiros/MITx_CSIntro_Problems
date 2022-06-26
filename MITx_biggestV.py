animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    newD = dict()
    if aDict is None: return None
    for pair in aDict:
     count = 0
     for item in aDict[pair]:
      count += 1
     newD[pair] = count
    maxC = max(newD.values())
    for k in newD:
     if newD[k] == maxC:
      return k
    return None

print(biggest(animals))

