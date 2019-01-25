Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`


My heapsort function comes out to O (N) * O (N log N) which is equal to O (2N log N) dropping the constant makes it O (N log N)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   I don't think it can be run in a better time complexity but space complexity can be improved, unless sorting min_heapsort runs in faster time complexity.


3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   My heapsorts space complexity is currently o (n) because I append the deleted values to a sorted_array that 
    starts off empty. I could have not used a sorted_array and instead tried to resort the heap everytime I got the max value
    Instead of making a copy of the array to return a sorted_array since I already have the array in memory I could have used that as a reference and made it 0 (1) so it doesn't need to allocate more memory and instead uses the array that gets heapified. 