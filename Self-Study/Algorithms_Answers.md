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

n = # of stories
egg is broken if floor >= f
egg is safe if floor < f

n = 30

take 30 / 2 
if at floor 15 the egg breaks we will split in half again, n is now equal to 8(rounded up)

if at floor 8 the egg is safe we can go start to come up, 15 - 8 = 7. Divide the num / 2. We can now move to the 4th floor(rounded up)

if at floor 12 the egg breaks, we can now find the difference between 12 and 8 = 4 and divide by 2. 

If at floor 10 we can go ahead and check 11 which is the last number between 10 and 12

if at floor 11 we break the egg we know floor 10 is the last floor before the egg breaks

Conclusion: This algorithm is very similar to how a binary search would work which would make this function O(o log n ) 



