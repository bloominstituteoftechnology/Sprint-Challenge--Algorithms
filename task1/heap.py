def heapsort(arr):
  heap_arr = []  # O(1)
  heap = Heap()  # O(1) size n heap

  #O(nlog(n))
  for item in arr:   # O(n)
  # insert item to heap one at a time
    heap.insert(item)  # O(log(n))
  # delete items from heap and add to arr either at front 
  # or end of the array and reverse it

  #O(nlog(n)) and O(n^2) if you do insert at front
  while len(heap.storage) > 0:  # O(n)
  # while heap.get_size() > 0
    deleted_item = heap.delete()  # O(log(n))
    # delete returns the max items in a list
    heap_arr.append(deleted_item)  #O(1)
    # can do insert at the beginning instead: heap_arr.insert(0, deleted_item) #O(n) 
    # wouldn't need to reverse it
  heap_arr.reverse() #O(n)
  return heap_arr

# heapsort([2, 4, 4, 5, 7, 1])

# heap stored as tight array
# can find child by doing i * 2 + 1, i *2 + 2
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