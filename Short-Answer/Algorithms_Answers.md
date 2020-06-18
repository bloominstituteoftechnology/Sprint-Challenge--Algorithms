#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)  

The size of A is dependent on and directly proportional to the 
    size of n  ==> O(1 + 2n)

----------------------------------------------------------------------
b)O(logn)

As the size of the input increase, the runtime or space used will grow at
a slightly slower rate 

---------------------------------------------------------------------

c) O(n) 
 The number of bunnyEars is dependent on and directly proportional to the number 
    of bunnies  ==> O(2 + 2(n-1)) = O(2n)

----------------------------------------------------------------------

## Exercise II

## NOTE: 
For this example, I imagined a building where you enter on the ground floor ("0th") and it has 13 floors above that floor.


1.  Find the sum of the highest and lowest floors. 
2.  Divide by 2 to find the middle floor. 
3.  Define top floors (higher than middle floor).
4.  Define bottom floors (lower than middle floor).
5.  Go to the middle floor and drop an egg
6.  You have one of two choices at this point
        a.  If it doesn't break, go up to the middle of the top floors and drop another egg. 
        b.  If it does break, go to the middle of the bottom floors and drop another egg.

7.  You will repeat this pattern, moving up and/or down until you get to the 
    floor where you can safely drop your egg without breaking it.

The time complexity is O(n) since the number of floors you might have to try is 
directly proportional to the number of floors in the building.