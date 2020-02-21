#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
a < n _ n _ n
a = a + n _ n
not sure if this is how it works but I'm subtracting the n _ n in the second statement which leaves me with 1 n
b)
O(n log n)
for i in range(n): this is n
j = 1
while j < n:
j \*= 2 this halves the n making it log n
sum += 1

c)
O(n)
the recursion is only calling itself n - 1 times and the body has an O of O(1)

## Exercise II

if the egg breaks, return floor
start with floor zero
for each floor from zero till n
if drop egg breaks
return floor

should only break one egg

run time of O(n)
