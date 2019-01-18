Add your answers to the Algorithms exercises here.

Exercise 1:
a) O(n^3).  The 'while' loop will run 'n * n * n' more times as n gets larger.  Therefore, the run time will increase as a factor of 'n' cubed.

b) O(n). Each 'for' loop runs in constant time, so O(n + n + n + n) -> O(4n) -> O(n) because constants are disregarded.

c) O(n). bunnyEars is called 'bunnies' times until 'bunnies' == 0.

Exercise 2:

Apply a binary search algorithm.  Start at the n/2 floor.  If the egg breaks, go to n/4...  If the egg doesn't break, go to n/2 + n/4...
Recur.