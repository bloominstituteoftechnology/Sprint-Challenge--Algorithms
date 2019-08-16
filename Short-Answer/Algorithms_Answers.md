A) 
    a = 0
    while(a < n^3)
        a = a + n^2

    O(n) - This function has a linear runtime because as N gets bigger the longer the function will run for a to become > or = to n. For example, when n = 2 the number of loops the function runs is also 2. When n = 3 the loop count is 3. When n = 4 the loop count is 4, etc etc. 

B) sum =  0
    for ... n
    ...
    for j ... n^2
    ...
    for k ... n^2
    ...
    for l ... n^2

    O(n^7) - This function's nested loops all rely on the size of n and have a horrible run time. I believe you multiply the big o of each loop and drop the constants involved as they don't make much of a difference at all when n becomes a huge number. 


C) O(n) - The recursive function is being called n times before reaching the base case of bunnies == 0, so it runs linearly.


## Exercise II
To begin with the naive solution would have to be as follows...

Starting from floor 1 until top of building __n__ drop an egg and have a function return whether the egg is safe or broken. If it is broken return the story number from which the egg was dropped. If not the loop continues until it reaches the story where the egg is broken, this is __f__ the floor we want.

The problem with this algorithm is that the number of times required to run to find __f__ would always be equal to __f__. So if __f__ is an insanely huge number then our algorithm will waste an equally insane amount of time dropping eggs to find __f__. A quicker way to find __f__ would be to do a binary search where we begin the first egg drop at the midpoint floor of __n__ storied building. Then if the egg breaks we know __f__ must be lower or equal to the midpoint, we could rule out half the stories of the building being __f__ with our very first drop. If the egg does not break then we know it must be higher than the midpoint. From there the algorithm will definitely take less time to find __f__ as we check the remaining stories by binary search.
