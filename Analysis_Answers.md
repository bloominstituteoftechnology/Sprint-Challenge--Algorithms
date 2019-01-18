Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

The heapsort code involves an O(n) while loop and the O(log n) heap.delete() inside of the append function, giving a total time complexity of O(n^2 log n).

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

I believe so. I feel like there might be a way to do this without sifting down or using the i increment, solutions I'll take a look at a bit later. Without those pieces of code all we would really need to do is call insert() and delete() to get proper heap organization, which should bring the time complexity to O(n log n). I might be wrong about the possibility of this solution but this does seem like it can be further optimized.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

The space complexity here is unfortunately not O(1) yet. It seems to be O(n), given that I created a new list (result) and appended information to that rather than work with the existing storage. It's not the most efficient solution yet but given the spirit of this week I wanted to get a basic version down on paper in order to solve the problem before worrying about optimization.

Addendum to question 3: I've now implemented what appears to be a solution with O(1) space complexity. My hunch from before was correct in that I was able to get test_heap.py to pass using only the insert() and delete() functions while working with the new heap and the original array, completely bypassing my previous step of creating the "result" list and using that to store values.