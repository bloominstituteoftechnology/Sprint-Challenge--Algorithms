#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Constant time


b) O(n log n) - Linearithmic time


c) O(n) - Constant time

## Exercise II

Go to the middle floor of the building by dividing `n` by two:
  drop the egg from current floor:
    if the egg does not break
        go halfway up the building (by adding current floor to total floors (n) and dividing sum by two)
        repeat step 2
    if the egg does break
      go up one floor
        drop the egg from current floor
          if the egg breaks
            return current floor minus one as `f`
          if the egg does not break
            go to step 3

O(log n) - Logarithmic time
