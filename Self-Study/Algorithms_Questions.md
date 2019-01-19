# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0                     0(n)
    while (a < n * n * n) 
      a = a + n * n
```

```
b)  sum = 0   O(n^4)
    for (i = 0; i < n; i++)
      for (j = i + 1; j < n; j++)
        for (k = j + 1; k < n; k++)
          for (l = k + 1; l < 10 + k; l++)
            sum++
```

```
c)  bunnyEars = function(bunnies) {  O(n)
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

O(log n)

def binary_search_recursive(arr, target, low, high): O(log n)
  if len(arr) == 0:
    return -1
  middle = int((low+high)/2)
  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  if target == arr[middle]:
    return middle
  elif target < arr[middle]:
    return binary_search_recursive(arr[:middle], target, 0, middle)
  else:
    return binary_search_recursive(arr[middle:], target, 0, middle+1)