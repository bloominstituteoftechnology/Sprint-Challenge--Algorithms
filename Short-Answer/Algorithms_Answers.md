#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n)

b)O(N^2)

c) O(2^N)

## Exercise II

I would use a binary search approach.

1. I would find the highest and lowest floors and make my first try from the middle. So if I had floor 1 - 100, I would drop an egg off of floor 50.
2. If the egg breaks, then I would find the floor between 49 and 0, so 25.
3. I would continue this process until I found the floor at which the egg didn't break. Then I could rule out all the floors above that floor and all those below.

The big O notation of this would be O(log\*n) because we know that we are basically halving our the number of floors that we have to test.
