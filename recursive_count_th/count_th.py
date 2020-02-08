'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    if 'th' not in word:
        return count
    else:
        pos = word.find('th')
        if pos != -1:
            count += 1
            return count_th(word[pos + 2:], count)
        else:
            return count
