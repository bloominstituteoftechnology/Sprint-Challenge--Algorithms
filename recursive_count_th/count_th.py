'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    search_string = "th"
    search_length = 2
    word_length = len(word)

    # TBC (The Base Case)
    # The string is to short for our substring "th" to fit.
    if word_length < search_length:
        return 0

    # Our search string ("th") matches the beginning of
    # the current sub-string.
    # Add 1 to the total and scroll forward 2 characters.
    if (word[0] == 't' and word[1] == 'h'):
        return 1 + count_th(word[2:])

    # Our search string doesn't match the beginning of the
    # substring. Move forward a character.
    return count_th(word[1:])
