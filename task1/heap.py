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


def heapsort(arr):
    if not len(arr):
        return []

    returned = []
    new_list = Heap()
    #  Creates new Heap.storage with all values from arr
    for i in range(len(arr)):
        new_list.insert(arr[i])
    #  Goes through new_list.storage, finds the max and appends it to returned array
    #  Finally the element that was passed to returned gets deleted
    #  continues this process until whole storage is gone
    for j in range(new_list.get_size()):
        returned.append(new_list.get_max())
        new_list.delete()
    #  reverses returned array so it is in ascending order
    return list(reversed(returned))


print(heapsort([4, 3, 2, 5, 44, 12]))