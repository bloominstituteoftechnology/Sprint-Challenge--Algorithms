#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is linear time, O(n), because every time you go through the loop, you are 1/n of the way to finishing all the iterations of the loop. Why 1/n? You are adding n^2 every time, so that makes it faster. But aren't you having to get to n^3 iterations of the loop? No. You are getting the variable, a, up to a value of n^3, but you're doing this really quickly because each iteration, you are adding n^2. The only caveat I'd add is that you need to make sure n is not a negative number. Or the run increases significantly ;)


b) This is log-linear time, O(n log n). The reason for this is that the completion condition for the while loop is j being equal to or more than n. J is doubling every time the while loop runs this is log time. The while loop then runs once for every number up to n. This is linear time. It runs log time, linear "times" (n log n).


c) This is also linear time. You will run this function once for each bunny.

## Exercise II
This is a binary search. Runtime is O(log n). Algorithm below:

Start on the ground floor
Go to the middle floor between where you are and the top.
Repeat the below until you find floor f.
	Drop the egg.
	If it breaks, move to the middle floor beteween where you are and the ground floor.
	If it doesn't break, move to the middle floor between where you are and the top floor.
	Once you find the highest floor it doesn't break on, that's floor f.


