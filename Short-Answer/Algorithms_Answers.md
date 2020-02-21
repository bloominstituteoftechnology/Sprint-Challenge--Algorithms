#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `O(n^3)`
    Because while the while loop is (`a` is less than `n^3`), the runtime scales by `n` cubed

b) **?** `O(2^n)`
    What is happening here is `j` is being multiplied by 2 `n` number of times so the runtime is `O(2^n)`

c) `O(n + 1)`
    The function will run as many times as there are `bunnies` passed into it (plus one for the 0 `bunnies` base case)

## Exercise II

Divide the number of floors `n` by half (minus 1 if odd) and drop 1 egg. If it breaks, the floor is either too high or floor `f`, divide the bottom half of floors by 2 and drop again. If it doesn't break, it's too low, divide the top half by 2 and try again off the center floor. This method is a binary search algorithm and I believe should yield the most efficient results.

Example:

    n = 20. high 20, low 1

    20/2 = 10th floor
    drop egg off 10th floor = it breaks. Too high, need lower floor. high 10, low 1

    10/2 = 5th floor
    drop egg off 5th floor = doesn't break, too low. high 10, low 5

    10-((10-5)/2) = 7.5;; halfway 7.5, round down to 7. 

    drop egg of 7th floor, it breaks, too high. low 5, high 7

    halfway between 5 and 7 is floor 6

    drop egg - it breaks.

    Since egg did not break on floor 5, we know floor `f` is 6

The runtime is `O(log n)` since the total number of tests halves every run until we reach the base case 1