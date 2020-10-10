'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # initialize imputs for recursive function
    word = word
    target = 'th'

    def find(word, target):
        # sets the length of the list and target to use in targeting specific portions of the list
        word_len = len(word)
        target_len = len(target)
        # base case for recursion, if the word length is none or the word is shorter than what we are looking for 0 is returned
        if word_len == 0 or word_len < target_len:
            return 0
        # recursive case, checking the first two letters in the string against the target, if found it adds to the return, and shortens the input of the word by removing the first letter
        if word[0: target_len] == target:
            return find(word[target_len - 1:], target) + 1
        # if the target is not found, nothing gets added to the return, and the list is still shortened by removing the first letter
        return find(word[target_len - 1:], target)
    # case for checking to see if there is a valid word to check against, if there is, then the recursive function is run. If not, 0 is returned
    if len(word) >= len(target):
        return find(word, target)
    else:
        return 0
