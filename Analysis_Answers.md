Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   Runtime complexity of my function is O(n log n). The for loop has an n runtime and within that, I use a method with an O(log n) runtime. The while loop is the same. The reverse method has an O(n) runtime. Totaling it up and getting rid of constants, the function is O(n log n).

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   I don't think so, there isn't anything being done in the function that isn't completely necessary to get it sorted and I don't see another quicker way to implement Heapsort.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   I believe the complexity of my function is O(N) since we're creating a new list equal in size to the given one. We could sort in place by swapping the nums to a certain place within the list based on whether or not they're equal to the current result of "get_max" and achieve O(1).