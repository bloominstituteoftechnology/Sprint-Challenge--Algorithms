'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
  def colunting_th(word, count):
    index = word.find('th')
    # add th to count if found and check if any more
    if index != -1:
      count += 1 + colunting_th(word[index + 2], count)
    return count

  return colunting_th(word, 0)
    