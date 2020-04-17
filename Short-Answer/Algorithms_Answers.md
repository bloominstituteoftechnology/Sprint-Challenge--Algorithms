## Exercise I

a)
### O(n)
Cancelling exponents shows that `n * n * n` (n^3) and `n * n` (n^2) simplify down to `n` (n^1) and `1` (n^0),
effectively making this a loop that runs only `n` times.

b)
### O(n*log(n))
The functions loops through `n` times, and runs the same code each time, doubling until it hits `n`.
How many times you need multiply a number by itself to get `n` is the `log[base](n)` function.
(i.e. `log[2](256) = 8` because you need to multiply 2 by itself 8 times to get 256. )

c)
### O(n)
Ignoring constants, this function recursively calls itself until hits 0, subtracting 1 from its value everytime, 
thus doing it `n` times.

## Exercise II

```py
def find_floor(lowest_floor, highest_floor):
    if lowest_floor < highest_floor:
        floor_to_check = (lowest_floor + highest_floor) // 2
        if ("egg doesn't crack"):
            return find_floor(floor_to_check+1, highest_floor)
        elif ("egg cracks"):
            return find_floor(lowest_floor, low, floor_to_check-1)
        else:
            return floor_to_check
```
This works very similar to a binary search. If you drop from a specific point, you can determine which section above or below you can filter out, based on if the egg breaks. Likewise, because of its similarity to a binary seach, it's big-O complexity is O(log(n)).
This is because similarly to Question B, you keep dividing by a constant until 0, the same as multiplying by a constant until it hits `n`.
