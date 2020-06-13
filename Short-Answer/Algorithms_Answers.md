#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  Line by line: 1) equality, 2) while loop, 2a) arithmetic 
    The time complexity is:
        O(1 + (n * 1))
        O(1 + n) ...we always want the highest value
        O(n)

b)  Line by line: 1) equality, 2) for loop, 2a) equality, 2b) while loop, 2bi) aritmetic, 2bii) arithmetic
    The time complexity is:
        O(1 + (n * 1 *(n * 1 * 1)))
        O(1 + n * n) ...we always want the highest value
        O(n^2)


c)  Line by line: 1) if statement, 2) return constant, 3) linear recursive return
    The time complexity is:
        O(n)...due to recursing n times in linear fashion


## Exercise II

U   -   We want to find the lowest floor at which an egg would break if thrown from that floor
        To do that we need to find the last floor that the egg doesn't break, and the first floor that it does

P   -   I think the best way to do this is to go by halves, in a binary search fashion

E--
drop and egg on the first floor
-if the egg breaks then you know f is 0
-if the egg does not break:
    First halving
    go to the middle floor of the building
    -if even number then the lower middle floor (this is how we will handle division moving forward)
    drop an egg
    -if the egg does not break:
        --this floor is considered your bottom floor 
        --then go to the middle of the current floors and top floor drop an egg
        --do this until the egg breaks

    -if the egg breaks:
        --this floor is now considered your top floor
        --go back down to the middle of the bottom floor and current floor
        --drop an egg

## --From here we will follow the rules set out above 
-we follow these steps until we get find the last floor that the egg doesn't break, and the first floor that it does

In a building of 100 floors, if the f floor was 66 we would find it in len[50, 75, 62, 68, 65, 66] = 6 steps

The runtime complexity of a binary search tree is O(logn) 

