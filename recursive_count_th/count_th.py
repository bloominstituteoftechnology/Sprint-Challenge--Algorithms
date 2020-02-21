'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of *"th"* occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    n = word.find("th")
    if n == -1:
        return 0 #if no th in word then return 0
    return 1 + count_th(word[n + 2:]) #if th is there it will keep calling it till there are no more "th"
 