'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # TBC
    if word == "th":
        return word

    if word[0].lower() != "t" and word[1].lower() != "h":
        print(word)
        count_th(word[2] + word[2:])
    elif word[len(word)-2].lower() != "t" or word[len(word)-1].lower() != "h":
        print(f"elif: {word[:len(word)-1]}")
        count_th(word[:len(word)-1])


print(count_th("throw"))
