'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import time
start_time = time.time()

def count_th(word):
    # set the counter var at 0
    letter_count = 0
    # set the base case up using length
    if len(word) <= 1:
        return 0

    
    if word[0] == 't' and word[1] == 'h':
        letter_count += 1
    
    return count_th(word[1:]) + letter_count

end_time = time.time()
word = 'the ant and the'
print(count_th(word))
print (f"runtime: {end_time - start_time} seconds")

    






    