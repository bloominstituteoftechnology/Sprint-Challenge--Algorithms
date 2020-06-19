'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import time
start_time = time.time()

def count_th(word):

    if word == word.count('th'):
        return 1
    else:
        return word.count('th')

end_time = time.time()
word = 'the ant and the'
print(count_th(word))
print (f"runtime: {end_time - start_time} seconds")

    






    