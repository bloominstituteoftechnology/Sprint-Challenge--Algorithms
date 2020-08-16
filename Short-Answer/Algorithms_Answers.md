#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 


b) This is O(n^2). There is a loop inside of a loop. The run time is proportional to the input size of data set. 


c)The run time is O(n). Depending on how many bunnies we have, the run time will grow exactly with the size of the input.

## Exercise II

So, if dropped eggs < broken eggs, then that means that we are on a higher floor. If dropped eggs > broken eggs, than we are on a lower floor. 

I would write an alogorithm along these line...

if broken_eggs == 0:
    f = 0

elif dropped_eggs < broken_eggs:
    f += 1

elif dropped_eggs > broken_eggs:
    f -= 1

This will indicated that the higher we are, the more broken eggs we have. Conversely, if we have more dropped eggs than broken eggs, this will indicate that we are on a lower floor. If we have no broken eggs, we have to assume that we are on the ground level.

I think this will be a O(lon n) alogorithm, because the point is to find out floor we are on that minimizes the amount of broken eggs we have. Basically our f = 0 and we are trying t reduce the amount of f's.

