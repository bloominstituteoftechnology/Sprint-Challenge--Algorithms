def heapsort(arr):
  # Make a new heap
  heap = Heap()
  
  for item in arr:	# O(n)
      heap.insert(item) # O(log n)
    
  # total so far = O(n*log n)
      
  # loop from 11, 10, 9, ... We are filling the array with the largest value at the end and going up to the beginning, so the sorted array is always [smallest,...,largest]
#  for i in range(len(arr) - 1, -1, -1):	# O(n)
#    # Get largest item and delete it	
#    largestItem = heap.delete() # O(log n)
#    arr[i] = largestItem	# O(1)
    
    # total here = O(n) * (O(log n) + O(1)) = O(n * (log(n) + 1)) => O(n * log(n))
    
    
  ## Stretch goal: max to min
  # We are filling the array from the beginning to the end, but the sorted array is always [smallest,...,largest].
  for i in range(len(arr)):
    largestItem = heap.delete() # O(log n)
    arr[i] = largestItem	# O(1)
    
  
  return arr
    
  # final total = O(n * log(n)) + O(n * log(n)) => O(2n*log(n))

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

#  def _bubble_up(self, index):
#    while (index - 1) // 2 >= 0:
#      if self.storage[(index - 1) // 2] < self.storage[index]:
#        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
#      index = (index - 1) // 2
#      
#  def _sift_down(self, index):
#    while index * 2 + 1 <= len(self.storage) - 1:
#      mc = self._max_child(index)
#      if self.storage[index] < self.storage[mc]:
#        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
#      index = mc
#      
#  def _max_child(self, index):
#    if index * 2 + 2 > len(self.storage) - 1:
#      return index * 2 + 1
#    else:
#      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2



  # Stretch goal: max to min      
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
      
"""
Stretch problem: Min versus Max

In the heapSort(), I reused the input array to be the output array so save space.
I changed the range of the for-loop to go from beginning to end, and fill in the values as it is being pulled out from the heap.
I switched the signs(<,>) in bubble_up(), sift_down(), and min_child().

The time complexity doesn't change; it's still O(n log(n)).
The wall clock time of the min heap version is neither faster nor slower. It's still the same as before, because we're reusing the input array and replacing indexes is O(1). But if we were making a new array, the min would be faster because we are not inserting at 0.

"""