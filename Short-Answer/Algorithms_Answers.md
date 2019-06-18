Add your answers to the Algorithms exercises here.

Exercise I

a)
Line 1  = O(1) - setting a variable is constant
Line 2 = O(n) - how many times this runs depends on n's value
Line 3 = O(1)

1 + n * 1
1 + n
 
Big O = O(n)

b)
Line 1 = O(1) - setting variable is constant
Line 2 = O(n) - depends on n's value
Line 3 = O(1) - single operation
Line 4 = O(n) - depends on n's value
Line 5 = O(1) - single operation
Line 6 = O(n) - depends on n's value
Line 7 = O(1) - single operation
Line 8 = O(1) - k will only run a certain number of times regardless of what k is
Line 9 = O(1) - single operation
Line 10 = O(1) - single operation

1 + (n * (1 + (n * (1 + (n * (1 + (1 * (1 +1))))))

Big O = O(n^3)

c)
    I believe this would be Big O of O(n). With the recursive call, it's just continuing to call itself -1 until it reaches 0 and is only really dependent based on the number that variable bunnies represents
    


Exercise II

initialize boolean value of broken egg to false
intialize counter variable to 0

while "egg is unbroken" loop:
    drop the egg

    if egg breaks:
        change boolean value to true 
        log counter variable as being floor f
    else:
        repeat function with counter increased by 1

The Big O of this should be O(n)        