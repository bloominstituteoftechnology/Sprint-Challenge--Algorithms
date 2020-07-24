'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base Case: Empty String,
    # contains no "th"
    if word == "":
        return 0

    # Special Case: beginning of string contains "th"
    # recursively returns shorter and shorter string.
    if word[0] is "t" and word[1] is "h":
        return 1 + count_th(word[1:])

    else:
        return 0 + count_th(word[1:])


if __name__ == "__main__":
    word = "thhtthht"
    print(count_th(word))