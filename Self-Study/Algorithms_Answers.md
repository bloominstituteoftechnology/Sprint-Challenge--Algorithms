Add your answers to the Algorithms exercises here.
Exercise I:
a) first line is 1 and while function is linear and grows directly in proportion to n, so run time is 0(n).  O(n) dominates, it is the overall theoretical worst case. 
b) there are 4 for loops, so each has a run time of O(n), so overall run time is O(n^4).  we disregard sum = 0 as it is dominated. 
c)you have to run through all the n bunnies, so this is O(n).

Exercise II:
n = total floors
f = egg break floor
e = eggs
t = test floor

drop first egg at testfloor0.  if it breaks move to lower floor to test and if it does not break move to higher floor to test. this would be similar to a binary search.  or this could be done recursively starting from n-1:
[t + (t-1) + (t-2) + ...etc] = n
