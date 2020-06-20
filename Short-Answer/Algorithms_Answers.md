Add your answers to the Algorithms exercises here.
1. Run time is constant. There is no interating over n, so the size of n would not make a difference for the run time.

2. O(n), the length of n will determine the run time.  Will only loop through n one time.  Other operations are just constant

3.Will be O of n squared.  Because it is recursive.


4. Egg 

we can determine f by knowing which eggs broke and from which floor they were dropped.
Assuming an egg was dropped from each floor.
We would search for an egg that was broken dropped from the lowest floor.
By putting the floor with if the dropped egg was broken or not broken in a dictionary {7: broken}
we could iterate over the dictionary and append add keys of broken eggs to a list.
then search for the lowest value in the list.  