'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
print('RUNNING')



# adding second parameter to store count
# def count_th(word, count = 0):
#     print('count_th START', word)
#     # count = 0
#     if len(word) == 0:
#         return count
#     if word[0] == 't' and word[1] == 'h':
#         count += 1
#         return count_th(word[2:], count)
#     else:
#         return count_th(word[1:], count)
#
#



# ADDS SECOND PARAMETER
# def count_th(word, count = 0):
#     print('count_th START', word)
#     # count = 0
#     if len(word) == 0:
#         return count
#     if word[0] == 't' and word[1] == 'h':
#         count += 1
#         return count_th(word[2:], count)
#     else:
#         return count_th(word[1:], count)
#
#


# DOES NOT ACCOUNT FOR CASE
# def count_th(word):
#     up = word.upper()
#     if len(up) == 0:
#         return 0
#     elif up[0] == "T" and up[1] == "H":
#         up = up[2:]
#         return 1 + count_th(up)
#     else:
#         up = up[1:]
#         return count_th(up)
# print(count_th("thabcthth"))



#   WINNER
def count_th(word):
    if len(word) <= 1:
        return 0
    elif word[0] == "t" and word[1] == "h":
        word = word[2:]
        print('+1')
        return 1 + count_th(word)
    else:
        word = word[1:]
        return count_th(word)














    # TBC

    # UPER

    # UNDERSTAND
    #   RETURN HO MANY TIMES 'th' APPEARS
    #   DO NOT USE LOOPS
    #   USE IF, ELSE INSTEAD
    #   ASSUME DATA IS VALID BASED ON TESTS REQUIRED

    # numberOfOccurences = 0
    # position_countA = 0
    # countA = 0
    #
    # if 'th' not in word:
    #     return numberOfOccurences
    # else:
    #     print('else')
    #     if position_countA == word.find("th"):
    #         if countA != 0:
    #         numberOfOccurences = numberOfOccurences + countA
    #     print('countA')
    #     print(countA)
    #     print('numberOfOccurences')
    #     print(numberOfOccurences)
    #     return numberOfOccurences
    #









    # PLAN
    # IF word CONTAINS 'th' return int for number of times.
    # numberOfOccurences = 0
    # inStringBool = False
    # if word.find('th') == True:


    # END STATEMENT - WHEN WORD HAS NO MORE LETTERS
    # if word.length
    # if 'th' in word:
    #     print('IF STATEMENT')
    #     numberOfOccurences = numberOfOccurences + 1
    #     return count_th(word)
    #
    #
    # print('numberOfOccurences')
    # print(numberOfOccurences)
    # return numberOfOccurences

    # EXECUTE

    # REFLECT
print('FUNCTION CALL')
print(count_th('basdfasdfasdfasdfasdfasdfaevavatetrthththththhththththththththththththththTHTHTHTtHtHHtHtTHTHTHTTHTHTHTHTH'))
