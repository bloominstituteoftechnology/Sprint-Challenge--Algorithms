Add your answers to the Algorithms exercises here.

a-  a = 0
    while (a < n * n * n):
      a = a + n * n


      0(n) -- linear. As N increases, the amount of steps for the loop increases


b-  sum = 0

    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1


    0(n^3) -- at the first loop we are at 0(n) x 3 additional nested loops



    c-  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)


      0(n) because as the variable increases, the function calls itself more times.