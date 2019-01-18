from timeit import default_timer as timer

#################
# Max Heap Sort #
#################

class MaxHeap:
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

max_heap = MaxHeap()

def max_heapsort(arr):
  # result = []
  length = len(arr)

  for i in range(0, length):
    max_heap.insert(arr.pop())
  
  for i in range(0, length):
    biggest = max_heap.delete()
    arr = [biggest] + arr

  return arr

#################
# Min Heap Sort #
#################

class MinHeap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[len(self.storage) -1]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_min(self):
    return self.storage[len(self.storage) -1]

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

min_heap = MinHeap()

def min_heapsort(arr):
  # result = []
  length = len(arr)

  for i in range(0, length):
    min_heap.insert(arr.pop())
  
  for i in range(0, length):
    biggest = min_heap.delete()
    arr = arr + [biggest]

  return arr


#############################
# Troubleshooting test code #
#############################

def create_array(size = 10, max = 99):
    from random import randint
    return [randint(0, max) for _ in range(size)]

def test_max_heap(places, times = 1000):
    heap_max_arr = create_array(places)
    print(f'len(n) {places} run {times} times')
    mh_start = timer()
    for i in range(0, times):
        max_heapsort(heap_max_arr)
    mh_stop = timer()
    print(mh_stop - mh_start)



# heap_min_arr = create_array()
# print(f'Before: {heap_min_arr}')
# print(f'After: {min_heapsort(heap_min_arr)}')
# print('          ^^ Yeah, that\'s not right ^^\n')

print('MAX HEAP TIME COMPLEXITY')
test_max_heap(10)
test_max_heap(100)
test_max_heap(1000)
test_max_heap(10000)

