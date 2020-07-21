'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    letters = list(word)
    # TBC
    if len(letters) < 2:
        return 0
    elif letters[0] == 't' and letters[1] == 'h':
        count += 1

    # slice off the first letter of 'word'
    # slicing off the first TWO letters won't work because the 'word' might be: 2th3adt
    return count + count_th(letters[1:])
    
a = [4, 3, 4, 5, 2]
print(a[1:])