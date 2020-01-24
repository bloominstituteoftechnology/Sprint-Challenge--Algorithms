#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n^2); because the number iterations for j goes up in tandem as the input n increases.

b)
O(n); because there is one simple while loop therefore the number of operations grows linearly with the number input data.

c)
O(n); because although it is a recursive function, the number of operations grows linearly with the number input data (bunnies to ears)

## Exercise II


Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off
 floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the
  value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

inputs = building_height, eggs
constraint = f (threshold floor for broken egg)

def something(building_height, eggs, f):
    e = eggs
    broken_eggs = 0
    for floor in building_height:
        if (floor >= f) and (e > 0):
            e -= 1
            broken_eggs += 1
        if (floor < f) and (e > 0)):
            pass

