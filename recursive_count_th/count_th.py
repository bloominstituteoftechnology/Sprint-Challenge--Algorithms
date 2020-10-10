
def count_th(word):
    """
    Your function should take in a single parameter (a string `word`)
    Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
    Your function must utilize recursion. It cannot contain any loops.
    """
    # hit a base case where there are no th to count
    x = "th" in word
    # if "th" is in word, it would be True
    if x is True:
        # when you split only one time, it's gets rid of the first th then split into two list
        word = word.split("th", 1)
        # this is where then we splice the list to just only the second half of the string
        word = word[1:]
        # we would then use recursion to countinue the splits until we hit our base case
        # which then we would return all the one's that it has added up
        # Note: "".join(word) is used to convert the list to a string. "th" in word doesn't work on list
        # so it will always be False once recused
        return 1 + count_th("".join(word))
    else:
        # Base Case
        # We either hit this if we no th's in our list or we have nothing literally in string
        return 0