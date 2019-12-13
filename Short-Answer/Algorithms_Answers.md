#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This would be O(log n) since as the input increases the runtime will grow at a slightly slower rate.


b) This would be O(n*log n) since the for loop is n and the while loop is log n.


c) This would be O(n) since all we are doing is subtracting 5 from n.

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

def drop(eggs):
    action to throw egg out

def testThenDrop(n-stories, eggs):
    i=0
    while i< n:
        if i ==f:
            break
        else:
            <!-- drop(eggs) -->
            
        i++

complexity log(n)
