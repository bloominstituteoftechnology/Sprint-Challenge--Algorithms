#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(1)

b) O(n)

c) O(c^n)

## Exercise II

I would try to use a binary search that would result in a runtime complexity of O(log(n)). I would need to sort the array of floors and test whether the egg will break if dropped in the middle of the floor. If it passes the test, I would run the same test again on all the lower floors recursively until I found the floor. If the egg did not break, I would run the test on all the upper floors.
