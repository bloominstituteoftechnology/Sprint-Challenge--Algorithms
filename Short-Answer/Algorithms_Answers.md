#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

(n^3) / (n^2) = n;
therefore, the runtime is O(n)


```python
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```


```python
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

In the absence of caching, memoization, or another runtime reduction method are O(c^n).

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


For a building of n floors, there exists a floor f which if eggs are thrown off of the bulding at any floor between 0 and f ,exclusive, the eggs will not be broken.

Given that the lower floors are more likely to have fewer eggs break, than the higher floors. A binary search approach, given that it would involve a fewer amount of tests compared with an itterative approach would most likely result in the fewest number of eggs damaged.

In this situation, we create a function find_f which takes in the building as an array with the 0 index representing the bottom floor, the -1 index representing the top floor, and each of its elements being the number of eggs broken if dropped from that floor (index position). This works because, like a sorted list, the number of eggs dropped will naturally increase with each successive floor.

```python
  
def find_f(building, f_minus_1=0, bottom=building[0], top=building[-1]):
    middle = (top + bottom) // 2
    if building[middle] == f_minus_1:
        return middle + 1
            
    elif building[middle] > f_minus_1:
        return find_f(building, target, middle, top - 1)
        
    elif building[middle] < f_minus_1:
        return find_f(building, target, middle + 1, top)

    # This accounts for the case that whatever the middle value winds up being zero. The next element, then, must naturally be checked if we're to find the top floor at which eggs are not to be broken.
    elif building[middle] == f_minus_1:
        while building[middle + 1] == f_minus_1:
        middle += 1
        return return find_f(building, target, middle + 1, top)

    else:
        return -1 # No floor is safe from eggs broken.
```

The runtime complexity of this is O(n), with Theta(log(n)) being the best case scenario and Theta(n) being the worst case scenario. Since the Binary Search algorithm doesn't need to visit every single positon, it can bypass the bulk of the top floors in its search for the floor f. Even in the worst case scenario that floor f is the top floor, the algorithm still bypasses at least half of the array's elements in it's search.
