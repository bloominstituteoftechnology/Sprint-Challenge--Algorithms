'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

th_count = 0
curr = -1

def reset():
    global th_count
    global curr
    th_count = 0
    curr = -1

def count_th(word):
    global th_count
    global curr

    curr += 1
    # print(curr)
    # print(curr, word[curr], len(word[:-1])) 
    if len(word) == 0:
        return 0

    if curr < len(word[:-1]):
        if word[curr] == "t" and word[curr+1] == "h":
            print(th_count)
            th_count += 1
            print(th_count)
        return count_th(word)

    temp = th_count
    print(f'{word}\n"th" count : {th_count}/{temp}')
    reset()
    return temp


# count_th("the")
print(count_th("thhtthht"))
# count_th("with")
# count_th("Ththththththththt")
# count_th("")