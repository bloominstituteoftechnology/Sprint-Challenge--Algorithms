#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
O(n) Linear- while loops through n items

b)
O(n^2) Quadratic- every element in a collection needs to be compared to ever other element.

c)
being called recursively n times before reaching base case so its O(n)

## Exercise II

Get the middle floor of the building by adding the lowest floor to the highest floor and divide by 2.
Go to the middle floor and drop the egg.
If it breaks, we know that anything higher than this middle would break the egg as well
Set the new highest floor to the floor below the middle (middle - 1)
Get the new middle floor and drop it again
Repeat until it doesn't break.
If it does not break we can set the lowest floor to the floor above the current middle (middle + 1)
Find the new middle between the low and high floor
Repeat until you find the floor lowest floor that doesn't break the egg
If for some reason the lowest floor ever exceeds the highest floor then your egg experiment is a fail
