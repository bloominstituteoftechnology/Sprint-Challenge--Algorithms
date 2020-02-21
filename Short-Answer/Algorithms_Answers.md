#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n): it will take n steps for the loop to iterate
from 0 to n^3, incrementing by n^2 each time, since
n^3 = n^2 * n.

b)

I think this is O(n log n), since the outer loop will run n times, but the inner loop log n times (value doubles with each iteration).


c)

I think this is O(n), since this algorithm will count down from n to 0.

## Exercise II

 - Max = n
 - Min = 0
 - Repeat these steps until we find f:
    - Set middle to the max floor // 2
    - Go to floor number {middle} and drop an egg off
    - If it does not break:
        - Go to the floor one higher and drop an egg. If it does break:
            -We found f. Return this floor number
            -Otherwise, our current floor is too low. Set min
            to our current floor
    - If the egg breaks, our current floor is too high. Set
    max to our current floor

This will have runtime complexity of O(log2 n), where n is the number of floors, since we are halving the problem space each time. Since we are checking the floor above each time this should mean double the guesses of a normal binary search which would be O((log2 n) * 2), but I believe we drop the constants.