Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   O(n log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   I don't think it's possible since you need recursion to make it this fast. Otherwise you would probably need to use multiple loops.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   O(n) since the class is increasing in size as we go through the for loop. To get to O(1) we would have to somehow get the array into the heap
   passed in as a parameter.

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?