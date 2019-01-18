Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   - Heap insert: `O(log n)`
   - Heap delete: `O(log n)`
   - Heap get max: `O(1)`

<!-- O(n log n^2). -->

O(n^2)
Within the second while loop, O(n), I have insert(), which is O(log n) wrapping delete(), which is O(log n). That brings the function to O(n^2), and it's the most dominant in the function.

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

Yes. Instead of insert() we could use append then reverse the arr.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

Since we are adding numbers to the sorted list, the more numbers we have in the arr, the more we need to append. Therefor the space complexity would be O(n).
To achieve O(1) we would probably need to make changes directly in arr instead of making a sorted list.
