Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`
   
   
> I believe the Big-O runtime of my `heapsort` function is `O(n^2)` as it divides the heap into sublists until each sublist is sorted, but this requires it to loop over many sublists (dependent on size). Upon further looking, this isn't a `heapsort` but some other kind of sort, similar to `quicksort`.

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   
> I could make it run in better time by implementing the correct `heapsort`. It currently makes too many iterations and sublists, recursion is not required and only makes it more difficult.

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?
> I believe the space complexity is `O(n)` as it creates a new sublist for each number until all of the sublists are sorted. These sublists never get larger than n, but at the max the sublists will likely be close to the length of n.