Add your answers to the Algorithms exercises here.



a)  a = 0 -- O(1)
    while (a < n * n * n): -- O(n**3) 

#Any assignments like a = 0, will have a constant run time. The run time for loops depends on how many times the loop will run at its worst. This loop will need to run n**3 times
      a = a + n * n -- O(1) #Because it is an assignment,it only runs once.

  Total big O number = 1 + 1 * n**3 = 1 + n**3 = O(n**3)
  
  # You keep the biggest number, in this case, n**3, the  1 is dropped.
```

```
b)  sum = 0 -- O(1)
    for i in range(n): -- O(n)
      i += 1 -- O(1)
      for j in range(i + 1, n): -- O(n - (i+1))
        j += 1 -- O(1)
        for k in range(j + 1, n): -- O(n - (j+1))
          k += 1 -- O(1)
          for l in range(k + 1, 10 + k): -- O((10+k) - (k+1)) =O(1)  #all constants have O(1) 
            l += 1 -- O(1)
            sum += 1 -- O(1)

    Total big O number = 1 + n*(1 + (n - (i+1))*(1 + n - (j+1)) * 1 = n*((n - (i+1))*(n - (j+1))

    O(n**3)

#Any assignments like sum = 0, i+=1, j+=1, k+=1, l+=1, or sum+=1 will have a constant run time. The run time for loops depends on how many times the loop will run at its worst. The last loop will run a total number of 9 times, therefore, a constant means O(1), the other loops really depend on the values of the other variables. However, at most if the variables started at the minimum of 0, each loop would run a max of n - 1 times. It may be safe to reduce all of these down,
# You keep the biggest number, as well as drop the smaller ones... it seems to reduce to n**3.

```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0: -- O(1)
        return 0 -- O(1)

      return 2 + bunnyEars(bunnies-1) -- O(1)
```

#Total big O number = 0(1) #I believe the number resolves to O(1), because even though it seems like there is some sort of variable big O, the final return of the call stack, and tHe following returns resolve to a constant number. Constants have a O(1).
  



  