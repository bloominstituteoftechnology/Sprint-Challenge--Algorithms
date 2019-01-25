def heapsort(arr):

  #Creates an empty max heap and inserts the items in the array one by one
  heap = Heap()
  for i in arr:     # O ( N )
    heap.insert(i)
  
  #Get length of the heap minus one to index 
  length = len(heap.storage)
  sorted_list = []

  while length > 0: # O (N)
    sorted_list.insert(0, heap.get_max())
    heap.delete() # O (log n)
    length -= 1
  return sorted_list
 

 
#A max heap - Items are stored in a special order such that the value in a parent node is greater than the values in its two children nodes
"""
For example
4, 10, 3, 5, 1


      Finished max heap:

          10 (0 index)

    5 (1)        3 (2)

4 (3)   3 (4)   

"""

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

if __name__ == "__main__":
  print(heapsort([2,9,5,7,1,8,5,6,3,1,9,5,0,1,2,1]))