# Exercise I

## Part a)
O(n) / linear - the bound is cubic, but the rate of growth is quadratic.

## Part b)
O(log(n)) / logarithmic (assuming integers not floats) - `i` is cut in half each
iteration, and the comparison to `x` is irrelevant.

## Part c)
O(sqrt(n)) - a somewhat unusual but still distinct complexity, determined fully
by the outer loop. The two inner loops are both always length 8 so are dropped.

## Part d)
O(n*log(n)) / log-linear (or "linearithmic") - the outer loop is logarithmic,
the inner is linear, and the total complexity is just their product.

## Part e)
O(n^3) / cubic - the outer loop is linear, the next two nested loops are both
linear (in the worst/general case), and the innermost is just constant (9).

## Part f)
O(n) / linear - essentially equivalent to a simple for loop but recursive.

## Part g)
O(n) / linear - it can return early, but worst/general case is linear.


# Exercise II

## Part a)
The naive (quadratic) approach would be a nested for loop, over `i` and `j`,
that compares all possible combinations and remembers the one with the biggest
difference.

The correct/efficient (linear) approach is to loop over the array once tracking
the minimum value and maximum difference in the same pass.

Pseudocode:
```
minVal = a[0]
maxDiff = 0
for i in 1...n:
    minVal = min(minVal, a[i])
    maxDiff = max(maxDiff, a[i] - minVal)
return maxDiff
```

## Part b)
This is a conceptual question, and can be answered in a number of ways - the key
insight is that you should essentially implement a binary search. Start by
dropping an egg from the middle floor - if it breaks, go to the midway point
between where you are and the bottom. If it doesn't, go to the midway point
between where you are and the top. Either way, continue until you've narrowed
on the specific lowest floor that causes it to break, and that is `f`.


# Exercise III

## Part a)
The runtime will be O(n^2) / quadratic - there will be a linear number of passes
on possible pivots, and each pivot will be compared with (on average) a linear
number of other elements.

## Part b)
The runtime will be O(n*log(n)) / log-linear - there will be a logarithmic
number of pivots, and on average a linear number of comparisons for each pivot.

Note that practical implementations of Quicksort often use randomization - that
is, pivots are chosen at random. The result (though it requires a bit of
statistics to prove) is, on average, O(n*log(n)) performance - and the
probability of the quadratic worst case is vanishingly small.

            
