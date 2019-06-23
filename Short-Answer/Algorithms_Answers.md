Add your answers to the Algorithms exercises here.

I need to spend more time with big O calculating. 

A: Question:
    a = 0   # O(1) Assignment so constant
    while (a < n * n * n):  # O(n^3) N is cubed here. However a = a + n^2 (n squared) That would increase the rate a overtakes N
      a = a + n * n # O(1) Assignment so constant
    
    Answer: O(n)
    Reason: 
    If n = 10
    a = 0
    while a is less than n^3 : n = 1000
        a = a + n^2 : n^2 = 100 # It adds 100 each time so the while loop runs n times 

B: Question:
    sum = 0 # O(1) Assignment so constant
    for i in range(n): # O(n)
      i += 1    # O(1) Assignment so constant i = 1
      for j in range(i + 1, n): #O(n^2) 
        j += 1  # O(1) Assignment so constant j = 3
        for k in range(j + 1, n): # O(n^3)
          k += 1    # O(1) Assignment so constant
          for l in range(k + 1, 10 + k): # O(n^4) Even though we're setting the end of the range to 10 + k, k will always be growing towards n each full loop.
            l += 1  # O(1) Assignment so constant
            sum += 1    # O(1) Assignment so constant
    
    Answer: O(n^4) : 
    Reason:
    Because as n grows the i + 1, j + 1 etc. Becomes less significant. 
    The final case l the range(k + 1, 10 + k) will always run at least from 4 -> n because k is set to run through the size of n

    If n = 10
    sum = 0
    for i in range n : 0 -> 10
        this loop will run at least O(n)
        i += 1
        for j in range(i + 1, n) : On the first loop i + 1 = 2 so 2 -> 10
            j += 1 : j = 3
            for k in range(j + 1, n) : On the first loop j = 3 so 3 -> 10

C: Question:
    def bunnyEars(bunnies):
        if bunnies == 0:
            return 0

        return 2 + bunnyEars(bunnies-1)

    Answer: O(n)
    Because bunnyEars will always call itself n times
        n = 10
        bunnyEars(10-1) -> 9
        bunnyEars(9-1) -> 8
        bunnyEars(8-1) -> 7
        And so on

## Exercise II
We know the building is sorted because it's a building. So each floor will always be one value higher.
Goto the middle of the building. 
curFloor = _n_ // 2
Now drop an egg. If it breaks go down a floor and check it.
    if dropEgg(curFloor) == breaks:
        while dropEgg(curFloor) == breaks:
            possibleN = curFloor # This may be the final floor it breaks on so.. set it and go down a floor
            curFloor -= 1
    else: # The egg didn't break at the middle floor so we need to go up
        # Go up the floors dropping eggs until 
        while dropEgg(curFloor) != breaks:
            curFloor++
        Once the egg breaks we're out of the while loop. Which means the _n_ floor is the floor we're on when we checked last. 
        possibleN = curFloor

The runtime of this is O(log n) because we only ever need to search half of n.. 