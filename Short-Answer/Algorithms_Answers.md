#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Outter while loop is O(n^3), but the computation is incrementing
    by n^2. So the n^2 cancel out two of the n's in n^3 making it O(n).


b) If n was 10 the for loop would essentially go through n many times
    making it O(n).
    The while part is O(log n) because you are incrementing j *2 each time going
    through it which is halving the computation each time.
    Thus you get O(n log n).


c) You essentially have to go through each of the bunnies in the
    bunnyEars; you hit each item in the collection that is passed in making it O(n).

## Exercise II
story_building = 0
breaking_egg_point >= f
doesn't_break < f

dropped_eggs = 0
broken_eggs = 0
dropped_and_broken = dropped_eggs + broken_eggs
'''

'''
start on the first floor of the building and drop an egg (story_building += 1, dropped_eggs += 1)
    If it doesn't break then you are good.
    If it does break you have found the value of f

def find_egg_breaking_point():              
    story_building = 0
    f = random_int?
    dropped_eggs = 0
    broken_eggs = 0
    egg_break = YES
    dropped_and_broken = dropped_eggs + broken_eggs
    while egg_break == YES:
        if story_building = f:
            egg_break = NO
        else:
            story_building += 1
            dropped_eggs += 1
            broken_eggs += 1
            find_egg_breaking_point()
    print(f"Eggs break on the {story_building}th level.")

# O(log n)?
