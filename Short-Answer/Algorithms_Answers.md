#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
a) O(n) = This is a linear algorithm, size of input affects runtime/space 
at the same rate. 
The while loop states: as n grows so does the runtime.
Acceptable Time complexity.

b) O(n*log n) = This is a logarithmic algorithm, as the size 
of input increases the runtime/space will grow at a slightly 
slower rate. 
Because there are two loops in order to satisfy the equation
it is does not keep the same time as n.
Pretty good time complexity.


c) O(n) = This is a linear algorithm, but it is also recursive.
It will continue to call itself till the requested answer is 
found. 
Acceptable Time complexity.


## Exercise II
 
(Devise a strategy to determine 
the value of f such that the number of dropped + broken eggs 
is minimized.
Write out your proposed algorithm in plain English or 
pseudocode AND give the runtime complexity of your solution.)


O(log n)
A binary search would be a good solution because n stories 
can be a large number.
(Suppose that you have an n-story building and plenty of eggs.)

You would need to loop through to a middle value floor to 
find f first, eliminating the higher values first 
# floor > f = broken eggs
So you would keep cutting the targets in half till you find
one that is # true thus eliminating all above it, then
again eliminating more till you find the # target 
(Suppose also that an egg gets broken if it is thrown off 
floor f or higher, and doesn't get broken if dropped off 
a floor less than floor f.)