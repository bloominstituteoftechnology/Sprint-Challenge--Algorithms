a) O(n) - linear time because as I would increase the value of n, the amount of steps needed for the while loop would increase. For example if I were to use 2 we would loop through twice but if I were to use 3 we had to go through 3 times.

n = 2
a = 0

while (0 < 8)
a = 0 + 4

while (4 < 8)
a = 4 + 4

2 loops through before the while loop would stop

if we used 3 though:
n = 3
a = 0

while (0<27)
a = 0+9

while (9<27)
a = 9 + 9

while (18<27)
a = 18 + 9

3 loops through before the while loop would stop


---------------------------------------------------------------------------

b)O(n^2) - quadratic time because as n increases the number of operations increases as a function of the input size n

n = 2, would perform 13 steps
n = 3, would perform 19 steps
n = 4, would perform 28 steps
n = 5, would perform 70 steps

As n increases the number of steps greatly increases 


---------------------------------------------------------------------------------

c)O(2^n) - exponential time because the function will call itself until it recursion has happened n amount of times.

----------------------------------------------------------------------------------



