'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0
def count_th(word):
    
    # TBC
    # print(f"word length: {len(word)}")
    substr = "th"

    if len(word) < 2:
        global count
        return count

    # print(word[2:])

    if word[:2] == substr:
        count += 1
        # print(f"count: {count}")
        return count_th(word[2:])

    return count_th(word[1:])

print(count_th("ht"))