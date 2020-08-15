'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
Inside the `recursive_count_th` directory you'll find the `count_th.py` file. In this file, please add your recursive implementation to the `count_th()` method following these rules:

* Your function should take in a signle parameter (a string `word`)
* Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
* Your function must utilize recursion. 
  * It cannot contain any loops.

Run `python test_count_th.py` to run the tests for your `count_th()` function to ensure that your implementation is correct.
'''
def count_th(word):
    
    if len(word) > 1:
        if word[:2] == "th":
            return 1 + count_th(word[2:])
        else:
            return count_th(word[1:])
    return 0
   