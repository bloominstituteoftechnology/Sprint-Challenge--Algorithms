'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# added count to function definition so that it may increment as it recurses
def count_th(word, count = 0):
    if len(word) < 2: #base case
        return count

    #if th in word we slice from 2nd index, else from 1st index
    if word[:2] == 'th':
        count += 1
        return count_th(word[2:], count)
    else:
        return count_th(word[1:], count)