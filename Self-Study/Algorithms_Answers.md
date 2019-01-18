## Exercise I

```
a) If we look at the number of runs the while loop would have to through for values of n from 1 to 3, we see that at n = 1 it would loop through 1x before completing, at n = 2, it would loop through 2x, and at n = 3, it loops through 3x. This means it has a time complexity of O(n).

b) Each for loop on its own is O(n), therefore the aggregated time complexity of the 4 for loops (see what i did there) would be O(n^4)

c) The nature of this recursive function is such that the number of times it will run is equivalent to the bunnies integer that's input. This is because it decrements by one every time, until it reaches the base case of bunnies == 0. Therefore the time complexity is O(n).
```

## Exercise II

The optimal strategy would be to use a variation of the binary search technique. Drop an egg from the middle floor, if it breaks, then you know every floor above it would also result in breakage, so you eliminate the half above the _f_ you began at. If it doesn't break, you know that every floor below it won't result in breakage either, so eliminate those lower floors. Split the remaining floors in half, and drop it from the new middle of those floors. Continue to do this splitting and eliminating until you find your culprit _f_.