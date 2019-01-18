## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n) 
      a = a + n * n
```
##Answer a): 
0(n) the while loop creates linear, 1:1 growth of operation based on the input of n. It only grows at magnitude of n because n*n*n / n*n reduces to n. 

```
b)  sum = 0 --- c
    for (i = 0; i < n; i++) -- n
      for (j = i + 1; j < n; j++) -- n
        for (k = j + 1; k < n; k++) -- n
          for (l = k + 1; l < 10 + k; l++) -- c
            sum++
```
##Answer b): 
O(n^3) for loop has 3 nested O(n) statements, nested n growth is multiplied, so n*n*n will give this loop an O(n^3)

```
c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0 --- c
      return 2 + bunnyEars(bunnies-1) --- n
    }
```
##Answer c): 
O(n), bunnies will run the number of times n is equal to until reaching 0 


## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

##Answer exercise II 
<br> I'm assuming the unstated question in this exercise is figuring out at which point eggs get broken. A linear search, going floor by floor could mean dropping as many eggs as _n_ is large - 1 resulting in eggs being dropped at an O(n) growth curve. Another approach that would lead to less egg dropping, more precisely could at best be dropped at a scale of O(logN) in the discovery process would be doing a binary search for the magic floor. We would start somewhere in the middle of n-story building, drop an egg if it doesn't break, we will move up half again, if it does break we will move down half again and so forth until we discover the magical floor. This will most likely result in far fewer dropped eggs than starting at the top or bottom of the building and checking floor by floor. 
