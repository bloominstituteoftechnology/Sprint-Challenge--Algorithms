Exercise 1:
- a. In terms of growth, the right-hand value `n * n * n` grows at a rate of 
     `n^3` whereas `a` grows at a rate of `n^2`. Comparatively, the former term 
      will grow much faster than the latter term for large values of `n`. Hence 
      this function has time compleixty `O(n^1)`, which the possibility of not
      terminating for substantially large values of `n`.

- b. This function has 4 inner loops. The outer-most loop runs at most `n` times,
     the second loop runs `n-m` times, the third runs `n-(m+k)`, the fourth runs
     `k-((m+k)+j)`. Simply, each loops runs `O(n)`. Conjointly, this makes for
     a total time complexity of `O(n^4)`

- c. This function has time complexity `O(n)`. Given `n` bunnies it'll recursively
     decrement the amount of bunnies until the number is 0.

Exercise 2:

Given an `n` story building, where we want to know the bottom-most floor 
from which we can toss an egg and have it break. We can utilize the following
strategy: Firstly, we can go to the middle floor of the building and drop
an egg. If we observe that the egg broke, we know either we're too high or
we're on the bottom most floor that allows for egg-cracking. We can't, however,
know that later bit of information without checking. To check, we can go to the
floor midway between the current floor and the bottom-most floor of the building
and drop another egg. If we observe that it didn't break, we know that we're too
low, and can next go to the floor midway between the current floor and the previous
floor to repeat the check. By repeating this pattern of bisecting the remaining floors 
above or below the current floor, you can binary search for the minimum floor from which 
an egg can be dropped and broken. Eventually, this processes converges to a single
value, in this case the bottom-most floor from which a dropped egg can break.

The runtime of this algorithm is: 
  - Best case, where the building consists of one floor: `O(1)`
  - Average case, the building consists of some `n` floors, and hence
    will need to be bisected `m` times to reach converge on a value. 
    Algebraically, the repeated halving `(((n/2)/2) ... /2\_m)` is 
    equivalent to `n/(2\*\*m)`. Giving a complexity of `O(n/2\*\*m)`
    isn't standard format, hence we can rewrite the expression as
    `n*(1/2\*\*m)` which can become `log(n) + log(1) - log(2\*\*m)`
    which goes to `log(n) - m*log(2)` and finally `log(n) - m`.
    In BigO this simplifies to `O(log(n))
  - No time for worst case :(

```
def min_floor(n):
  top = n
  middle = top/2
  bottom = 0

  while top != middle and middle != bottom:
    goto_floor(middle)
    did_break = drop_egg()

    if did_break:
      top = middle
      middle = middle/2
    else:
       middle = middle+((top-middle)/2)
       bottom = middle

  return middle
```
