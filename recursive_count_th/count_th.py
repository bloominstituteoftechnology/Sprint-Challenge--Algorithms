'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    
    # TBC
    if word == "":
        return count
    else:
        if word.find("th") == -1:
            return count
        else:
            newindex = word.find("th")
            newword = word[newindex+2:]
            count += 1
            print(count)
            return(count_th(newword, count))
    
    pass
