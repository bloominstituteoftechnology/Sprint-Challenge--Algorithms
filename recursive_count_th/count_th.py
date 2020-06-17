'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def adder(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + adder(list[1:])
    

def count_th(word, n = 0, count = []):
    # TBC

    stringList = list(word)

    if stringList[n] + stringList[n + 1] == "th":
        count.append(1)
        
    if n == len(stringList) - 2:
        return 0

    count_th(stringList, n + 1)

    return adder(count)
    

print(count_th("abcthefthghith")) # count = 3
