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
  



  ## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

What I envision being the best and most effective way to minimize egg loss is to base my algorithm on halves. Based on the half floor result, we can adjust our target by half each time to find the exact floor which breaks the egg. Each time, the algorithm will limit the range to search from by half the number, previously.


def egg_toss(n, f):
    floors = [1,n] 
    u = floors[1]
    l = floors[0]
    while floors[1]-floors[0] > 1:
        mid = l + (u-l + 1)//2
        if mid >=f:
            u = mid
            floors = [l,u]
        else:
            l = mid
            floors = [l,u]
    if u == f:
        return print(u)
    else:
        return print(l)



def egg_toss(n, f):
    floors = [1,n] -- O(1)
    u = floors[1] -- O(1)
    l = floors[0] -- O(1)
    while floors[1]-floors[0] > 1: -- between O(log(n)) and O(n)
        mid = l + (u-l + 1)//2 -- O(1)
        if mid >=f: -- O(1)
            u = mid -- O(1)
            floors = [l,u] -- O(1)
        else: -- O(1)
            l = mid -- O(1)
            floors = [l,u] -- O(1)
    if u == f: -- O(1)
        return print(u) -- O(1)
    else: -- O(1)
        return print(l) -- O(1)


#Because there are many assignments and if conditions that run once, many of the big O numbers resolve to a constant run time. The only part that is a factor in the big O number is the while loop. I estimated it to be between
O(log(n)) and O(n).