class Heap:
    def __init__(self):
        self.storage = []
        
    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        retval = self.storage[0]  # largest number
        self.storage[0] = self.storage[len(self.storage) - 1]  # replaces storage[0] with storage[-1]
        self.storage.pop()  # pops last value (no more storage[0])
        self._sift_down(0)
        return retval  # returns storage[0] BEFORE deletion

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


def heapsort(l):
    heap = Heap()  # O(1)
    result = []  # O(1)
    # O(n)
    for n in l:
        # O(log n)
        heap.insert(n)  # converts list into heap
    # O(n)
    while heap.get_size() > 0:
        # append: O(1) + delete: O(log n)
        result.append(heap.delete())  # appends laragest number onto results and deletes it from heap
    # O(n)
    result.reverse()
    return result  # returns reversed result

# ( O(n) * O(log n) ) + ( O(n) * O(log n) )
# combine children
# O(n log n) + O(n log n)
# comparesiblings
# O(n log n)
