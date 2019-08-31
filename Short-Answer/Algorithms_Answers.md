#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
   The number of times is based on the value of 'n'.

b) O(n^2)
   There are 2 checks for 'n' and to me this would result in the complexity of n^2.

c) O(2^n)
   This one is tricky in that I feel recursion is very tricky. Based on previous experience with cases like this, my guess it will be 2^n, plus recursion is not very efficient.

## Exercise II

We have a building with 'n' number of stories and many eggs.
if we drop eggs from floor 'f' or higher they break. If under floor 'f' they will not break.

if current_floor >= f:
  return 'egg will break'
else:
  return 'egg will not break'

I think this is O(1) because current_floor is either >= 'f' or it is < so I feel the time complexity should be simple.