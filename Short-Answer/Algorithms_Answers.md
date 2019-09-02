#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

a)  a = 0
    while (a < n * n * n):0(n3)
      a = a + n * n  0(c)

Ans : This program has a runtime of 0(n). While loop will run n*n*n/n*n times since in each iteration of while loop, a is
incremented by n*n times.   
 
b)  sum = 0 0(c)
    for i in range(n): 0(n)
      i += 1
      for j in range(i + 1, n): 0(n)
        j += 1
        for k in range(j + 1, n):O(n)
          k += 1
          for l in range(k + 1, 10 + k):10
            l += 1
            sum += 1 
            
Ans : we have 4 nested for loops. Top three are linear with n, but last one runs 10 times each time. So the total runtime will be
 n*n*n*10=10n*n*n*n we will ignore the constant 10 so it will be 0(n**3)    
 
c)  def bunnyEars(bunnies):
      if bunnies == 0: 0(c)
        return 0  0(c)

        return 2 + bunnyEars(bunnies-1) O(n) 
Ans : This is a recursive function call, with one function call per recursion. So if there are 4 bunnies then the function is recursively call for 3, 2,1 bunny 
  respectively. Hence  It will be a linear function of n.  
  
  
## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown
 off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_.
  Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

Ans : 
To find out the floor f from which the egg will not break  we  can start from nth floor  or 1st floor and go linearly to check where egg breaks/does not break.
But this approach is not optimum in terms of run time. This will require n eggs in worst case.

We can apply binary search here, So we will start from middle floor and this way we can neglect one half of the floor  

middle floor = highestfloor+lowest floor//2

Let's say middle floor is the 5th floor and 
  - egg breaks from 5th floor , so we hve to test the lower floor that is the 4th floor, left side of the array
  - egg does not break, so we have to go upper floor

Like binary search, we continue to find eliminate and find right floor.

We can think of this as binary search of a key, but finding leftmost occurance of it.
Lets say, we represent floors as array index, and store 0 at each floor if egg does not break, 1 if it does.
For example,
  floors = [0,0,0,1,1,1,1,1] <- Indicates egg does break on 1st, 2nd and 3rd floor. And it starts to break from 4th floor.
Now problem reduces to finding leftmost occurance of key 1 in this sorted array


so, 
```python
def find_min_floor(floors):
    last_floor_seen = None
    low, high = 0, len(floors)
    while low <= high:
        mid = (low + high) //2 
        if floors[mid]  == 1: #We find one occurance of 1, go left to check there are more
            last_floor_seen = mid
            high = mid -1
        else: #We found 0, 1 will be right of it. So go right.
            low = mid + 1
        
    return last_floor_seen   
```     
        
                  

