#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1), constant time

I would think that in the `while` statement on line 10, the `n` being squared would be constant time, since the calculation basically doesn't get more complex as `n` goes up. Same for line 11, since `n` is just being multiplied by itself, and increases in `n` would not cause increased instructions to execute in the algorithm.


b) O(n log n)

In the `for` statement on line 17, the length of the loop is determined by `n`, so line 17 is linear time. Line 19 has another loop based on `n`, but it's checking `n` against `j`, which gets multiplied by two each iteration of the loop, so I'd say that's `O(log n)`, so multiplied with line 17 would be `O(n log n)`.


c) O(1), constant time

There is no `n` anywhere in this function (as far as the compiler is concerned), so this would be constant time. As `n` goes higher, no change in this function.


## Exercise II


We have to pick a starting spot. I was assuming there would be one listed in the problem, but since there is not, we have to pick a reasonable number to start. Since we are talking about buildings with many floors, let's start at 50.

```
current = 50

highest_unbroken_floor = 0
lowest_broken_floor = -1


while (lowest_broken_floor - 1) != highest_unbroken_floor:

  Drop egg at current floor.

  If broken:
    lowest_broken_floor = current
    Too high, go lower (guess half)
    current = current // 2

  Else (not broken):
    highest_unbroken_floor = current
    Too low, go higher (guess twice)
    current = current * 2

f = lowest_broken_floor
```

Since we are guessing by halving or doubling each iteration, this would be `O(log n)`.
