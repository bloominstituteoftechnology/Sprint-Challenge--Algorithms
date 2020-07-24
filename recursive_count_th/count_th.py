'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    first = 0
    second = 1
    #print(word)
    #base
    
    print(len(word))
    if len(word) < 2:
        #print('stop')
        return 0
    else:
        together = word[first] + word[second]
        print(together)
        total = 0
        if together == 'th':
            total = 1
        # print('th')
        
        new_word = word[1:]
        #print('new word',new_word)
    #return count + recursion count
        return total + count_th(word[1:])

print(count_th("abcthxyz"))

    # print(len(word))
    # if len(word) >= 2:
        
    #     together = word[first] + word[second]
    #     print('together', together)
    #     if together == 'th':
    #         return 1
    #     else:
    #         return 0
        # print('th')
        
    # new_word = word[1:]
    # print('new word',new_word)
    # return count_th(word[1:])

# print(count_th('hrthethw'))

# print(len(word))
#     if len(word) < 2:
#         print('stop')
#         return 0
#     together = word[first] + word[second]
#     if together == 'th':
#         return 1
#     else:
#         return 0
#         # print('th')
        
#     # new_word = word[1:]
#     # print('new word',new_word)
#     return count_th(word[1:])




# count = 0
#     #split in two
#     for i in range(1, len(word)):
#         together = word[i - 1] + word[i]
#         if together == 'th':
#             count += 1
#     #base - until check last two letter
#         if i+1 == len(word):
#             return count