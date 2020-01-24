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

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

There are two ways to solve this problem:

The naive way would be to use a linear search, starting from floor 0 and working your way up to floor n. Doing this would be an incredible waste of perfectly good eggs, but very healthy if you are taking the stairs and the building were VERY TALL... runtime of the linear search is O(n).

The  better way is to implement a binary search.  Start by dropping hte egg from the median between floor 0 anf floor n. If it breaks, that means you may have been too high. So you would then find the median between the floor you were on and floor 0. If the egg breaks now, you might still be too high, so you would again find the median of the current floor you are on and floor 0. This would be repeated until you met the criteria.  
If, on the other hand, the egg did not break after the first iteration, that means you were not high enough.  In this case, you would find the median of the floor you were on and floor n (the top), continuing to recursively search from the median of (current_floor, n) until the criteria are met. The runtime of the binary search is O(log n).