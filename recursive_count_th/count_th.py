'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    if word == "":
        return 0
    else:
        if word.find("th") == -1:
            return 0
        else:
            newindex = word.find("th")
            newword = word[newindex+2:]

            return(1+count_th(newword))
    
    pass
