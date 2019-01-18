Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   I used heap insert + heap delete + and the builtin reverse which is O(n)
   meaning my heap sort probably has a runtime of O(n log (n)^2)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   Yes it could be better I am sure. One would have to insert the delete result directly into the last
   slot of the array. This would eliminate the need for the last list traversal.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   The size complexity is O(n) because we have copied the data. One in the heap and the other in the result arr.

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   We would have to sort the array as a heap in place. BY doing this way we wouldn't have to create copy of the data. We would have to change the insert method of the Heap class to rearrange the array as a heap instead of creating one.