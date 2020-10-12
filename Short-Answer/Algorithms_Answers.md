#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -- run time increases linearly as n increases. Single loop.


b) O(n^2) -- 2 loops. So run time increases twice as n increases. 


c)  It is O(n) because the runtime will increase at a constant pace with the size of the input. 

## Exercise II

Binary search is best way to go about this. 

1. Drop the egg on floor 1, if it breaks then f =0 and end program

2. if egg does not break. 
    halve the total num of floors, if total floors is odd then move to 1 floor lower. 
        drop egg
            if it breaks, consider this floor as top floor. Move to middle of 1st floor and current floor. 
            if its does not break, consider this as bottom floor. move to middle floor of topmost and current floor. 

3. follow above process and find the floor where egg does not break, move 1 floor ahead and find where it does not. 

4. this is give the 'f' answer. 

