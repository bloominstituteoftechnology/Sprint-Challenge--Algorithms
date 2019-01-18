def heapsort(arr):
  '''
  description:
    this function uses a Heap class to sort a list

  pseudo code:
    - list = [] 
    - use insert function to add highest # to the list, then bubbles up a new max #
    - use delete function to remove the highest #, then sift down the smaller #s
    - list will be in descending order
      - how can i make it come out in ascending order?
    - return list
  '''
  # initialize Heap class
  heap = Heap()
  sorted_list = []

  # in the insert function, bubble_up function will swap the numbers make sure the largest number is on the left
  for i in arr:
      heap.insert(i)

  # in the delete function, sift_down function will move the smaller numbers to the right
  # when the largest # gets popped off, it'll get added to the sorted_list
  for i in arr:
    sorted_list.append(heap.delete())

  # reversing the list from descending to ascending order
  sorted_list.reverse()
  return sorted_list


class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2


# # try it out:
# arr = [4, 10, 3, 5, 1]
# print(arr)
# print(heapsort(arr))
