#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) The function only multiplies n. It's not running through it n times, like O(n^5) or something. Put another way, the loop ends when a reaches n^3. n^3 / n^2 = n. Therefore, it takes n loops. 


b) O(n^2) Inner and outer loop. Outer loop runs n times (in range of n). Meanwhile, the inner loop runs while j < n. J doubles each iteration, though.


c) O(n) Bunnies reduces by 1 each time. So it takes n times for the function to finish. 

## Exercise II

Binary search. You're searching through n floors until you find a floor, f, such that when you drop an egg from it to the bottom floor, the egg doesn't break. So if you start at the middle floor, you can determine whether you go up or down depending on the result (breaks, eliminate all higher floors. Doesn't break, go to the next middle floor between remaining floors and top floor). Eventually you hone in at the right floor, f. 
