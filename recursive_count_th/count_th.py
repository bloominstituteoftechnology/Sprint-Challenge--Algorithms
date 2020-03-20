'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # n1 = 0
    # n2 = 2
    # count = 0
    # text = word[n1:n2]
    
    # if text.find("th") == -1:
    #     return 0
    # elif text[:-1] == None:
    #     return count
    # else:
    #     count += 1
    #     n1 += 1
    #     n2 += 1
    # return count_th(word)
        
    #return count(word)

# return count_th(word)
# return count

    return word.count("th")





# print(count_th("th"))
# print(count_th("abcthefthghith"))