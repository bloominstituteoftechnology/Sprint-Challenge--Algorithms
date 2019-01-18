Add your answers to the Algorithms exercises here.
# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  O(n)
```
b)  O(n^3)
    sum = 0
    for (i = 0; i < n; i++)  O(n)
      for (j = i + 1; j < n; j++) O(n)*O(n)
        for (k = j + 1; k < n; k++) O(n)*O(n)*O(n)
          for (l = k + 1; l < 10 + k; l++) 
            sum++
```

```
c)  O(n) the recursion is acting like 1 for loop going from n down to 0.
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.
I would do a binary search starting at the 1/2 point and seeing if the egg broke or not.
  If it broke, I would go down to the floor that is 1/4 of the stories. 
  If it didn't break. I would go to the floor that is 3/4 of the stories
etc...
O(log n)
def binary_search_recursive(arr, target, low, high):
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