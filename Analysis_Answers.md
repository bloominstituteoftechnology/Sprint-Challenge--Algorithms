Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

my algorithm runs O(n^2 log n) with my for loop O(n) and inside if have an insert O(log n)  which has delete O(log n) inside of it. 

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
possibly, if I got rid of the insert function and replaced it with an append then just reverse at the end of the function. Then I would maybe be able to get rid of one for loop and just increment i through the index arr every time the main loop iterated. I would end with O(n log n)

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?


   The space complexity is O(n). We are appending a number into a new list, so we have to iterate through all the n's in the list. To get O(1), we would need the storage in Heap class to be retrned - and in the correct order. If we put the max number at the end of the storage then make the size not look at all the indices of the array. 