'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # initialize count variable

    # check if word is "th"
    if word == "th":
        return 1
    # check if word is 2 length and isn't "th"
    elif len(word) == 2 and word != "th":
        return 0
    # check if length of word is 1 or 0
    elif len(word) <= 1:
        return 0

    else:
        # split word in half
        half = len(word) // 2

        left_half = word[:half]
        right_half = word[half:]

        # recursively call count_th and add the results of each half together
        count = count_th(left_half) + count_th(right_half)
        # return count but check the odd case
        return count + count_th(word[half-1] + word[half])


print(count_th("abcthxyz"))
