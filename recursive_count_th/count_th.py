'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    
    # TBC
    l = list(word)

    if len(l) <= 1:
        return count

    if l[0:2] == ['t', 'h']:
        count += 1
    return count_th("".join(l[1:]), count)
