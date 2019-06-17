Add your answers to the Algorithms exercises here.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a)  a = 0       O(1)
    while (a < n * n * n):   O(n)
      a = a + n * n        O(1)

O(1) + O(n) + O(1) == O(n)

** For a, the while loop is only incrementing a until it reaches n^3.
It could take a while given a large enough n, but it's still only doing one
function per iteration. **

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

b)  sum = 0                                 O(1)
    for i in range(n):                      O(n)
      i += 1                                O(1)
      for j in range(i + 1, n):             O(n^2)
        j += 1                              O(1)
        for k in range(j + 1, n):           O(n^3)
          k += 1                            O(1)
          for l in range(k + 1, 10 + k):    O(k + 10)
            l += 1                          O(1)
            sum += 1                        O(1)

** Since there are 2 nested for loops running to n, the time complexity
    should be O(n^3). We drop everything else because O(n^3) is significant enough that they don't matter. **

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

c)  def bunnyEars(bunnies):
      if bunnies == 0:                      O(n)
        return 0                            O(1)

      return 2 + bunnyEars(bunnies-1)       O(n)

** I think O(2n)? I'm not entirely sure on this one.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exercise II:

Binary search:

## Define some variables

    mid = len(_n_)/2
    unBrokenEgg = true
    newList = []

## Helper function
def eggDrop:
    if unBrokenEgg:
        return true
    else
        return false

## What to do with these variables

while len(newList) > 1:
    call eggDrop at mid:
        if eggDrop:
            newList = list.range(mid, len(_n_))
            mid = len(newList)/2
        
        else:
            newList = list.range(0, mid)
            mid = len(newList)/2


return newList

** Since we're not dropping an egg at every floor to see if it breaks, 
the time complexity is O(log n). **

    


