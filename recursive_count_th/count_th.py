'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
count = 0
     substring = 'th'
     for chars in range(len(word)):
         print(word[chars : chars+2])
         if word[chars:chars+2] == substring:
             count += 1

     return count
