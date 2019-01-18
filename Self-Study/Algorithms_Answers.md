Add your answers to the Algorithms exercises here.


a) a = 0  # O(1) constant time
   while (a < n * n * n) # O(n) only iterating once from 0 to n^3
      a = a + n * n  # O(1) constant time - not iterating. 
   ### The runtime is O(n) * O(1) = O(n)

b) sum = 0  # O(1) constant time
    for (i = 0; i < n; i++)  # O(n)
      for (j = i + 1; j < n; j++)  # O(n)
        for (k = j + 1; k < n; k++)  # O(n)
          for (l = k + 1; l < 10 + k; l++)  # O(n)
            sum++ # O(1) constant time

### The runtime is O(n) * O(n) * O(n) * O(n) since they are all nested we multiply them so the runtime would be O(n^4)

c) bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1) # O(n)
    }

   ### with the recursive function we are iterating through the arr - 1 with each recursion. so the runtime would be O(n)

Exercise II 

set variable for drops
base cases for floors = 0 would be no drops are needed so return 0
base case for floors = 1 if breaks return 1 else return 0
find pivot which is length of floors//2
if egg breaks at pivot then drop egg again from floor - 1 and down until egg does not break
if egg does not break then drop from floor +1 and up until egg breaks
return number of drops needed to find breaking floor


getDrops(eggs, floors):
    if floors is 0 or floors is 1:
        return the floors

    if eggs is 1:
        return floors

    pivot is floors//2

    if egg breaks at pivot:
        for n in range floors[:-pivot]:
            if egg does not break at n:
                return n + 1
    else:
        for n in range floors[pivot:]:
            if egg breaks at n:
                return n