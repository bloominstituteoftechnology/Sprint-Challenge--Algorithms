'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
    
cache = {'count': 0}
def count_th(word):

    # get word length
    length = len(word)
    # if word is too small to find 'th'
    if length < 2:
        # save count
        count = cache['count']
        # empty cache
        cache['count'] = 0
        return count

    # find th
    search = 'th'
    if word[length-2:length] == search:
        # update count
        cache['count'] += 1

    # decrement word  
    word = word[:-1]
    
    return count_th(word)
