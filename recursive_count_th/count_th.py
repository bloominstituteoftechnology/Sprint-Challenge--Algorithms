'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #     define base case
  if len(word) < 2:
    return 0
  else:
      # if first two letters are 'th' that is one occurance
      # recurse at this point with slice of str dropping the accounted for
    if word[0:2] == "th":
      return 1 + count_th(word[2:])
      # if first two letters not 'th', move up by one letter and check again
    else:
      return count_th(word[1:])

