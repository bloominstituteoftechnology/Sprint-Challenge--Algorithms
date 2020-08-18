'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # make the whole word lowercased to check for case insensitive "th"
    word.lower()
    # initialize a count variable to keep track of the count
    if "th" not in word:
        return 0
    else:
        new_word = word.replace("th", "", 1)
        return count_th(new_word) + 1

word = "abcthefthghith"
print(count_th(word))
