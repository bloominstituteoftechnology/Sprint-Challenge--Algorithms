

def heapsort(arr):
  result = []
  heap = Heap()
  for x in arr:
    heap.insert(x)
  print("HEAP", heap)
  while heap.get_size() > 0: #O(n)
    v = heap.delete()
    result.insert(0, v)
  return result
  new_heap = []
  sorted_heap = []
  l = len(arr)
  def grow_heap(arr):
    print('ARR', arr)
    for el in arr:
      new_heap.append(el)
      index = len(new_heap) - 1
      while (index - 1) // 2 >= 0: # while index > 0 or parent not at head
        if new_heap[(index - 1) // 2] < new_heap[index]: # if parent < new el
          # swap parent and new el
          new_heap[index], new_heap[(index - 1) // 2] = new_heap[(index - 1) // 2], new_heap[index]
        index = (index - 1) // 2  # index is now parent
    print('NEW', new_heap)
    return new_heap
  next_heap = grow_heap(arr)
  # head = next_heap[0]
  # def get_head(old, new):
  #   head = old[0]
  #   new.append(head)
  #   print('old', old)
  #   print('new', new)
  #   print(old, new)
  #   if len(old) == 1:
  #     return new
  #   print('OLD', old)
  #   return grow_heap(old[1:])
  # print('NEXT', next_heap)
  # get_head(next_heap[1:], [head])
  # # print(x)
# print(heapsort([2, 1, 3, 6, 10, 5, 7, 0, 8, 9, 4]))

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

  # # while len(sorted_heap) < l:
  # #   print(len(sorted_heap))
  # def get_heap_head(new_heap):
  #   index = 0
  #   retval = new_heap[0]  # head aka largest number
  #   print('NEW HEAP 0', new_heap)
  #   new_heap[0] = new_heap[-1:][0]  # new head is last val in arr
  #   new_heap.pop() # pop off last val since it is a duplicate
  #   print(index * 2 + 1, len(new_heap) - 1)
  #   print('NEW HEAP 1', new_heap)
  #   for i in range(len(new_heap)):
  #     while index * 2 + 1 <= len(new_heap) - 1: # while index 1 < last index
  #       if index * 2 + 2 > len(new_heap) - 1:
  #         mc = index * 2 + 1  # if 2 > last index ==> max child = 1
  #       elif new_heap[index * 2 + 1] > new_heap[index * 2 + 2]:
  #         mc = index * 2 + 1  #  elif val 1 > val 2  ==> max child = 1
  #       else:                 # return max child = 2
  #         mc = index * 2 + 2
  #       if new_heap[index] < new_heap[mc]: # if val of new head < max child
  #           # swap parent and max child
  #           new_heap[index], new_heap[mc] = new_heap[mc], new_heap[index]
  #       print('HEAP', new_heap)

  #       print('RETVAL', retval)
  #       return retval 
    
  #   return retval
  # head = get_heap_head(new_heap)
  # sorted_heap = [head] + sorted_heap
  # print('SORTED', sorted_heap)
  # while len(sorted_heap) < l:
  #   print('SORTED', sorted_heap)
  #   head = get_heap_head(new_heap)
  #   sorted_heap = [head] + sorted_heap
  #   get_heap_head(new_heap)
  # return sorted_heap
  # print('NEW HEAP 2', new_heap)
  # # if new_heap[1] > new_heap[0]:
  # #   new_heap[1], new_heap[0] = new_heap[0], new_heap[1]
  # print(sorted_heap)
  # return sorted_heap + new_heap