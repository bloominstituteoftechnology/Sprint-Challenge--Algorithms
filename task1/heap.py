
class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    #if right or left child is greater than root, swap/reconstruct

  def delete(self):
    #start at root, delete 
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
    #if right or left child is greater than root, swap/reconstruct
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    #moving down through tree
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

# HEAPSORT IMPLEMENTATION -----------------------------------

def heapsort(arr):
  new_array = []
  new_heap = Heap()
  
  for i in arr:
    new_heap.insert(i)
    #traverse tree, check if right or left child is greater than root, then swap/reconstruct if needed
  
  for i in arr:
    root_max = new_heap.delete()
    #start at root, delete 
    new_array = [root_max] + new_array
    #deleted item, becomes sorted and added to sorted array

  return new_array


''' - didn't read directions closely enough, so created the helper function that was already defined in class-
#heapify = helper function to validate max heap structure and reconstruct heap if needed after an item is sorted
def heapify(arr, n, i):
  maximum = i
  left = 2 * i + 1
  right = 2 * i + 2

  #is left greater than root?
  if left < n and arr[i] < arr[left]:
    maximum = left
  
  #is right greater than root? 
  if right < n and arr[maximum] < arr[right]:
    maximum = right

  #if right or left child is greater than root, swap/reconstruct
  if maximum != i:
    arr[i],arr[maximum] = arr[maximum],arr[i]

    #call heapify for each node remaining in heap/tree
    heapify(arr, n, maximum)
'''

''' - from misguided first attempt -
  n = len(arr)
  print(n)

  #reconstructing heap if needed before performing sort
  for i in range(n, -1, -1):
    heapify(arr, n, i)
  
  #sorting, swaping root node with last item
  for i in range(n-1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)

'''


