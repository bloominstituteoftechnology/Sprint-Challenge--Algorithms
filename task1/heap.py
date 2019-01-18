"""
Heapsort pseudocode:

- First we'll need to establish a heap and another list to hold our resulting data
- Go over the given array (arr) and use Heap's insert() function to add the values
- Analyze the heap with get.size() and use sift_down where appropriate (get.size > 0)
- Call the delete() function and append the result to the heap, increment counter
- Return the result, which is our new properly ordered heap

"""

def heapsort(arr):
  heap = Heap()
  result = []
  
  for i in arr:
    heap.insert(i)
  
  # new i value
  i = 0
  while heap.get_size() > 0:
    '''
     This bit saves some time: initially I used insert here, but append runs faster.
     To compensate the return now uses [::-1] to reverse the order as necessary.
     I don't think this changes runtime, just a small optimization change.
    '''
    heap._sift_down(i)
    result.append(heap.delete())
    i += 1

  return result[::-1]
 

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