'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):

    substring = "th"
    count = 0

    index = word.find(substring)
    if index >= 0:
        count += 1
        word = word[index + len(substring):]

        # increment count by recursively calling count_th
        count += count_th(word)
    return count