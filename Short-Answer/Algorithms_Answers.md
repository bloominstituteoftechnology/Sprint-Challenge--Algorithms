#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) **_The runtime of this function is O(n)_**. This function is dependent upon the input value of n, but it does not require nested loops and performs a single operation using the values of _a_ and _n_.

```python
a)  a = 0
    # this loop is O(n)
    while (a < n * n * n):
      # this portion is O(1)
      a = a + n * n
```

This function could be understood as _O(n + 1)_, but we drop the less consequential constants (**the 1**) and focus on the larger, more complicated runtime.

b) **_The runtime of this function is O(n log n)_**. This is due to the nature of a loop nested inside another loop.

```python
b)  sum = 0
    # this loop is O(n)
    for i in range(n):
      j = 1
      # this loop is also O(n)
      while j < n:
        # this is O(1)
        j *= 2

        # this is O(1)
        sum += 1
```

The first loop sets up the outer bounds for the second loop. The second loop will run a complete execution for every iteration **i** in range(n). **j** will continue to grow with each iteration of the inner loop until the value of j is greater than the value of n. At that point, the first loop will iterate to the next value and the cycle repeats. The reason this is O(n log n) is that we have an O(n) loop (for i in range(n)) which sets up the outer bounds of the function, but our inner loop is not going to be iterated the same number of times as the outer loop because we're not comparing items one to one. Rather, the outer loop provides a maximum value that **j** cannot go beyond. When **j** goes beyond that value, it triggers the loop to reset and the sum counter to be incremented. This means that because we're multiplying **j \*= 2** with each run of the loop, we're never going to be doing the same amount of linear work in both loops.

c) **_The runtime of this function is O(n)_**. This recursive function will be called from within the function as many times as the value we pass into the function as an argument.

```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

The approach I would choose for this problem would be to divide the total number of floors in half and start by asking if an egg dropped from the middle floor would break or not.

```python
start = 0
end = len(n)
middle = (start + end) // 2
```

If an egg dropped from the middle of the building breaks, we know that we're still too high and need to reduce the height of our _middle_ value. We can remove all of the floors above our middle value as possible candidates for a non-breaking floor because we know we're still breaking eggs at our current height and it won't get any better.

```python
start = 0
end = middle - 1
middle = (start + end) // 2
```

If an egg dropped from the middle of the building survives, we know that we can maybe go higher.

```python
start = middle + 1
end = len(f)
middle = (start + end) // 2
```

We repeat the process of narrowing down the floor range until we find the floors where a) an egg will break and b) the egg will not break.

We then return the value of the floor where the eggs will not break.

This function runs in an **O(log n)** runtime because while the number of executions does increase with respect to the value of **n**, it does so at a reduced rate because we're reducing the **total** amount of work required for completion with every subsequent execution.
