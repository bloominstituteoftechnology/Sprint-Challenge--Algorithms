'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #start the counter at 0
    count = 0
    #start searching at the beginning
    letter_index = 0

    #base case - We run out of letters
    if len(word) <= 1:
        return 0
    # if the current index plus one matches increase count and move on to the next letter
    if word[letter_index : letter_index + 2] == "th":
            count += 1 + count_th(word[letter_index + 1: ])
    # if it doesn't match , then move on to the next letter without increasing our count
    if word[letter_index: letter_index + 2] != "th":
        count = count_th(word[letter_index + 1: ])
    return count
