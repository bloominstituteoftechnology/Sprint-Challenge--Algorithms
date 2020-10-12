#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1) - this is constant, will only run onnce


b) O(n log n)


c) O(n) - the function runs n times.

a) When broken down each line is O(1). Yet the while loops has it run an undetermined amount of times. This makes a constant time turn into an O(n) time complexity. Without further information on the full algorithm we cannot determine if there is a worse time complexity so we must insist this snippet of algorithm is O(n).

b) The first thought when seeing two loops in tandem is O(n^2). Then we must debate our instinct to make sure nothing in the algorithm stretches to a worse time complexity or better one. As we see each loop will run for each iteration it does conclude that this snippet of algorithm is O(n^2).

c) Since bunnies can be any number and we are doing an operation on each bunny/number and not just picking one bunny/number we know that this is not constant time automatically. Because we are only using one operation the worst time complexity of this algorithm is O(n).

## Exercise II

binary search building 
f = [1,2,3,4,5,6]
start= f[3]

if it doesn't break, go halfway between the midpoint you just dropped form and the top of the building. Repeat process from this new midpoint.if it breaks, go halfway between the point you just dropped from and the bottom of the building. repeat this process form this new endpoint.this is like binary search, and has a time complexity of O(log n)