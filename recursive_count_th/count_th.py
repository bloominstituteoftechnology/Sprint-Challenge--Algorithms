def count_th(word):
    '''
    Your function should take in a single parameter (a string `word`)
    Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
    Your function must utilize recursion. It cannot contain any loops.
    '''

    # TBC - one base case is if len(word) < 2, can't have "th" in it
    if len(word) < 2:
        return 0

    # another base case - first two letters include "th"
    if word[0:2] == "th":
        # count it and go again on the rest
        return 1 + count_th(word[1:])

    # otherwise, move closer to base case by calling function on rest of word
    else:
        return count_th(word[1:])


if __name__ == "__main__":
    word = ""
    print(count_th(word))  # > Exp Out: 0

    word = "abcthxyz"
    print(count_th(word))  # > Exp Out: 1
