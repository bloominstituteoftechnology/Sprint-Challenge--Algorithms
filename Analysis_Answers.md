Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   - Heap insert: `O(log n)`
   - Heap delete: `O(log n)`
   - Heap get max: `O(1)`

   O(1) + O(n log n) + O(n^2) + O(1) = O(n^2) because O(n^2) dominates O(1) and O(n log n)

   ```python
   def heapsort(arr):
    heap = Heap()  # O(1)

    for i in arr:  # O(n) * O(log n) = O(n log n)
        heap.insert(i) # O(log n)

    sorted = []
    while len(heap.storage) > 0: # O(n) * O(n) = O(n^2)
        sorted.insert(0, heap.delete())
        # O(log n) + O(n) = O(n)
        # delete: O(log n)
        # py insert: O(n)

    return sorted # O(1)
   ```

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   - Yes because based on bigocheatsheet website, heapsort can run O(n log n) and I think for it to run O(n log n) is to use a helper method that runs O(n log n) and done it recursively then building the heap with a runtime of O(n) can lead to a total runtime of O(n log n)

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   The space complexity of my heapsort function is O(n) since I used a new list to populate it with the elements that's being sorted from the original list. If we need to make it O(1), we need to mutate the original list and sort the elements from there without needing a new list.
