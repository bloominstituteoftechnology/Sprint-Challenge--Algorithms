'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Start with a base case
    # If the word only has 1 letter, it cannot contain "th"
    if len(word) <= 1:
        return 0
    # Looking for occurrences of "th" within a given word.
    # Must start with t so we check everything following our initial index[0]
    # Utilize recursion. Cannot use ANY loops. 
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])