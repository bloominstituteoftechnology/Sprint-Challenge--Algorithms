#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```
a) The running time is O(n) because when you consider how many times the loop will run as n increases, it will run n times. This is because each iteration it adds n**2 to a. n**3 / n**2 is n. 
```

```
b) This case is more complex because there are two different loops running. The outer loop will run n times since it is incrementing by 1 each iteration up to the end of range n.  The inner loop is doubling the value of j every iteration, which is not linear. It can be prescribed the label O(log(n)). Since the loops are nested, to get the running time its necessary to perform multiplication on the two. Runtime is O(n log(n)).
```

```
c) This runtime is O(n) because the bunnies variable is being subtracted from one at a time until the base case is met. 
```

## Exercise II

```
Using basic logic we can assume that the egg will be less likely to break at lower floors so we will start at floor 1 and go up, throwing eggs down, in a linear fashion until finding "f". Complexity is O(n). 
```

