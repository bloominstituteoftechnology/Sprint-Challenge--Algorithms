Add your answers to the questions below.

1. What is the runtime complexity of your `heapsort` function? (If you used any
   Python built-in functions, you can find their time complexities here:
   https://wiki.python.org/moin/TimeComplexity )

   Other hints, to save you some searching:

   * Heap insert: `O(log n)`
   * Heap delete: `O(log n)`
   * Heap get max: `O(1)`

   Answer:
   So, I think that the time complexity is O(n log n)

   I came to this conclusion following this breakdown:

   ```
    sorted = [] O(1)
  
    heap = Heap() O(1)
    for i in arr: O(n)
      heap.insert(i) O(log n)

    for i in range(0, heap.get_size()): O(n) + O(1)
      sorted = [heap.delete()] + sorted O(log n)

    return sorted O(1)

   ```

   Therefore, if we total it all up: 
   O(1) + O(1) + (O(n) * O(log n)) + ((O(n) + O(1)) * O(log n)) + O(1)...
   O(3) + O(n log n) + O(n log n) + O(log n)...
   O(n log n)

   Time Complexity: O(n log n)

2. Could one make your algorithm run in better time? If so, how? If not, why
   not?

   Answer:
   I honestly don't know. Maybe if, instead of making a Heap class every time, 
   I had the heap and needed functions integrated into the function. Besides
   that, I'm really not sure if I could. 

   I say that because I believe that I have the minimum number of nested
   iterations necessary to complete this. Definitely want feedback here!

3. What is the space complexity of your `heapsort` function? Recall that your
   implementation should return a new array with the sorted data. (Also remember
   that the size of the input array passed to the `heapsort()` function does
   _not_ contribute to the size complexity.)

   Most online sources say that the space complexity of heapsort is `O(1)`. What
   would we have to change in our code to get there?

   Answer:
   I think that the space complexity is currently O(N) because we are creating a
   new list each time, AND a Heap object in addition to the list being passed in, 
   and the space taken by those structure is relative to the size of the original 
   list passed in.

   In order for our heapsort to be O(1), we'd need to sort the list in place
   somehow. So we'd have to be able to represent a heap as a list and then modify our
   heap functions so that they work on the list instead of our Heap class object.

## STRETCH:
  1. My heapsort didn't break, actually. Though it did sort everything in reverse!
     To fix that, I just swapped the sorted list and the concatenated item when
     I build up the sorted list.
  2. I don't think that the time complexity changed. I changed very little to
     accomplish this and nothing that should have created a limiting increase
     in time complexity.
  3. After running tests of the two, they appear to be neck and neck. Here are some
     results:

    items , time (seconds)
    100   , 0.0000000000
    100   , 0.0000000000
    1000  , 0.0109984875
    1000  , 0.0109441280
    10000 , 0.2683062553
    10000 , 0.2642953396
    20000 , 0.8696694374
    20000 , 0.8736567497
    30000 , 1.8859679699
    30000 , 1.8739492893

    100   , 0.0009968281
    100   , 0.0010032654
    1000  , 0.0109658241
    1000  , 0.0119938850
    10000 , 0.2672986984
    10000 , 0.2692778111
    20000 , 0.8736319542
    20000 , 0.8806369305
    30000 , 1.8889625072
    30000 , 1.8689625263
