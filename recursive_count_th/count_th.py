'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0, search_start=0):
    try:
        # find first index of 'th'
        found_at = word.index('th', search_start)
        # update next search start position
        search_start = found_at + 2
        # if found, increment count
        count += 1
        # remove 'th' from string and recurse
        return count_th(word, count, search_start)
    except:
        # else, return count
        return count
