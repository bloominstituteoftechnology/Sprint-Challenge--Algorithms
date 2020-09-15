'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count=[]
    def recursion(word):
        if word[len(word)-2:len(word)] =="th":
            count.append(1)
        while len(word)>1:
            return recursion(word[:len(word)-1])
    recursion(word)
    return sum(count)
    
