Add your answers to the Algorithms exercises here.

a.)
 ```
 a = 0 

 This is a variable assignment, or primitive operation, and thus will only run once, meaning it has a constant run-tim(e, or O(1).
 
 while (a < n * n * n):

 This is a loop, where the condition (which may also technically set our base case as a > n),
 is an inequality comparison between n and a variable, meaning it is dependent upon n, and thus,
 the run-time is linear, or O(n).

  a = a + n * n

  This line is a variable assignment, meaning it's run-time is constant, or O(1).

  So we have: 
   
  O(1) + O(n) * O(1).

  We multiply O(n) and O(1), giving us O(n), and add to that O(1), giving us O(n+1),
  over time, the 1 will become irrelevant, allowing us to drop it for a run-time of O(n).


 ```
b.)