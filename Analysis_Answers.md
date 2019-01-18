Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`
   
   

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
   
   
   
ANSWERS

1. O(n log n)

2. I think no, since the root of the tree needs to be rearranged everytime an index is deleted.

3. I would have to sort heap.storage and return that instead of creating a results array
to achieve O(1). Right now my implementation is O(n).