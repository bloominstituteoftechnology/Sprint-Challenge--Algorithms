'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    i = 0
    while word:
        if word[i] == "t" and word[i + 1] == "h":
            count +=1
            i +=1
    return print("count"{count})
    pass

count_th(["thththh"])