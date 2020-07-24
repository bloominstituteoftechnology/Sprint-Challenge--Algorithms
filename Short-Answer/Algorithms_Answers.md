#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) - 0(n)
despite there being a multiplication factor of "n _ n _ n" and "n _ n_" in this solution, they create a constant variable (3n + 2n) which we remove in the final classification as they are less meaningful than the initial time comlplexity of looping through "n" to begin with. We simplify the expression to it's largest component of complexity. In this case: 0(n)

b) - 0(n)
Okay here we go....
  
 for i in range(n): 0(n)

    the initial for loop takes in a variable of N with an
    unknown range therefore the iteration will be dependant on the size of n. 0(n)

      j = 1 0
      while j < n:
        j *= 2
        sum += 1
    Each line here evaluates as a constant as no part of this time complexity changes based on the size of n. Each pass the loop instruction performs a single operation regardless of the number of times it is executed making it 0(1) which is secondary time complexity presented in the initial for loop 0(n)


    0(n), final answer Penny

c) 0(n)
My intial thought was that this was a 0(1) but then realized the default return actually invokes the function again with adjusted parameters qualifying this as a recursive function that takes in n, and therefore the number of loops required to resolve to the base case of 0 to exit the loop varies by the value of the input.

    I'm going to go with 0(n), final answer unless i have a lifeline left to use...

## Exercise II

Assuming an input of a sorted list of integers as floor values.

My solution algorithm would incorporate a binary search tree that would evaluate to the mid point of the list and execute a function that drops an egg and checks to see if it breaks or not.

if the egg does not break, I know that the maximum height from which an egg can be dropped is not contained in the left half of the list, reset the previous midpoint + 1 as the new start point and repeat the search on the right half of the list.

If the egg does break, I know that the maximum height from which an egg can be dropped without breaking is contained on the left half of the list, and I would then reset current the mid point -1 as the new end point and perform the search again on the left side of the list.

Repeat this until i have found the the 2 floors where the egg is dropped and breaks but does not break if dropped from the floor below it.

Time complexity of this: 0(logn) as the size the data set is reduced by half for each iteratrion of the loop until the base case is found.
