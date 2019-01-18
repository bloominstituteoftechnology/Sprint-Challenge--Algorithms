 

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

  def heapsort(self, input_arr):
    arr = []
    arr2 = input_arr
    for j in arr2:

      self.insert(j)
    # self.insert(54)
    # self.insert(56)
    # self.insert(7777)
    # self.insert(54)
    # self.insert(40)
    # self.insert(44)
    # self.insert(13)
    # self.insert(9)
    # self.insert(7)
    print(self._max_child(0))
    for i in range(0, len(self.storage)):
      # if self._max_child(i) <= len(self.storage)-1:
      arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
    # arr.append(self.delete())
        
        # self.storage[0], self.storage[self._max_child(i)] = self.storage[self._max_child(i)], self.storage[0]
        
    print(arr[::-1])
    return arr[::-1]
    # for i in range(0, len(self.storage) - 1):
    #   print(len(self.storage) - 1)
    #   print(self.storage[self._max_child(i)])
    #   maximum_child = self.storage[self._max_child(i)]
    #   parent = self.storage[i]
    #   # while self._max_child(i) < self.get_size():
    #   # maximum_child, parent = parent, maximum_child
    #   while maximum_child < len(self.storage) - 1:
    #     if parent < maximum_child:
    #       parent, maximum_child = maximum_child, parent
    #     else:
    #       parent, self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], parent
          
    print(self.storage)
    return self.storage
    
        

    pass 


Heap().heapsort([54, 56, 7777, 54, 40, 44, 13, 9, 7])