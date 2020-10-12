#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
Runtime: 'O(n)'
Reasoning: Each iteration increases by n^2, and it is looking for 'a' to be greater than n^3.  
n^3 divided by n^2 gives us n, so O(n) runtime complexity.  

b)
Runtime: 'O(n log n)
Reasoning: The outer portion is 'O(n)', and the inner begins at 1 then doubles until it is greater than
n, giving it a O(log2 n) complexity.  Nested loops have their complexity multiplied, giving us O(n log n)

c)
Runtime: 'O(n)'
Reasoning: This algorithm calls itself recusrively.  A constant amount is subtracted each time, bringing 
it closer and closer to the base case of 0.  Due to the constant amount, and only one recursive call each iteration,
the number of steps will mimic a linear function.  

## Exercise II


