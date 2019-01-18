# def heapsort(arr):
#     heap = Heap()
#     final = []
#     for i in arr:
#         heap.insert(i)
#     i = 0

#     for i in range(heap.get_size()):
#         heap.delete(i)

#     # final = final[::-1]
#     return heap.storage


# class Heap:
#     def __init__(self):
#         self.storage = []

#     def insert(self, value):
#         self.storage.append(value)
#         self._bubble_up(len(self.storage) - 1)

#     def delete(self, index):
#         retval = self.storage[0]
#         print('first', retval)
#         print(self.storage)
#         print('----')
#         self.storage[0], self.storage[len(
#             self.storage) - index - 1] = self.storage[len(self.storage) - index - 1], self.storage[0]
#         print(index)
#         print(self.storage[len(self.storage)-index-1])
#         print(self.storage)
#         self._sift_down(0)
#         return retval

#     def get_max(self):
#         return self.storage[0]

#     def get_size(self):
#         return len(self.storage)

#     def _bubble_up(self, index):
#         while (index - 1) // 2 >= 0:
#             if self.storage[(index - 1) // 2] < self.storage[index]:
#                 self.storage[index], self.storage[(
#                     index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
#             index = (index - 1) // 2

#     def _sift_down(self, index):
#         while index * 2 + 1 <= len(self.storage) - 1 - index:
#             mc = self._max_child(index)
#             if self.storage[index] < self.storage[mc]:
#                 self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
#             index = mc

#     def _max_child(self, index):
#         if index * 2 + 2 > len(self.storage) - 1 - index:
#             return index * 2 + 1
#         else:
#             return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2


# print(heapsort([2, 6, 1, 7, 3, 4, 5]))

# First answer passes test
# def heapsort(arr):
#     heap = Heap()
#     final = []
#     for i in arr:
#         heap.insert(i)

#     while heap.get_size() > 0:
#         for i in range(heap.get_size()):
#             heap._sift_down(i)
#         final.insert(0, heap.delete())

#     return final

# Best run time
# def heapsort(arr):
#     heap = Heap()
#     final = []
#     for i in arr:
#         heap.insert(i)
#     i = 0
#     while heap.get_size() > 0:
#         heap._sift_down(i)
#         final.append(heap.delete())
#         i += 1

#     return final[::-1]

# Even less code


def heapsort(arr):
    heap = Heap()
    final = []
    for i in arr:
        heap.insert(i)

    while heap.get_size() > 0:
        final.append(heap.delete())

    # final = final[::-1]
    return final


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_down(len(self.storage) - 1)

    def delete(self):
        retval = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return retval

    def get_min(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_down(self, index):
        while (index - 1) // 2 >= 0:
            if self.storage[(index - 1) // 2] > self.storage[index]:
                self.storage[index], self.storage[(
                    index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
            index = (index - 1) // 2

    def _sift_down(self, index):
        while index * 2 + 1 <= len(self.storage) - 1:
            mc = self._min_child(index)
            if self.storage[index] > self.storage[mc]:
                self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
            index = mc

    def _min_child(self, index):
        if index * 2 + 2 > len(self.storage) - 1:
            return index * 2 + 1
        else:
            return index * 2 + 1 if self.storage[index * 2 + 1] < self.storage[index * 2 + 2] else index * 2 + 2


print(heapsort([2, 6, 1, 7, 3, 4, 5]))
