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

# if __name__ == "__main__":
#   print(heapsort([2,9,5,7,1,8,5,6,3,1,9,5,0,1,2,1]))

def heapsort(arr):
  heap = Heap()
  sorted = []
  for num in arr:
    heap.insert(num)
  while heap.get_size() > 0:
    sorted.append(heap.delete())
  sorted.reverse()
  return sorted

def heapsort_inplace(arr):
  heap = Heap()
  for num in arr:
    if len(heap.storage) == len(arr):
      break
    heap.insert(num)

  for idx in range(len(arr)):
    arr[idx] = heap.delete()
  arr.reverse()
  return arr
print(heapsort_inplace([13, 85, 2, 10, 27]))