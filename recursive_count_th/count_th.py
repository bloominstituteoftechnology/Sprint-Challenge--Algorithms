'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    substring = "th"
    word_count = len(word)
    substring_count = len(substring)

    # TBC
    
    if word_count == 0 or word_count < substring_count:
        return 0
    elif word[0: substring_count] == substring:
        return count_th(word[substring_count - 1: ]) + 1
    else:
        return count_th(word[substring_count - 1: ])