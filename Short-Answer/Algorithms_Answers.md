#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
i chose O of n because this function has a loop that runs n^3, but n^2 is being added to the counter so its only a linear loop.


b)O(n logn)
this is n log(n) beacuse first we have a loop that runs for every input element, then a second loop that runs for less then half of the input elements

c)O(n) 
this function runs a recursive call for every bunnie that is added to the input so its linear

## Exercise II
search through the floors and find the breaking point with as few steps as possible
use binary search - small step search method

While f is not found,
    if f == not break and f+1 == break, then f == found
    elif f==not break, then f = f+n/2  #middle of higher half
    else then f = f/2  #middle of lower half
return f



