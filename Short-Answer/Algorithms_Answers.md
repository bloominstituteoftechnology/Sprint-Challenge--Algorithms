#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n^2)


c) O(1)

## Exercise II

def find_perfect_floor(n):
  f would be set to the value n // 2 representing the first floor to drop and egg at rounding for if n was not even
  I would have a boolean flag for egg broke set to true
  while egg broke was true 
    start at floor f, drop an egg
    if the egg broke, that means I am too high so I would set f value to be current floor (f) // 2
    this would continue until I found a floor that egg broke is false
  once the first floor was found which the egg didn't break, I would increment the floors 1 until it broke
  while egg broke is false 
    drop egg
    increment floor count 
  When the egg breaks you have found floor f
  return f

  This solution would be O(log n)