'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    
    if word[:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])


print(count_th('worhit'))