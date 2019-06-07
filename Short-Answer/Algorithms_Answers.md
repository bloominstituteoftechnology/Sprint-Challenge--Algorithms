Add your answers to the Algorithms exercises here.

## Exercise I

a) O(n^3)
> Initial while loop has running time of 0(n^3) (_although line inside loop causes the runtime to decrease twice exponentially_)
> Line inside while loop has running time of O(1) 

b) 0(n^4)
> Each of the four for loops has running time O(n)

c) O(n)
> Function runs "n" times according to the number of "bunnies" given since it's a recursive iteration

## Exercise II

> It seems that the best way to find floor _f_ while minimizing the number of eggs dropped is to do a _binary search_.
> Runtime coplexity with binary searches is _O(log n)_ (worst case scinario).

> 1. You would take your list and _find middle floor_.
> 2. Throw egg from middle floor.
> - If egg does not break, _ignore floors below middle_ (meaning eggs begin to break on one of the floors above).
> - If egg breaks, _ignore floors above middle_ (meaning eggs stop breaking in one of the floors below).
> 3. Repeat steps 1 through 2.
> 4. Once you find point where egg breaks next does not you have found _f_ floor.


