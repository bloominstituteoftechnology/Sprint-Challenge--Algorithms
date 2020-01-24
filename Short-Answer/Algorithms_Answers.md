#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n), because we are in a loop that will run a variable amount of times, increasing the amount of times directly compared to the value of n

b)
    O(n log n), because the first loop is O(n), and the nested loop runs proportionally less the higher n becomes, which would be O(log n).
    O(n) * O(log n) == O(n log n)

c)
    O(n), each recursion only increases the number of operations by 1. so the higher the number, the more operations

## Exercise II

get midway_point = n // 2

You can test to see if egg would break at the midway_point.

and if the egg breaks, then take the lower 1/2 of the array, & find the midway point & repeat

then if the egg doesn't break, you can take the upper 1/2 of the array, & find the midway point & repeat.

& then repeat the process until you move in one direction at one spot. If the egg breaks, & you move one spot down & the egg doesn't break.. The previous spot is 'f'.

if the egg does not break & you move up one & it does break, that last spot is your 'f'

Since we are halving every time, the runtime complexity would be O(log n)

n would represent the amount of floors
