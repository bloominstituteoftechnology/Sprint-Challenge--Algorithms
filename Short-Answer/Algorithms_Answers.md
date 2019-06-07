Add your answers to the Algorithms exercises here.

```
a)  a = 0                     O(1)
    while (a < n * n * n):    O(n^3) 
      a = a + n * n           O(log(n))
```

O(1) + O(n^3) + O(log(n)) --> O(n)
<br>
In this case, the O(log(n)) in the while loop is "holding back" the exponential run time of the loop. The two n's being multiplied within of the loop would cancel out two of the n's of the loop, leaving just n or O(n).

```
b)  sum = 0                               O(1)
    for i in range(n):                    O(n)
      i += 1                              O(1) 
      for j in range(i + 1, n):           O(n - 3)
        j += 1                            O(1)
        for k in range(j + 1, n):         O(n - 5)
          k += 1                          O(1)
          for l in range(k + 1, 10 + k):  O(n + 2)
            l += 1                        O(1)
            sum += 1                      O(1)
```
O(n^4)
<br>
The time complexity is exponential x^4 because each loop has approximately O(n) complexity. In total 4 loops would be: n * n * n * n, equaling n^4.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

O(n)
<br>
`bunnyEars` will get called however many times `bunnies` is equal to because if `bunnies` is greater than 0 it will call itself, each time decrementing by 1. It is essentially like a decrementing for loop using i--.
