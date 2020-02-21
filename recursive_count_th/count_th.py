'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# BELOW CONTAINS NO PRINT STATEMENTS
def count_th(word):
    if len(word) < 2:
        return 0
    elif (word[0:2] == 'th'):
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])



# # BELOW CONTAINS PRINT STATEMENTS
# def count_th(word):
#     if len(word) < 1:
#         # print('a')
#         return 0
#     if (word[0] == 't') and (len(word) > 1):
#         # print(f'b = {word[0]}')
#         if word[1] == 'h':
#             # print(f'c = {word[1]}')
#             return 1 + count_th(word[2:])
#         else:
#             # print('d')
#             return 0 + count_th(word[1:])
#     else:
#         # print('e')
#         return 0 + count_th(word[1:])


# print(count_th('thhtthht'))


# a = 'abcd'
# print(a[2:])

# def count(arr, n):
#     if len(arr) < 1:
#         return 0
#
#     if arr[0] == n:
#         return 1 + count(arr[1:], n)
#     else:
#         return 0 + count(arr[1:], n)