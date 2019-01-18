Add your answers to the questions below.

### 1. What is the runtime complexity of your `heapsort` function? (If you used any

Python built-in functions, you can find their time complexities here:
https://wiki.python.org/moin/TimeComplexity )

Other hints, to save you some searching:

- Heap insert: `O(log n)`
- Heap delete: `O(log n)`
- Heap get max: `O(1)`

```
def heapsort(arr):
  result = []                           # O(1)

  for i in arr:                         # O(n)
    my_heap.insert(i)                   # O(log n)

  for i in arr:                         # O(n)
    biggest = my_heap.delete()          # O(log n)
    result = [biggest] + result         # O(1)

  return result                         # O(1)
```

#### Answer:

In the heapsort function `O(n)` is the dominant operation that adds to the scaling
complexity. There are 2 `O(n)` operations that have a `O(log n)` operation nested,
leading to a final Big O rating of `O(n log n)`

---

### 2. Could one make your algorithm run in better time? If so, how? If not, why not?

#### Answer:

The `heapsort` function needs to pass over the length of the array once, to place
each item in the `Heap`. It then needs to pull out each item it put in one by one
using the provided method. I thought about combining these to one loop, but the
heap needs to have all the items, before they are sorted. To my knowledge the only
thing I could do to make the algorithm run better would be to reduce the run time
of the methods in the `Heap` class.

---

### 3. What is the space complexity of your `heapsort` function? Recall that your

implementation should return a new array with the sorted data. (Also remember
that the size of the input array passed to the `heapsort()` function does
_not_ contribute to the size complexity.)

Most online sources say that the space complexity of heapsort is `O(1)`. What
would we have to change in our code to get there?

#### Answer:

Since the incoming array does not add to the space complexity of `heapsort` and
the space of the `Heap` class itself is `O(1)`. Then `O(n)` for the new sorted array
we use for the return value would be dominant since `O(1)` is neglegable in comparison.

Final answer `O(n)` for space complexity scaling in it's current state.

```
def heapsort(arr):
  result = []

  for i in arr:
    my_heap.insert(i)

  for i in arr:
    biggest = my_heap.delete()
    result = [biggest] + result

  return result
```

After seeing that O(1) is possible with `heapsort` I could probably refactor it, so that
as I add an item to the heap, it is removed from the origional array. Then when I get the
results back, add them to the now empty origional array. Think I will go do that now.

#### UPDATE:

Refactored `heapsort` to not use an additional array

```
def heapsort(arr):
  # result = []
  length = len(arr)

  for i in range(0, length -1):
    my_heap.insert(arr.pop())

  for i in range(0, length -1):
    biggest = my_heap.delete()
    arr = [biggest] + arr

  return arr
```

---
