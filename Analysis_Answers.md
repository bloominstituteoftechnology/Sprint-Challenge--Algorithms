Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

I have a nested for loop so I am sure it is super slow to scale

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

This is basically my first pass solution, so it has some refactoring it needs to have done to it.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

O(n**2)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

I would need to remove at least one of the for loops.