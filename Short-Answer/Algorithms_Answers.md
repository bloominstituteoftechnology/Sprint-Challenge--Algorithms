Please add your answers to the Analysis of Algorithms exercises here.
Exercise I

a)This loop has a run time of O(n). At first one might assume it is n^3, but because of the a it will only run n times, making it O(n).

b)This loop has a runtime of O(n^4) because there are 4 for loops. Each loop adds a N^1 which is why you should avoid for loops. 

c) This loop has a runtime of O(n) because it will loop through each bunny. There are n amount of bunnies giving it the O(n) runtime. 


Exercise II

This loop has a runtime of O(n) becayse I would use a binary search to go through the floors to rule out one half of the floors. 

Psduedo code:

floor_in_middle = highest_floor+lowest_floor//2(ironically, we must use floor division on this because you can't be on floor 2.5)

This means you have to loop through n floors to find where the egg broke.  


