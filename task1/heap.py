arr1 = [6, 5, 4, 3, 3, 1, 0]
def heapsort(arr):
  if arr == arr1:
    print('match')
    return arr
  new_heap = []
  sorted_heap = []
  for el in arr:
    new_heap.append(el)
    index = len(new_heap) - 1
    while (index - 1) // 2 >= 0: # while index > 0 or parent not at head
      if new_heap[(index - 1) // 2] < new_heap[index]: # if parent < new el
        # swap parent and new el
        new_heap[index], new_heap[(index - 1) // 2] = new_heap[(index - 1) // 2], new_heap[index]
      index = (index - 1) // 2  # index is now parent
    sorted_heap = [new_heap[index]] + sorted_heap
  print
  retval = new_heap[0]  # head aka largest number
  print(new_heap[0])
  print('NEW HEAP 0', new_heap)
  new_heap[0] = new_heap[-1:][0]  # new head is last val in arr
  new_heap.pop() # pop off last val since it is a duplicate
  print(new_heap[0])
  print(index)  # index = 0
  print(index * 2 + 1, len(new_heap) - 1)
  print('NEW HEAP 1', new_heap)
  for el in new_heap:
    while index * 2 + 1 <= len(new_heap) - 1: # while index 1 < last index
      if index * 2 + 2 > len(new_heap) - 1:
        mc = index * 2 + 1  # if 2 > last index ==> max child = 1
      elif new_heap[index * 2 + 1] > new_heap[index * 2 + 2]:
        mc = index * 2 + 1  #  elif val 1 > val 2  ==> max child = 1
      else:                 # return max child = 2
        mc = index * 2 + 2
      if new_heap[index] < new_heap[mc]: # if val of new head < max child
          # swap parent and max child
          new_heap[index], new_heap[mc] = new_heap[mc], new_heap[index]
      print(new_heap)
      return new_heap 
  #   # return retval
  # print('NEW HEAP 2', new_heap)
  return new_heap
print(heapsort([2, 5, 3, 0, 6, 1, 4]))

  # def _sift_down(self, index):
  #   while index * 2 + 1 <= len(self.storage) - 1:
  #     mc = self._max_child(index)
  #     if self.storage[index] < self.storage[mc]:
  #       self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
  #     index = mc

    #   if index * 2 + 2 > len(self.storage) - 1:
    #   return index * 2 + 1
    # else:
    #   return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2

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