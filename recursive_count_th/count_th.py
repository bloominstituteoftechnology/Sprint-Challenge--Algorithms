'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, substring: str = 'th'):
    # base case of noting
    if word == "":
        return 0

    # seperate into head and tail
    # recurisvely call on tail
    # count by len of sub string if found and continue onto next
    if word[:len(substring)]==substring:
        return 1 + count_th(word[len(substring):])
    # increment count and continue next part
    else:
        return 0 + count_th(word[1:])
    
    
