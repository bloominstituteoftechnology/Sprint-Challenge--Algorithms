from math import floor

def heapsort(arr):
  pass

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    if not len(self.storage):
      return None
    if len(self.storage) == 1:
      return self.storage.pop()
    max_value = self.storage[0]
    self.storage[0] = self.storage.pop()
    self._sift_down(0)
    return max_value

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent_index = floor((index - 1) / 2) if index > 0 else 0
    if self.storage[parent_index] < self.storage[index]:
      self.storage[parent_index], self.storage[index] = self.storage[index], self.storage[parent_index]
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    left_index = index * 2 + 1
    right_index = index * 2 + 2
    max_child_index = len(self.storage) - 1 
    
    try:
      left_child = self.storage[left_index]
    except IndexError:
      left_child = None

    try:
      right_child = self.storage[right_index]
    except IndexError:
      right_child = None

    if left_child and right_child:
      max_child_index = left_index if left_child > right_child else right_index
    elif left_child:
      max_child_index = left_index
    elif right_child:
      max_child_index = right_child

    if self.storage[index] < self.storage[max_child_index]:
      self.storage[max_child_index], self.storage[index] = self.storage[index], self.storage[max_child_index]
      self._sift_down(max_child_index)