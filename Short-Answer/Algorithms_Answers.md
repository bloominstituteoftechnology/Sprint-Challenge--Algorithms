#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime would be O(n). This one seems decieving as one might think it was O(n^3) based on the while loop, but as a is increasing by n^2. It will run n times before a = n^3. 


b) Runtime is O(nlogn). There is one for loop that will run through the range of n and w while loop that will run through half of n. 


c)Runtime is O(n). This function will run n times to sum the number of bunny ears for n bunnies. 

## Exercise II
Given the n-floors:

Start at f = n / 2.

Drop_Egg_at_floor(f, f_broken = n):

    if f_broken := f + 1:
        return f

    drop egg
    
    If egg := broken, 
        then
             f_broken := f
             f = f // 2
            
    Then f_broken := f
    
    Drop_Egg_at_floor(f, f_broken)

    Else:
        
        f = (f_broken + f) / 2 

        Drop_Egg_at_floor(f, f_broken)
    
The runtime complexity is O(logn) as it would divide n in half and then the floors in half. 