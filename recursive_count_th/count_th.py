'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th = 'th'
    count = 0
    # TBC
    #base case?
    if th not in word:
        return (count)
    else: 
        #recursive function?
        index = word.find(th) #gives me index position of where 'th' starts in word
        count += 1 + count_th(word[index + 2:]) #add 1 to count + recursive call with word
        #                                        from index position plus 2 onwards
    return count


print(count_th('the'))
print(count_th("abcthefthghith"))
print(count_th("THtHThth"))
