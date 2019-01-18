def heapsort(arr):
    result = []                 # O(1)
    heap = Heap()               # O(1)

    # O(n log n)
    for x in arr:
        heap.insert(x)

    # O(n^2) largest
    while heap.get_size() > 0:  # O(n)
        v = heap.delete()
        result.insert(0, v)

    print(result)
    return result


class Heap:
    def __init__(self):
        # Initializes an empty array
        self.storage = []

    def insert(self, value):
        # Adds inserted value to self.storage
        self.storage.append(value)
        # Runs method _bubble_up on the length of self.storage - 1
        self._bubble_up(len(self.storage) - 1)
    # Makes a new variable

    def delete(self):
        # ratval is assigned the first item in self.storage
        retval = self.storage[0]
        # the first item in storage is assigned self.storage index of the lengs of self.storage - 1
        self.storage[0] = self.storage[len(self.storage) - 1]
        # Removes the last item of self.storage
        self.storage.pop()
        #
        self._sift_down(0)
        return retval

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # Checks if the input index (minus 1) floor divided by 2 is greater than or equal to 0
        while (index - 1) // 2 >= 0:
            # Conditional to check if self.storage at the index -1 floor divided by 2 is less than self.storage at index
            if self.storage[(index - 1) // 2] < self.storage[index]:
                # Deconstruction assignment of self.storage at index and self.storage  at index - 1 floor divided by 2, swapping the positions of each
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
            # Assigns index the index - 1 floor divided by 2
            index = (index - 1) // 2

    def _sift_down(self, index):
        # While index times (2 + 1) is less than or equal to the length of self.storage minus 1
        while index * 2 + 1 <= len(self.storage) - 1:
            # mc is equal to self._max_child(index)
            mc = self._max_child(index)
            if self.storage[index] < self.storage[mc]:
                self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
            index = mc

    def _max_child(self, index):
        # Conditional to check if index times 2 plus 2 is greater than the length of self.storage minus 1
        if index * 2 + 2 > len(self.storage) - 1:
            # Returns index times 2 plus 1
            return index * 2 + 1
        else:
            # returns index times 2 plus 1 if self.storage at the index of index times 2 plus 1 is greater than
            # self.storage at the index of index times 2 plus 2 else, index times 2 plus 2
            return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2
