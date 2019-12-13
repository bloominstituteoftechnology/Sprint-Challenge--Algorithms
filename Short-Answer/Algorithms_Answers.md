#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This code block uses the linear complexity classification that is denoted as O(n)
   due to the fact that the the number of operations only increases with in the increased 
   size of n.
  
  This code block can be reduced by:
  
  1. Taking `while(a < n*n*n):` = O(n<sup>3</sup>)
  2. And `a = a + n*n` = O(n<sup>2</sup>)
  3. Reducing O(n^3) by O(n<sup>2</sup>) because of inside loop incrementation
  4. Resulting in O(n<sup>1</sup>) == O(n) 


b) This code block uses notation of O(n log(n)). This is because as the input size
   increases the runtime space growth rate slightly improves.
  
  Here is how the code block reduces:
  
  1. Start with `for i in range(n):` = O(n)
  2. Next we evaluate `while j < n:` = O(n)
  3. Then `j *+ 2` = O(log(n))
  4. Because there are nested loops we multiply the reduced O(n) with O(log(n))
  5, Resulting in = O(n log(n))


c) Like code block in `a(` this code block results with a linear complexity classification
   of O(n). There is just one input that can increase in size and the number of operations
   will only increase with the size of the input.
   
   Here is the reduction of the code block:
   
   1. With `if bunnies == 0:` = O(1)
   2. And `return 2 + bunnyEars(bunnies-1)` = O(n)
   3. We get the reduction result of = O(n)
   

## Exercise II

#### Unanswered questions to this problem:
 1. Are the eggs real or fake?
 2. Are the eggs all raw and/or are they hard-boiled?
 3. Are all of the floors made of the same material?
 4. Why are we dropping the eggs? Motivation?
 5. What is the expected result and goal?
 
 #### Answer based on the info made available and without the answers to the above questions:
 
 <u>Binary Search Approach</u>
 
 1. Start on the middle floor and drop an egg. ```def egg_drop(): 
                                                    num_floors = n
                                                    mid_floor = floors // 2```  
 2. `if egg break == False: move halfway up to the top floor` 
 3. `if egg break == True: move halfway up to the bottom floor`
 4. Repeat the above steps in a loop until the the floor is reached with the lowest
    number of broken eggs.
    
  The average performance of the method results in a complexity of Linearithmic O(n log n).
 
 
 
  
