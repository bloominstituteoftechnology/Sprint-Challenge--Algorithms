'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, index=2, count=0):
  if word == "":
    return 0
  if index > len(word):
    return count
  if "th" in word[(index-2):index]:
    count += 1
  
  index += 1
  return count_th(word, index, count)
