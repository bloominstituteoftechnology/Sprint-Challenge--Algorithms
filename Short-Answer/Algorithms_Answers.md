#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  
```python

a = 0                       # O(1)
    while (a < n * n * n):  # O(3n) 
        a = a + n * n       # O(2)
                            # Total O(n)
```

b)
```python

    sum = 0             # O(1)
    for i in range(n):  # O(n)
        j = 1           # O(1)
        while j < n:    # O(n)
            j *= 2      # O(1)
            sum += 1    # O(1)
                        # Total O(n^2)
```
c)
```python

    def bunnyEars(bunnies):             
        if bunnies == 0:                # O(1)
            return 0                    # O(1)
        return 2 + bunnyEars(bunnies-1) # O(1)
                                        # Total O(1)
```
## Exercise II
```python

    currentFloor = 0                    # O(1)
    while (currentFloor < unsafeFloor): # O(n)
        eggs.throw(safely)              # O(1)
        currentFloor += 1               # O(1)
    return currentFloor                 # O(1)
                                        # Total O(n)
```