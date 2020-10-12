#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```
a)  a = 0
    while (a < n * n * n): # O(n)
      a = a + n * n
```
The runtime for this while loop is O(n). This is because this loop's running is based on the value of n each time.



```
b)  sum = 0
    for i in range(n): # O(n) range of n
      j = 1
      while j < n: # O(log n ) the loop variable is increased exponentially by a constant amount
        j *= 2
        sum += 1
```
The inside loop doubles until j is eqaul to n, therefore the runtime complexity is O(log n. The for loop is O(n). Since these are nested loops we multiply the time complexities:
O(n * log n) == O(n log n). The runtime complexity of this is O(n log n).



```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1) # O(n) recursion is normally linear time
```

Because this is a recursive this is a recursive function. You have to call bunnyEars(bunnies-1) every time bunny ears changes value.

## Exercise II

1. Find the middle of the n-stories (len(n-story)//2.)
2. If the eggs break then we know that it is in the range of f(f floors or higher). This means that we can eliminate any floors above this middle. Then we would go incremently down f-1 till we do not break any eggs.
3. Or if the eggs do not break from the middle floors we can incremently add mid + 1 till we get to the floor where the eggs break. In this case we know that any floors less than n is safe and we can eliminate these lower floors.

This is similar to a binary search tree. As we go down the left side, we know the numbers are going down and we have the ability to eliminate floors above the middle or below the middle if the eggs do(n't) break. The runtime of this solution would be O(log n)


