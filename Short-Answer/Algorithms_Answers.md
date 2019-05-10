Add your answers to the Algorithms exercises here.


Exercise I

A. 
    Time Compexity = 0(n) --- Since when 3 is n the while loop runs three times when 4 is n the loop runs four times so it has a linear number of run time.

B. O(n * (n-1) * (n-2) * 10)  -> O(n^3)

C. 
    Time Complexity = 0(n) --- The function runs on the loop with the number of input bunnies so it runs n times as the number of bunnies



Exercise II

    Since we know in building floors are sorted from lowest to highest, we will use a binary search. We will go to the middle of the building and drop an egg. If the egg breaks, we will find middle of lower and midd half and drop an egg from that floor and ignore highest half. If the egg does not break, we will go to the upper half of the building and drop an egg. This should be repeated until we will find the floor number where egg is breaking but floor below it not.