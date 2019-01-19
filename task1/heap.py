def heapsort(arr):
  sorted_heap = []
  heap = Heap()
  for el in arr:    #O(n)
    heap.insert(el) #O(log n)
                    # => These are nested so they are O(n log n)

# .insert
# for element in the arr (parameter) it appends the heap's storage
# then it bubbles up
# temp_index is the last item
# while temp_index > 0              
#   if val of the temp_val's parent < val at temp_index
#     swap parent and val at temp_index
#   temp_index is now the parent 

# Heap is partially orded.
# Largest value is at the head

  while heap.get_size() > 0:  # len() is O(1)
    v = heap.delete()         #O(log n)
    sorted_heap.insert(0, v)  #O(log n)  # These run one after the other so
                                        # It is O(2 * log n ) = > O(log n)
  return sorted_heap

# while len of heap > 0
# Return Value is head of the heap (largest value)
# move item at the end of the heap to the front
# pop off the back of the heap (since it is a duplicate of the front)
# then, sift down zero 
#  while zero * 2 + 1 (aka index 1) <= last item of heap:
#     if index 2 > last item of heap
#       mc (max child) is index 1
#     elif val > val 2 
#       mc is index 1
#     else:
#       mc is index
#     if val of new head < max child
        # swap parent and max child
#  return Return Value from above  
# 

# Insert the Return Value into the insert function above to make sure that the sorted array remains sorted



# # Insert 

# def heapsort(arr):
#   new_heap = []
#   sorted_heap = []
#   print(arr)
#   def grow_heap(arr):
#     for el in arr:
#       new_heap.append(el)
#       index = len(new_heap) - 1
#       while (index - 1) // 2 >= 0: # while index > 0 or parent not at head
#         if new_heap[(index - 1) // 2] < new_heap[index]: # if parent < new el
#           # swap parent and new el
#           new_heap[index], new_heap[(index - 1) // 2] = new_heap[(index - 1) // 2], new_heap[index]
#         index = (index - 1) // 2  # index is now parent
#     return new_heap
#   
# Incomplete .delete

#     # while index * 2 + 1 <= len(post_heap) - 1: # while index 1 < last index
#     #   if index * 2 + 2 > len(post_heap) - 1:
#     #     mc = index * 2 + 1  # if 2 > last index ==> max child = 1
#     #   elif post_heap[index * 2 + 1] > post_heap[index * 2 + 2]:
#     #     mc = index * 2 + 1  #  elif val 1 > val 2  ==> max child = 1
#     #   else:                 # return max child = 2
#     #     mc = index * 2 + 2
#     #   if post_heap[index] < post_heap[mc]: # if val of new head < max child
#     #       # swap parent and max child
#     #       post_heap[index], post_heap[mc] = post_heap[mc], post_heap[index]
#     #   print('HEAP', post_heap)

                #           2
                #     5           3
                # 0       6    1


                #           6
                #     5           3
                # 0       2     1

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
  def set_heap(self, items):
    self.storage = items

  