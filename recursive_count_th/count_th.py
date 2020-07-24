def count_th(text):
    """
    Counts the number of occurences of the string "th" within the input text string.
    """
    # Base case: Fewer than 2 characters in word:
    if len(text) < 2:
        return 0

    # Recurse toward the base case:
    if text[:2] == "th":
        return 1 + count_th(text[2:])
    else:
        return 0 + count_th(text[1:])
