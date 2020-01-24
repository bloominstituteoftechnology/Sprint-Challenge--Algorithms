#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime of this code snippet is O(n)

Reasoning:
```python
a = 0

while (a < n * n * n): # Here in the while loop, n * n * n gives us a runtime of O(n^3) 

    a = a + n * n # And inside, this n * n adds O(n^2) to each iteration

# we can calculate the total runtime by simply dividing the runtime of the while loop (n^3) by the runtime of the inner (n^2) which gives us O(n) 
```


b) The runtime of this code snippet is O(n log n)

Reasoning:
```python
sum = 0

for i in range(n): # our outer loop runs n times

    j = 1

    while j < n: # is not happening in linear time, but rather O(log n), because
        j *= 2 # here the value of j is doubling each iteration
        sum += 1

# We can calculate the total runtime of the nested loops by simply multiplying their runtimes 
# O(n * (log n)) = O(n log n)
```


c) The runtime of this code snippet is O(n)

Reasoning:
```python
def bunnyEars(bunnies): # Assuming that bunnies is an int (base case check against 0),
                        # then this recursive algorithm will always execute "bunnies" number 
                        # of times (linear time). 
    
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1) # recursive call decrements "bunnies" or n by 1 (linear time)
```

## Exercise II


