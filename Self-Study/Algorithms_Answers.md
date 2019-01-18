Add your answers to the Algorithms exercises here.

Exercise I

A) Runtime for this algo is O(n). This is because a is advancing at a rate of n^2 and the loop runs only for n^3.

B) Runtime for this algo is O(n^3). This is because there are 3 nested loops that are going thru the entire length of n.
The constants are minutae compared to that so the average case becomes O(n^3).

C) I think this will be an infinite loop as the failure condition for the recursive method will not be met. (we will subtract 1 bunny but add 2).

Exercise II

A) The ideal strategy would be having to go thru each floor from the top most floor and drop 1 egg to see if it breaks or not. If it does not break we stop as we have found the safe floor. This would minimize the number of eggs destroyed while also giving us a correct answer. 
