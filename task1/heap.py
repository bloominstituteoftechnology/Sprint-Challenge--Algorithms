def heapsort(arr):
  result = []
  heap = Heap()

  # Insert all values of arr into the heap
  for i in arr:
    heap.insert(i)

  # For each item in the heap get max value and insert it at the beginning of the results array.
  while heap.get_size() > 0:
    result.insert(0, heap.delete())

  return result

def heapsort_min(arr):
  result = []
  heap = Heap()

  # Insert all values of arr into the heap
  for i in arr:
    heap.insert(i)

  # For each item in the heap get max value and insert it at the beginning of the results array.
  while heap.get_size() > 0:
    result.append(heap.delete())

  return result

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

  def delete_min(self):
    retval = self.storage[-1]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop(0)
    self._sift_down(0)
    return retval

  def get_max(self):
    return self.storage[0]

  def get_min(self):
    return self.storage[-1]

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