#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) In the example given, the variable a is set equal to zero, then incremented by the value n^2 until a > n^3. Due to the exponential growth differences between n^2 and n^3, the larger that n is, the more iterations it will take for the value of a to reach its goal and for the algorithm to complete. This exponential difference makes the runtime complexity of the algorithm O(n), or linear.


b) In the second example, the outer loop repeats for the length of the input, n. This basic loop structure suggests a linear component to the runtime complexity. The inner loop features a variable that doubles every iteration, and this is repeated until the variable reaches at least equality with the input, n. This is a logarithmic component to the complexity. In summary, the overal runtime complexity is O(n*log(n)). 


c) In the final example, a non-zero input amount of bunnies results in two being added to the final sum at the same time as the function is being recursively called with n - 1 bunnies as the input. In essence the function is adding two for every bunny, which makes the runtime complexity O(n). The number of iterations required is directly tied to the runtime. An increase of one in the input results in an additional iteration required to count all of the bunny ears. 

## Exercise II

Alongside the primary goal of searching for the minimum floor at which an egg dropped does not break, the proposed algorithm is attempting to optimize for the number of eggs dropped required to find this minimum. Given the task is searching, I proposed the implementation of a binary search algorithm in order to solve the problem. Binary search will minimize the number of comparisions, and therefore the number of eggs dropped. In this case the runtime complexity would be O(log n) at worst.  

```python
def floor_search(n_floors, lower, upper):
    # n_floors is the array or set of floors to be tested
    # Original set is full building
    # lower is bottom potential target floor, upper is top potential target floor
    lower = n_floors[0]
    upper = n_floors[-1]
    # Start at middle floor of building with dropping
    midfloor = (lower + upper) // 2

    # Drop egg at midpoint and record result
    # Egg doesn't break
    if n_floors[midfloor] == egg_not_broken:
        # Recursively search floors above
        return floor_search(n_floors, midfloor + 1, upper)
    else:
        # Egg does break
        if lower == upper:
            # Check floor below for no break
            # Check floor above for break
            return target floor
        else:
            # Recursively search floors below
            return floor_search(n_floors, lower, midfloor - 1)
```
