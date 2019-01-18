Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   if you take the two loops we have we get O(n log n) and O(n log n). The dominant of the two is O(n log n) so our heapsort function will have a time complexity of O(n log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   No. The big beta case for hepsort is O(n log n) so the algorithm is already running at the best case scenario

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   Since we are using up only n cells for the function and are not adding any new data, the space complexity would be O(n)