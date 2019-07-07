Add your answers to the Algorithms exercises here.

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
a). Answer:- 0(1)+ 0(n) * 0(1) = 0(n)


```
b)  sum = 0   ---> 0(1)  ----> 0(n^3) + 0(1) ---> 0(n^3)  Cubic
    for i in range(n): ---> 0(n)  ---> 0(n) * [0(1)+0(n^2)] ---> 0(n^3)
      i += 1           ---> 0(1)
      for j in range(i + 1, n): ---> 0(n-1)   ---> 0(n-1) * [0(1)+ 0(n)] --> 0(n^2)
        j += 1                  ---> 0(1)
        for k in range(j + 1, n): --> 0(n-2)  ---> 0(n-2) * (0(1)+ 0(1)) --> 0(n-2)*0(2) --> 0(2n-4) --> 0(n) Linear
          k += 1                  ---> 0(1)
          for l in range(k + 1, 10 + k): --->0(9)  ---> 0(9) * (0(1)+0(1)) --> 0(9)*0(1) --> 0(9) ----> 0(1) Constant
            l += 1                      --> 0(1)
            sum += 1                    --> 0(1) 
``` 
b) .Answer:-  From bottom to the top ---> It is cubic 0(n^3)



```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
C)  Answer:- Linear --> 0(n)