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

class Min_Heap:
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

  def get_min(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] > self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._min_child(index)
      if self.storage[index] > self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _min_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] < self.storage[index * 2 + 2] else index * 2 + 2

# Max Heapsort
def heapsort(arr):

  # Declare a new list to store our sorted data into:
  sorted = []
 
  # First, let's 'heapify' our array data:
  heap = Heap()
  for i in arr:
    heap.insert(i)    

  # Next, we should iteratively remove the top node of the heap and add it to our sorted list until the heap is empty:
  for i in range(0, heap.get_size()):
    sorted = [heap.delete()] + sorted

  # Finally, we return our list, now with the elements sorted.
  return sorted


# Min Heapsort
def min_heapsort(arr):
  
  # Declare a new list to store our sorted data into:
  sorted = []
 
  # First, let's 'heapify' our array data:
  heap = Min_Heap()
  for i in arr:
    heap.insert(i)    

  # Next, we should iteratively remove the top node of the heap and add it to our sorted list until the heap is empty:
  for i in range(0, heap.get_size()):
    sorted = sorted + [heap.delete()]

  # Finally, we return our list, now with the elements sorted.
  return sorted

# Testing Heap / heapsort

# test_array = [15, 19, 10, 7, 17, 16, 12341, 34, 456, 76, 123]

# print(heapsort(test_array))
# print(min_heapsort(test_array))

# min_heap = Min_Heap()
# heap = Heap()

# for i in test_array:
#   heap.insert(i)   
#   min_heap.insert(i)

# print(heap.get_max())
# print(min_heap.get_min())

# Comparing Clock Time of min_heapsort and heapsort:
import random
import time

def gen_random_input(length, max):
  input = []
  for i in range(length):
    input.append(random.randint(0, max))
  return input

big_test = [gen_random_input(100, 500), gen_random_input(1000, 500), gen_random_input(10000, 500), gen_random_input(20000, 500), gen_random_input(30000, 500)]

for i in big_test:
  max_start = time.time()
  heapsort(i)
  max_finish = time.time()

  print("%d,%.10f" % (len(i), max_finish - max_start))

  min_start = time.time()
  heapsort(i)
  min_finish = time.time()

  print("%d,%.10f" % (len(i), min_finish - min_start))