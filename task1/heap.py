def heapsort(arr):
    # Create heap object
    heap = Heap()

    # Loop through each element in arr
    for i in arr:
        # insert each element to heap.storage
        heap.insert(i)

    sorted = []
    # Loop through each element in heap.storage
    while len(heap.storage) > 0:
        # delete each element from heap.storage then
        # prepend each element to sorted
        sorted.insert(0, heap.delete())

    return sorted


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
                self.storage[index], self.storage[(index - 1) // 2] = (
                    self.storage[(index - 1) // 2],
                    self.storage[index],
                )
            index = (index - 1) // 2

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            mc = self._max_child(index)
            if self.storage[index] < self.storage[mc]:
                self.storage[index], self.storage[mc] = (
                    self.storage[mc],
                    self.storage[index],
                )
            index = mc

    def _max_child(self, index):
        if index * 2 + 2 > len(self.storage) - 1:
            return index * 2 + 1
        else:
            return (
                index * 2 + 1
                if self.storage[index * 2 + 1] > self.storage[index * 2 + 2]
                else index * 2 + 2
            )


print(heapsort([5, 3, 2, 1, 4]))

