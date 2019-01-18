Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

    Other hints, to save you some searching:

    - Heap insert: `O(log n)`
    - Heap delete: `O(log n)`
    - Heap get max: `O(1)`

-- My time complexity for my function is O(n^2 log n). This is because I have a while loop (O(n)) and inside of it I have a insert(O(n)) wrapping a heap.delete(O(log n)). So all together they are O(n^2 log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?
   -- Yes I could. I could replace insert with append and then at the end of the function I could do a reverse. But I would still have (n^2 log n). I would have to get rid of the for loop inside of the whie loop and have an i increment every time the while loop looped. This would then give me a O(n log n).

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

    Most online sources say that the space complexity of heapsort is `O(1)`. What
    would we have to change in our code to get there?

--I would say that our space complexity is O(n). This is because we are appending a number into a new list to return at the end. If we wanted O(1), we would need to have to return the storage in the heap class and that be in the correct order. This might be possible if we would flip the max number to the end of the storage and then tell the size to not look at the last so many digits of the array.
