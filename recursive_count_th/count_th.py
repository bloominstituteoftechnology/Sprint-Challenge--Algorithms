'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
cache = {'th':0}
def count_th(word):
    print('---')
    print(word)
    if len(word) < 2:
        print("last step!", word)
        return cache['th']
    if word[-2:] == 'th':
        print("increment step", word)
        cache['th'] += 1
        print(cache['th'])
    print('xxx')
    return count_th(word[:-1])

cache = {'th':0}
def count_th(word):
    if len(word) < 2:
        return cache['th']
    if word[-2:] == 'th':
        cache['th'] += 1
    return count_th(word[:-1])