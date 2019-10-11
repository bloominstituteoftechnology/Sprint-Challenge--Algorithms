#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This snipet initially looks like a O(n**3) runtime, but because the a value inializes at a value of n * n and then increments by n * n for each iteration of the while loop, it is actually O(n) runtime because it is basically n * n * n == n * (n * n) or n * a == n * a.

```python
    a = 0
    while (a < n * n * n):
      a = a + n * n
```


b) This bad boy is O(n log n) because we have the for loop (n) then a while j < n, this while loop will not equal n because j increments exponentially, but it is a function of n so we'll call it a log n complexity.

```
    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

c) O(n), the function is being called recursively n times so it is linear.

```
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II


The simplest solution is to start incrementing from the first or the last floor and stop when and egg breaks/survives. This solution gives us O(n) complexity since the worst case is if we start at 0 and f = n, so we iterate through the entire list once.


Let's say floors is a list of floors, so every floor under f returns 1 egg, but f and every floor afterwards returns 0 eggs.

This means that I'm looking for a sequence of 10, and the 0 in that sequence == f.

I can break up the floors into sequences of 2 and then binary search accross these sequences until I find one that matches '10'

find_f(floors, target='10'):

    sequences = [floors[i:i+1] for i in range(0, len(floors))]

    target_sequence = binary_search_recursive(sequences, target, 0, len(sequences)):

        if high >= low:
          middle = (low + (high - low)) // 2

        # Catches the issue of the sequence getting stuck at 1
        if middle == low:
            middle +=1

        item = sequences[middle]

        if item == target:
            return middle
        
        elif item == '11':
            return binary_search_recursive(arr, target, middle+1, high )
      
        else: #IF THE ITEM = '00'
            return binary_search_recursive(arr, target, low, middle-1)


    return floors.index(target_sequence[1])
    

