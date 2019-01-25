def heapsort(arr):
    newArr = []
    newHeap = Heap()

    for item in arr:
        newHeap.insert(item)

    for x in range(newHeap.get_size()):
        j = newHeap.delete()
        newArr.insert(0, j)

    print(newArr)
    return newArr


class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.size += 1
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self.size -= 1
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
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
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


heapsort([1, 2, 3])

heapsort([2, 1, 6, 4])
