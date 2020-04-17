#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) a equals 0. While a is less than n times n times n, a will be equal to the value of a plus (n) times (n).
0(n) -> while loop runs 0(n), constant operation inside, making it 0(1), combined it becomes 0(n)


b) The sum is zero. For i in the range of n, j is equal to 1. While j is less than n, j is equal to j times 2. The sum of 1. 
O(n^2) -> The range of the function is as large as (n) but check again conditionally. This increases as a much faster rate.
For loop runs O(n) the inside while loop, checks in again and runs operation at O(n), because both checked (n) and need to be combined, O(n^2)


c) If bunnies is equal to 0, then the answer is 0.
Return the answer for 2 plus the number of bunnies minus 1. This is a linear.
O(n) -> the function runs 1 operation based on the number (n) bunnies, O(n)

## Exercise II

There are two ways we can look at this. Recrusively until we add a return statement to end it or as a merge sort. 

The first way we can implement this is if we drop the first egg on the first floor and if it doesn't break, we can move on to the next floor. Once on the next floor see if it breaks, else the floor it broke on recursively. This would be very long, especially if the egg is tough.

However, we can try a merge sort where we go to the middle of the floor, drop the egg, see if it breaks. If the egg breaks then everything to the higher floors means it will break, so we move down to the lower floors and drop the egg from that half way point onwards till it breaks.

mid = len(n) // 2:

go to a window on n // 2 floor, drop egg: if_broken = True: n[i:] = not_broken find floor between len(n[1:i]) // 2: repeat process is_broken = False: n[:i] = safe_floors

runtime -> log(n)


