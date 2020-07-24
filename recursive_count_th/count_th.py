'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #create a count
    count = 0

    #return values or the input
    list_breakdown = list(word)
    
    #base case or less than 2 since we are looking for 2 letters 
    if(len(list_breakdown)) < 2:
        return 0

    #base case of finding them right away?????

    elif list_breakdown[0] == "t" and list_breakdown[1] == "h":
        count +=1

    return count + count_th(list_breakdown[1:])


