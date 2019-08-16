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
