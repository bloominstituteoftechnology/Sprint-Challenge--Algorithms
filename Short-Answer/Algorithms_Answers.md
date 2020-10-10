#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime for this problem is O(N). The problem grows linearly meaning it
   is on a 1:1 scale


b) The running time for this problem is O(n log(n)) since we have two loops that
   are multiplied together. The parent loop is n and the child loop is log(n).

c) The running time is O(N) this one is also growing linearly.

## Exercise II
First we check the midpoint(n/2) of the nth floors and see how many if any eggs have
broken. If no eggs have broken then we check the midpoint between the
 (n/2)floor to the nth floor and see if any eggs have broken. We keep checking
 the midpoint of the top half until we find a broken egg once we do we stop at
 that midpoint and move to the bottom half and once again check the midpoint
 floor and start the process over again until we find the floor were the eggs
 first start breaking. This would be log_2(n). The time complexity is O(log(N)). 
