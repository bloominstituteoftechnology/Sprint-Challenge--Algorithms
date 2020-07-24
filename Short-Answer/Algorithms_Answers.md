#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Big O (worst case runtime complexity): O(n)
Rationale: Because the variable *a* will increase by n^2 every iteration through the while loop (`a += n^2` each iteration, as below), *a* will equal n^3 after n iterations, causing the while loop to terminate. So the maximum number of iterations is n - 1, which simplifies to O(n) runtime complexity (i.e., if the number of input items *n* doubles, then the runtime will double in the worst case scenario).

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n         # O(n)
```

b) Big O (worst case runtime complexity): O(nlogn)
Rationale: The inner while loop has runtime O(logn), because j is 2^j in any given loop --> the number of loops = log2(n). The outer loop runs the inner loop for every input item, so the outer loop has a runtime complexity of O(n), which means the entire process has a Big O (worst case) runtime complexity of O(nlogn).

```
b)  sum = 0                 # Overall: O(n * logn) = O(nlogn)
    for i in range(n):      # O(n)
      j = 1
      while j < n:          # O(logn)
        j *= 2
        sum += 1
```


c) Big O (worst case runtime complexity): O(n)
Rationale: Even though this is recursive, it still effectively only runs once for every +1 increase in n (e.g., runs 16 times if bunnies=16, and 32 times if bunnies=32), so has a worst case runtime of O(n).

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Question: 
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

**Answer (Chris):**
If you care only about avoiding broken eggs, but do not care about optimizing runtime (the prompt says nothing about optimal runtime, only about breaking eggs), then the best approach for your needs would be a simple 1-by-1 iteration approach up from the bottom, as below. This would result in only 1 broken egg when floor = f.

Approach: Linear Search Starting on Lowest Floor
Runtime (Big O worst case): O(n)
```
# From each floor in the building, beginning with the ground floor:
def find_limit_floor(total_floors=n):
    for floor in range(total_floors):
        # Drop an egg and see if it breaks:
        if drop_egg_safely(floor_num=floor) == False:
            # If it breaks, return that floor number as f (the floor at+above which the egg breaks):
            return floor
```

BUT if you also care about ensuring the optimal runtime, and are willing to tradeoff a couple of broken eggs for a more compute- and time-efficient approach, a binary search algorithm would work better:

Approach: Binary Search
Runtime (Big O worst case): O(logn)

```
def binary_drop(bottom_floor, top_floor):
    # Base case: No more floors left to search:
    if bottom_floor > top_floor:
        return "No maximum floor found: Eggs can be safely dropped from any floor in this building."
    # Find the middle floor:
    middle_floor = (bottom_floor + top_floor) // 2
    # Determine whether the threshold floor f (at+above which the egg breaks) is below or above middle_floor:
    # If egg breaks from middle_floor, then threshold floor f is lower than middle_floor:
    if drop_egg-safely(floor_num=middle_floor) == False:
        return binary_drop(bottom_floor=bottom_floor, top_floor = middle_floor - 1)
    # If the egg does not break, then threshold floor f is above middle_floor:
    elif drop_egg-safely(floor_num=middle_floor) == True:
        return binary_drop(bottom_floor = middle_floor + 1, top_floor=top_floor)    
```
