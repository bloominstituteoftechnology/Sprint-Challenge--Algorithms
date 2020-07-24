'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC

    n1 = len(word)
    n2 = len("th")

    # Assuming there is no word or is smaller than length of 'th'
    if (n1 == 0 or n1 < n2):
        return 0
    # Range of 0 - length of th
    # Subtract each letter until find "th"
    if (word[0: n2] == "th"):
        return count_th(word[n2 - 1:]) + 1

    # Recursive return to add + 1 to count once "th" has been found
    return count_th(word[n2 - 1:])


count = count_th("thThthTHthth")

print(count)
